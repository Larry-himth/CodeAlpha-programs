print("ChatBot is running, Type something\n")

running = True

while(running):
    user_message = input("You: ").lower()
    
    if user_message == "hello" or user_message == "hi" or user_message == "hey":
        print("ChatBot: Hi!")
    elif user_message == "how are you" or user_message == "how are you doing":
        print("ChatBot: I'm fine, thanks!")
    elif user_message == "bye" or user_message == "stop":
        print("ChatBot: Goodbye!")
        running = False
    else:
        print("I dont understand!")