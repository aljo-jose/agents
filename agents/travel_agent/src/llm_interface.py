# llm_interface.py

from openai import OpenAI
import os
from dotenv import load_dotenv
from prompt_templates import itinerary_prompt
from agents.travel_agent.tools.weather import get_weather_forecast
from agents.travel_agent.tools.currency import convert_currency


# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_itinerary(destination, days, interests, memories, budget=None, from_currency="AED"):
    forecast = get_weather_forecast(destination)
    
    # Convert currency if budget is given
    if budget:
        try:
            # Simplified: convert AED to destination currency (mock logic)
            # You could later map destination to currency code properly
            dest_currency = "TRY" if "turkey" in destination.lower() else "USD"
            converted_budget = convert_currency(budget, from_currency, dest_currency)
            budget_info = f"{budget} {from_currency} ≈ {converted_budget} {dest_currency}"
        except Exception as e:
            budget_info = f"Budget given: {budget} {from_currency}. Currency conversion failed."
    else:
        budget_info = "No budget specified."

    prompt = itinerary_prompt(destination, days, interests, forecast, memories, budget_info)

    print(prompt)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful travel planner."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content

