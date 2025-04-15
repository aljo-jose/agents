# agent_travel_planner.py

from langchain import hub
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain_openai import ChatOpenAI

from agents.travel_agent.tools.currency import convert_currency
from agents.travel_agent.tools.weather import get_weather_forecast
from langchain.prompts import PromptTemplate


# Tool: Get weather forecast
def format_weather(city: str) -> str:
    forecast = get_weather_forecast(city)
    return "\n".join([
        f"{date}: {info['weather']}, {info['avg_temp']:.1f}°C"
        for date, info in forecast.items()
    ])


# Tool: Currency conversion wrapper
def currency_tool(input_text: str) -> str:
    try:
        amount, from_currency, _, to_currency = input_text.split()
        converted = convert_currency(float(amount), from_currency.upper(), to_currency.upper())
        return f"{amount} {from_currency} ≈ {converted} {to_currency}"
    except Exception as e:
        return f"Conversion error: {str(e)}"


# Define tools
def define_tools():
    return [
        Tool(
            name="Weather Info",
            func=format_weather,
            description="Use this tool to get a 5-day weather forecast for a city. Input should be a city name."
        ),
        Tool(
            name="Currency Converter",
            func=currency_tool,
            description="Use this to convert currency in the format: '2500 AED to EUR'"
        )
    ]


# Set up the agent executor
def setup_agent_executor():
    tools = define_tools()
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    # Load the default ReAct prompt from LangChain Hub
    prompt = hub.pull("hwchase17/react")

    # Create the agent
    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True)




# Run agent in CLI
def run_cli(agent_executor):
    print("\n🔗 Ask your travel planning agent (type 'exit' to stop):")
    while True:
        user_input = input("🧳 > ")
        if user_input.strip().lower() in {"exit", "quit"}:
            break
        print("\n🧠 Agent response:\n")
        result = agent_executor.invoke({"input": user_input})
        print(result["output"])


# MAIN function
def main():
    agent_executor = setup_agent_executor()
    run_cli(agent_executor)


if __name__ == "__main__":
    main()
