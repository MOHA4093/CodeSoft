def simple_chatbot(user_input):
    user_input = user_input.lower()
    
    greetings = ['hello', 'hi', 'hey', 'howdy']
    inquiries = ['how are you', 'what is your name', 'who are you']
    if any(word in user_input for word in greetings):
        return "Hello! How can I help you today?"

    elif any(word in user_input for word in inquiries):
        return "I am a simple chatbot. My purpose is to assist you."

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)