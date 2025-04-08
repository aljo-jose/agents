import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Use the OpenAI client compatible with version 0.28.0
def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

def fun_fact_agent():
    return ask_gpt("Give me a fun science fact suitable for an 8-year-old.")

def quiz_agent():
    return ask_gpt("Create a multiple-choice quiz question for an 8-year-old. Include options and say the correct answer.")

def creative_challenge_agent():
    return ask_gpt("Suggest a short creative challenge for an 8-year-old. Something fun that uses imagination.")

if __name__ == "__main__":
    print("🌞 Welcome to your Daily Learning Buddy!")
    print("\n📚 Fun Fact:")
    print(fun_fact_agent())

    print("\n❓ Quiz of the Day:")
    print(quiz_agent())

    print("\n🎨 Creative Challenge:")
    print(creative_challenge_agent())
