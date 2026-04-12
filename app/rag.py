from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from anthropic import Anthropic
import os
from dotenv import load_dotenv

load_dotenv()

CHROMA_PATH = "chroma_db"

client = Anthropic()

def get_answer(question: str) -> str:
    # Load the vector store
    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    )

    # Search for relevant chunks
    results = vectorstore.similarity_search(question, k=4)

    # Build context from the chunks
    context = "\n\n".join([doc.page_content for doc in results])

    # Send to Claude with the context
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""Use the following context to answer the question. 
If the answer is not in the context, say "I don't have enough information to answer that."

Context:
{context}

Question: {question}"""
            }
        ]
    )

    return message.content[0].text