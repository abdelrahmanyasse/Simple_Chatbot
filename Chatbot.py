
import re


Inputs = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hi there! What can I do for you?",
    "how are you?": "I'm just a chatbot, but I'm here to help you!",
    "what is your name?": "I am jarvis a simple chatbot created to assist you.",
    "what can you do?": "I can answer simple questions and have a basic conversation with you.",
    "where are you from?": "I am a virtual assistant created by a developer.",
}

Exits = ["exit", "quit", "goodbye", "bye"]


while True:
    user_input = input("You: ")
    if user_input.lower() in Exits:
        print("Chatbot: Goodbye!")
        break
    response = Inputs.get(user_input.lower().strip(), "I'm sorry, I don't understand that.")
    print(f"Chatbot: {response}")
