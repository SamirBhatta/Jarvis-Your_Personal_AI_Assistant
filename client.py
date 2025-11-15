import google.generativeai as genai

genai.configure(api_key="AIzaSyDx14O4cF8crg5yQFaWHAwqREQ2Yq21aT0")

model = genai.GenerativeModel("gemini-2.0-flash")

chat = model.start_chat()

response = chat.send_message("What is coding?")
print(response.text)
