from openai import OpenAI
import os

with open(f"perguntas/perguntas.txt", "r") as perguntas:
    text = perguntas.read()

pasta = "C:/Users/kawan/OneDrive/Documentos/programas/python/projeto/respostas"

client = OpenAI(
    api_key = "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"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "retorne respostas das perguntas"},
        {"role": "user", "content": f"{text}"}
    ]
)

gpt = completion.choices[0].message
gpt_text = gpt.content

with open ("respostas/respostas.txt", "w") as respostas:
    respostas.write(f"{gpt_text}")

