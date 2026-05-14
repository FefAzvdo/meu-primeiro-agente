import sys
from openai import OpenAI
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()

client = OpenAI()
history = []

print("Chatbot iniciado. Digite 'sair' para encerrar.\n")

while True:
    user_input = input("Você: ").strip()
    if user_input.lower() == "sair":
        break
    if not user_input:
        continue

    history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=history,
    )

    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})

    print(f"Bot: {reply}\n")
