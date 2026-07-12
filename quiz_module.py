import google.generativeai as genai
import json
import re

# Configure Gemini
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_quiz(topic):
    prompt = f"""
Generate exactly 3 multiple-choice questions about "{topic}".

Return ONLY valid JSON.

Example:

[
  {{
    "question": "Which keyword is used to define a function in Python?",
    "options": [
      "class",
      "function",
      "def",
      "return"
    ],
    "answer": "def",
    "explanation": "The 'def' keyword is used to define a function."
  }}
]

Rules:
- Exactly 3 questions
- 4 options each
- One correct answer
- One short explanation
- Do NOT write markdown.
- Do NOT use ```json.
- Return only JSON.
"""

    try:
        response = model.generate_content(prompt)

        text = response.text.strip()

        # Remove markdown code blocks if Gemini adds them
        text = re.sub(r"```json", "", text)
        text = re.sub(r"```", "", text)

        quiz = json.loads(text)

        return quiz

    except Exception as e:
        print(e)
        return []