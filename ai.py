import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))



def askAI(question):

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=f"""
        You are Jarvis, a smart personal voice assistant.

        Answer naturally in 2 to 3 short sentences.
        Include important facts and useful information.
        Use simple conversational English.
        Avoid unnecessary details.
        Do not use headings, bullet points or lists.

        Question: {question}
        """
    )

    return response.text


    
