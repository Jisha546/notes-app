def simple_chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. How can I help you today?")

    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase for case-insensitive matching

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there! How are you doing?")
        elif "how are you" in user_input:
            print("Chatbot: I am just a program, but I'm functioning well. Thank you for asking!")
        elif "what is your name" in user_input:
            print("Chatbot: I don't have a name, I am a simple Python chatbot.")
        elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break  # Exit the loop and end the conversation
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you rephrase?")

# Run the chatbot
if __name__ == "__main__":
    simple_chatbot()