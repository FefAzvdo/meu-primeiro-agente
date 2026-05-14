import sys
import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from config import MODEL, SYSTEM_PROMPT, TEMPERATURE, MAX_TOKENS, TOP_P, FREQUENCY_PENALTY, PRESENCE_PENALTY, STREAM, HISTORY_FILE

sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()


def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return [{"role": "system", "content": SYSTEM_PROMPT}]


def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


client = OpenAI()
history = load_history()

print("Chatbot iniciado. Digite 'sair' para encerrar.\n")

while True:
    user_input = input("Você: ").strip()
    if user_input.lower() == "sair":
        break
    if not user_input:
        continue

    history.append({"role": "user", "content": user_input})

    print("Bot: ", end="", flush=True)

    stream = client.chat.completions.create(
        model=MODEL,
        messages=history,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        top_p=TOP_P,
        frequency_penalty=FREQUENCY_PENALTY,
        presence_penalty=PRESENCE_PENALTY,
        stream=STREAM,
    )

    reply = ""
    for chunk in stream:
        token = chunk.choices[0].delta.content or ""
        print(token, end="", flush=True)
        reply += token

    print("\n")
    history.append({"role": "assistant", "content": reply})
    save_history(history)
