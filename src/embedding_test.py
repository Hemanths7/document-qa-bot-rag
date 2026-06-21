import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

result = genai.embed_content(
    model="models/text-embedding-004",
    content="Artificial Intelligence is transforming the world."
)

print("Embedding Length:", len(result["embedding"]))