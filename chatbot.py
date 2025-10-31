def chatbot():
    print("Hello! I am your friendly chatbot. (Type ‘bye’ to exit.)")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input in ("hi", "hello", "hey"):
            print("Bot: Hi there! How can I help you today?")
        
        elif user_input in ("how are you", "how are you?"):
            print("Bot: I'm doing well, thanks for asking! How about you?")
        
        elif "your name" in user_input:
            print("Bot: I’m a simple rule-based chatbot created in Python.")
        
        elif "weather" in user_input or "raining" in user_input:
            print("Bot: I’m not connected to real-time weather yet, but I hope it’s nice where you are!")
        
        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M")
            print(f"Bot: It’s currently {now}.")
        
        elif "date" in user_input or "today" in user_input:
            from datetime import date
            today = date.today().strftime("%B %d, %Y")
            print(f"Bot: Today’s date is {today}.")
        
        elif "tell me about" in user_input:
            topic = user_input.replace("tell me about", "").strip()
            if topic:
                print(f"Bot: Here’s a brief on {topic}. [You can add more details here]")
            else:
                print("Bot: About what exactly?")
        
        elif "joke" in user_input or "make me laugh" in user_input:
            print("Bot: Why did the computer go to the doctor? Because it had a virus! 😂")
            
        elif "nice jock" in user_input in user_input:
            print("Bot:thank you!")
        

        
        elif "sad" in user_input or "not feeling well" in user_input:
            print("Bot: I’m sorry to hear that. Want to talk about what’s making you feel this way?")
        
        elif user_input in ("thanks", "thank you", "thank you!"):
            print("Bot: You’re welcome! Anything else I can do for you?")
        
        elif user_input in ("bye", "exit", "quit"):
            print("Bot: Goodbye! Have a great day.")
            break
        
        else:
            print("Bot: I'm sorry, I didn’t understand that. Could you please rephrase?")
            
if __name__ == "__main__":
    chatbot()

