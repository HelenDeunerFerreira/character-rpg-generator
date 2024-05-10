import google.generativeai as genai

GOOGLE_API_KEY='cole aqui sua chave'
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "candidate_count": 1,
    "temperature": 0.5
}

safety_settings = {
    "HARASSMENT": "BLOCK_ONLY_HIGH",
    "HATE": "BLOCK_ONLY_HIGH",
    "SEXUAL": "BLOCK_ONLY_HIGH",
    "DANGEROUS": "BLOCK_ONLY_HIGH",
}

model = genai.GenerativeModel(model_name='gemini-pro', generation_config=generation_config, safety_settings=safety_settings)

chat = model.start_chat(history=[])

sistema = input('Bem-vindo, aventureiro! Você está precisando de um personagem/NPC de qual sistema de RPG? (Digite FIM para encerrar): ')

while sistema != "FIM" and sistema != "fim" and sistema != "Fim":
  detalhe = input('Tem algum detalhe da história ou aparência desse personagem que seria importante? ')
  response = chat.send_message(f"Escreva uma história de origem e uma ficha de RPG para um personagem fictício considerando o sistema de RPG {sistema} e considerando que {detalhe}")
  print(response.text)
  sistema = input('Bem-vindo, aventureiro! Você está precisando de um personagem/NPC de qual sistema de RPG? (Digite FIM para encerrar): ')

