from google import genai

# Initialize Gemini client
client = genai.Client(api_key="AIzaSyCDlrBfOc2KvnA8hzSXYDRhq_6b2Rpa22c")


def generate_quiz(topic, difficulty):
    """
    Generate quiz questions using Gemini AI
    """

    prompt = f"""
Generate 10 {difficulty} level multiple choice questions about {topic}.

Format strictly like this:

Question: ...
A) ...
B) ...
C) ...
D) ...
Answer: A/B/C/D
"""

    try:
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"ERROR: {str(e)}"