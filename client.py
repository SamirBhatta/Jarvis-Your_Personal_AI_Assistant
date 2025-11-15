import google.generativeai as genai

genai.configure(api_key="Your_Api_Key")

model = genai.GenerativeModel("gemini-2.0-flash")

chat = model.start_chat()

response = chat.send_message("What is coding?")
print(response.text)
