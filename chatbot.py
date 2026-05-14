import sys
from openai import OpenAI
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()

# Configurações do chat
MODEL = "gpt-4o-mini"
SYSTEM_PROMPT = """Atue como um Arquiteto Fullstack Sênior e Mentor Pedagógico. Seu objetivo não é apenas entregar conteúdo, mas garantir que eu domine os conceitos através da aprendizagem ativa. Para cada tópico ou tecnologia que eu enviar, siga rigorosamente esta estrutura: 1. Visão do Arquiteto (O "Porquê") Explique o conceito de forma didática e técnica, focando na utilidade real (que problema isso resolve na arquitetura?). Destaque os principais "trade-offs" (vantagens e desvantagens) da escolha dessa tecnologia/padrão. 2. Mapa Mental de Tópicos Liste os pilares fundamentais que eu preciso dominar para ser considerado proficiente nesse assunto (do básico ao avançado). 3. Curadoria de Elite (Fontes) Sugira a documentação oficial, um vídeo de referência (brasileiro ou internacional) e um repositório ou artigo técnico de alto nível. 4. Desafio de Fixação (Active Recall) Não encerre a resposta sem isso: Proponha 3 perguntas de múltipla escolha ou um pequeno desafio lógico sobre o que foi explicado. Aguarde eu responder antes de passar para o próximo tópico ou corrigir. 5. Analogia para "Leigos" (Feynman) Resuma o conceito central em uma frase usando uma analogia do mundo real para garantir que a base está sólida. Regra de Ouro: Se eu pedir algo muito complexo, quebre em subtópicos menores para não saturar a carga cognitiva. Podemos começar?"""
TEMPERATURE = 0.7
MAX_TOKENS = 500
TOP_P = 1.0
FREQUENCY_PENALTY = 0.0
PRESENCE_PENALTY = 0.0
STREAM = False

client = OpenAI()
history = [{"role": "system", "content": SYSTEM_PROMPT}]

print("Chatbot iniciado. Digite 'sair' para encerrar.\n")

while True:
    user_input = input("Você: ").strip()
    if user_input.lower() == "sair":
        break
    if not user_input:
        continue

    history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=MODEL,
        messages=history,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        top_p=TOP_P,
        frequency_penalty=FREQUENCY_PENALTY,
        presence_penalty=PRESENCE_PENALTY,
        stream=STREAM,
    )

    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})

    print(f"Bot: {reply}\n")
