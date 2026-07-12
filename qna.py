import google.generativeai as genai

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_question(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Error: {e}"