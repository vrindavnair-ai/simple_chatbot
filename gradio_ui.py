import gradio as gr
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

# 🔐 Load your Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 🧠 Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# 💬 Define chatbot logic
def chat_with_gemini(message, history):
    history = history or []
    full_prompt = ""
    for user, bot in history:
        full_prompt += f"User: {user}\nAI: {bot}\n"
    full_prompt += f"User: {message}\nAI:"

    try:
        response = model.generate_content(full_prompt)
        reply = response.text.strip()
        history.append((message, reply))
    except Exception as e:
        history.append((message, "Error", e))
    
    return "", history

# 🎨 Build Gradio UI
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 🤖 Gemini AI Chatbot\nAsk me anything!")

    chatbot = gr.Chatbot(height=400)
    msg = gr.Textbox(placeholder="Type your message...", label="")

    clear_btn = gr.Button("Clear Chat")

    msg.submit(chat_with_gemini, [msg, chatbot], [msg, chatbot])
    clear_btn.click(lambda: None, None, chatbot, queue=False)

demo.launch()
