def chatbot():
    print("ChatBot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("ChatBot: Hi!")
        elif user == "how are you":
            print("ChatBot: I'm fine, thanks!")
        elif user == "what is your name":
            print("ChatBot: I am a simple chatbot.")
        elif user == "good morning":
            print("ChatBot: Good morning!")
        elif user == "thank you":
            print("ChatBot: You're welcome!")
        elif user == "who created you":
            print("ChatBot: I was created as a Python internship project.")
        elif user == "bye":
            print("ChatBot: Goodbye!")
            break
        else:
            print("ChatBot: Sorry, I don't understand that.")

chatbot()