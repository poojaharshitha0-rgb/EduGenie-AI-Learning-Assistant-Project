import google.generativeai as genai

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def explain_concept(topic):
    prompt = f"""
    Explain the following topic in very simple words for a beginner.

    Topic:
    {topic}
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"