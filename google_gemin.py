

import google.generativeai as genai

# Replace with your actual API key
GOOGLE_API_KEY = "AIzaSyDTuP9mQuLaEUE7Y3A76ig-k4Ta-wTStWg"

genai.configure(api_key=GOOGLE_API_KEY)

# Choose model - 'gemini-1.5-flash' or 'gemini-1.5-pro'
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

chat = model.start_chat(history=[])

print("Welcome to your Gemini chatbot! Type 'exit' to end.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    try:
        response = chat.send_message(user_input)
        print("Gemini:", response.text)

    except Exception as e:
        print("API called failed. The error is , ",e)