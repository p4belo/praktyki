import tkinter as tk
import os
from tkinter import scrolledtext
import requests
import json

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.environ.get("klucz_api", "")
MODEL = "x-ai/grok-4.1-fast:free"

def send_message_to_api(user_text):
    
    response = requests.post(
        url=API_URL,
        headers={
            "Authorization": "Bearer " + API_KEY,
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": MODEL,
            "messages": [{"role": "user", "content": user_text}],
            "extra_body": {"reasoning": {"enabled": True}}
        })
    )
    data = response.json()
    msg = data['choices'][0]['message']

    messages = [
        {"role": "user", "content": user_text},
        {
            "role": "assistant",
            "content": msg.get('content'),
            "reasoning_details": msg.get('reasoning_details')
        }
    ]

    response2 = requests.post(
        url=API_URL,
        headers={
            "Authorization": "Bearer " + API_KEY,
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": MODEL,
            "messages": messages + [{"role": "user", "content": "Jesteś tego pewny? Pomyśl dokładnie jeszcze raz."}],
            "extra_body": {"reasoning": {"enabled": True}}
        })
    )

    data2 = response2.json()
    final_msg = data2['choices'][0]['message']['content']

    return final_msg


root = tk.Tk()
root.title("Chat API")
root.geometry("600x600")
root.resizable(True, True)

chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Arial", 12))
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

input_box = tk.Entry(root, font=("Arial", 14))
input_box.pack(padx=10, pady=10, fill=tk.X)


def send_message():
    user_text = input_box.get().strip()
    if not user_text:
        return

    chat_box.configure(state='normal')
    chat_box.insert(tk.END, f"You: {user_text}\n")
    chat_box.configure(state='disabled')
    chat_box.see(tk.END)
    input_box.delete(0, tk.END)

    try:
        bot_response = send_message_to_api(user_text)
    except Exception as e:
        bot_response = "Error: " + str(e)

    chat_box.configure(state='normal') 
    chat_box.insert(tk.END, f"Bot: {bot_response}\n\n") 
    chat_box.configure(state='disabled') 
    chat_box.see(tk.END)


def enter(event):
    send_message()

root.bind("<Return>", enter)
send_button = tk.Button(root, text="Wyślij", command=send_message, font=("Arial", 12))
send_button.pack(pady=5)

root.mainloop()
