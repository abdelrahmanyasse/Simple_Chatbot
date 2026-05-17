import re
import unicodedata
import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-lite",  # higher free tier limits
    system_instruction="You are Jarvis, a helpful and friendly assistant."
)


chat = model.start_chat(history=[])

exits = ["exit", "quit", "goodbye", "bye","end chat","ciao"]

def sanitize(user_input): 
    user_input= user_input.strip()
    user_input= re.sub(r'[\x00-\x1F\x7F]', '', user_input) 
    user_input = re.sub(r'\s+', ' ', user_input)
    user_input = re.sub(r'[^\w\s]', '', user_input)
    user_input = unicodedata.normalize('NFKC', user_input)
    user_input = user_input.lower()
    return user_input

while True:
    user_input = input("You: ")
    sanitized = sanitize(user_input)

    if sanitized in exits:
        print("Jarvis: Goodbye!")
        break

    response = chat.send_message(sanitized)
    print(f"Jarvis: {response.text}")
