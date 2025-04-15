# prompt_templates.py

def itinerary_prompt(destination, days, interests, forecast, memories, budget_info):
    weather_summary = "\n".join(
        [f"{date}: {info['weather']} (~{info['avg_temp']:.1f}°C)" for date, info in forecast.items()]
    )

    memory_note = "\n".join(memories) if memories else "No memory available."

    return f"""
    I'm planning a {days}-day trip to {destination}.
    My interests are: {interests}.
    Budget: {budget_info}
    Past travel memory: {memory_note}

    The weather forecast is:
    {weather_summary}

    Based on the weather, preferences, and budget, create a day-wise itinerary with specific suggestions. For bad weather, suggest indoor activities. Be mindful of the budget when suggesting hotels, activities, or restaurants.
    """


