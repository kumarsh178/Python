from groq import Groq
from .rag import search
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
#client code should be here
client = Groq(api_key=groq_api_key)

def hospital_chat(question):

    context = search(question)

    prompt = f"""
You are a hospital assistant.

Hospital records:
{context}

Answer the question using the hospital data.

Question: {question}
"""

    chat = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return chat.choices[0].message.content