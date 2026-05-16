import re
import unicodedata


inputs = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "i am very good, thank you for asking! How about you?",
    "what is your name": "I am jarvis a simple chatbot created to assist you.",
    "what can you do": "I can answer simple questions and have a basic conversation with you.",
    "where are you from": "I am a virtual assistant created by a developer.",
}

exits = ["exit", "quit", "goodbye", "bye","end chat","ciao"]

def Sanitize(user_input): 
    user_input= user_input.strip()
    user_input= re.sub(r'[\x00-\x1F\x7F]', '', user_input) 
    user_input = re.sub(r'\s+', ' ', user_input)
    user_input = re.sub(r'[^\w\s]', '', user_input)
    user_input = unicodedata.normalize('NFKC', user_input)
    user_input = user_input.lower()
    return user_input

while True:
    user_input = input("You: ")
    user_input = Sanitize(user_input)
    if user_input in exits:
        print("Chatbot: Goodbye!")
        break
    response = inputs.get(user_input, "I'm sorry, I don't understand that.")
    print(f"Chatbot: {response}")
