from google import genai

client = genai.Client(api_key="AIzaSyCekuUUJeuCGVHs77phoGY_IXSjWUYOZOc")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain stack in data structures simply"
)

print(response.text)