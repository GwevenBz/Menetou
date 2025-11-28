import google.generativeai as genai
import os

API_KEY = os.getenv("GOOGLE_API_KEY") or "AIzaSyC5HKLQIQq7k0nM-_fFbcs84j__qG1ot3I"
genai.configure(api_key=API_KEY)

print("Listing available models:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
