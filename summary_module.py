import google.generativeai as genai

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def summarize_text(text):
    prompt = f"""
    Summarize the following text in simple and concise points:

    {text}
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"