import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("API key not found. Make sure you have a .env file with GOOGLE_API_KEY set.")

genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

def chat_with_gemini(prompt):
    try:
        chat_session = model.start_chat()
        response = chat_session.send_message(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Sorry, I couldn't get a response from Gemini."

if __name__ == "__main__":
    print("Gemini Chatbot is ready!")
    print("Type 'bye' to end.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye']:
            print("Chatbot: Sayonara!")
            break

        response = chat_with_gemini(user_input)
        print(f"Chatbot: {response}")
