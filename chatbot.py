def chatbot():
    print("Bot: Hello! I am your assistant. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "hello":
            print("Bot: Hi! How can I help you today?")
        elif user_input == "how are you":
            print("Bot: I am just a computer program, but I'm functioning perfectly!")
        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day!")
            break
        else:
            print("Bot: I'm sorry, I don't understand that.")

chatbot()