import google.generativeai as genai

genai.configure(api_key="API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

def get_learning_path(topic):

    prompt = f"""
Create a learning roadmap for {topic}.

Include:

1. Beginner
2. Intermediate
3. Advanced

For every level provide:
- Topics
- Practice ideas
- Resources

Keep it simple and beginner friendly.
"""

    response = model.generate_content(prompt)
    return response.text
