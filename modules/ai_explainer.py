from google import genai

client = genai.Client(api_key="AIzaSyDXyLE83lHTx4tTiLhqLJYevVLDN0QYzbc")

def explain_topic(topic, emotion):

    prompt = f"""
    Student emotion: {emotion}

    Explain the topic {topic} in simple terms with examples.
    """

    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=prompt
    )

    return response.text