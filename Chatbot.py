
import re
import unicodedata


Inputs = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hi there! What can I do for you?",
    "how are you?": "I'm just a chatbot, but I'm here to help you!",
    "what is your name?": "I am jarvis a simple chatbot created to assist you.",
    "what can you do?": "I can answer simple questions and have a basic conversation with you.",
    "where are you from?": "I am a virtual assistant created by a developer.",
}

Exits = ["exit", "quit", "goodbye", "bye"]

def Sanitize(user_input): 
    user_input= user_input.strip() 
    user_input= re.sub(r'[\x00-\x1F\x7F]', '', user_input) 
    user_input = re.sub(r'\s+', ' ', user_input)
    user_input = unicodedata.normalize('NFKD', user_input)
    user_input = user_input.lower()
    return user_input

while True:
    user_input = input("You: ")
    user_input = Sanitize(user_input)
    if user_input in Exits:
        print("Chatbot: Goodbye!")
        break
    response = Inputs.get(user_input, "I'm sorry, I don't understand that.")
    print(f"Chatbot: {response}")
