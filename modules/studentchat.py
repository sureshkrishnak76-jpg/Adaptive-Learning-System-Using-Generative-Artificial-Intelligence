import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyDXyLE83lHTx4tTiLhqLJYevVLDN0QYzbc")

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_explanation(topic, emotion):

    prompt = f"""
    A student is feeling {emotion}.
    Explain the concept of {topic} in a simple and motivating way.
    Use easy examples.
    """

    response = model.generate_content(prompt)

    return response.text