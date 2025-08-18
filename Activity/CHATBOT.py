responses = {
    "hi": "Hello there! How are you?",
    "hello": "Hi! Nice to see you.",
    "how are you": "I'm just a program, but I'm doing great! 😄",
    "your name": "I'm ChatBot 1.0, nice to meet you!",
    "bye": "Goodbye! Have a great day!"
}
print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ").lower()
    reply = responses.get(user_input, "Sorry, I don’t understand that.")
    print("Chatbot:", reply)
    if user_input == "bye":
        break