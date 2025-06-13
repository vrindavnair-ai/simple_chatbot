import gradio as gr
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat()

def chat_fn(message, history):
    response = chat.send_message(message)
    return response.text

try :
    iface = gr.ChatInterface(chat_fn)
    iface.launch(share=True)

except Exception as e:
    print("Error is ",e)
