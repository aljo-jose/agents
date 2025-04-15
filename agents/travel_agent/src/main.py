# main.py

from llm_interface import generate_itinerary
from agents.travel_agent.memory.store import search_memory, add_to_memory, initialize_memory

def main():
    destination = input("Where do you want to go? ")
    days = int(input("How many days is your trip? "))
    interests = input("What are your interests? (e.g. food, nature, museums): ")
    budget = input("What is your budget in AED? (e.g. 1000): ")

    # BEFORE generating prompt
    initialize_memory()
    memories = search_memory("travel preferences")
    print("\n🧠 Found past memories:", memories)

    result = generate_itinerary(destination, days, interests, memories, budget=budget, from_currency="AED")
    print("\nHere's your suggested itinerary:\n")
    print(result)

    # AFTER generating plan
    add_to_memory(f"Trip to {destination} for {days} days with interest in {interests}", "travel preferences")

if __name__ == "__main__":
    main()
