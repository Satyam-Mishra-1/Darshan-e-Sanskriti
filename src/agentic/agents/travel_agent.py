import json
from taskflowai import Agent
from src.agentic.utils.main_utils import LoadModel
from src.agentic.logger import logging
from src.agentic.exception import CustomException
from src.agentic.tools.search_flights import SearchFlights
from src.agentic.tools.get_weather_data import GetWeatherData


class TravelAgent:

    @classmethod
    def run(cls, context: str, instruction: str) -> str:
        try:
            agent = cls.initialize_travel_agent()
            prompt = f"{context.strip()}\n\n{instruction.strip()}"
            print("DEBUG: Prompt being sent:\n", prompt)

            if agent.llm is None:
                raise CustomException("LLM function is not defined in agent.")

            response = agent.llm(prompt)
            print("DEBUG: Agent response:\n", response)

            return response if isinstance(response, str) else str(response)
        except Exception as e:
            raise CustomException(f"TravelAgent run error: {e}")

    @staticmethod
    def gemini_llm(prompt: str, *args, **kwargs) -> str:
        try:
            model = LoadModel.load_gemini_model()
            response = LoadModel.generate_content_with_rate_limit(model, prompt)
            return response.text
        except Exception as e:
            raise CustomException(f"Gemini LLM error: {e}")

    @classmethod
    def initialize_travel_agent(cls) -> Agent:
        try:
            logging.info("Initializing Travel Agent.")
            travel_agent = Agent(
                role="Travel Agent",
                goal="Assist travelers with their queries",
                attributes="friendly, hardworking, and detailed in reporting back to users",
                llm=cls.gemini_llm,
                tools={
                    SearchFlights.search_flights_tool,
                    GetWeatherData.fetch_weather_data,
                },
            )
            logging.info("Travel Agent initialized successfully.")
            return travel_agent
        except Exception as e:
            raise CustomException(f"Failed to initialize Travel Agent: {e}")

    @classmethod
    def research_attractions(cls, destination: str) -> list | str:
        instruction = (
            f"List the top 5 attractions to visit in {destination}. "
            f"Provide titles, brief descriptions, and URLs to images if available, formatted as a JSON list "
            f"where each item has 'title', 'description', and optional 'image' fields."
        )
        context = f"Destination: {destination}"
        response = cls.run(context, instruction)

        try:
            attractions = json.loads(response)
            return attractions
        except json.JSONDecodeError:
            print("WARNING: Could not parse attractions response as JSON. Returning raw text.")
            return response


    @classmethod
    def research_weather(cls, destination: str, dates: str):
        instruction = (
            f"Provide a detailed weather forecast for {destination} during {dates}. "
            f"Return the result as a JSON object with two keys:\n"
            f"1. 'forecast' → a list of daily weather entries with the following fields:\n"
            f"   - 'date' (string, format YYYY-MM-DD),\n"
            f"   - 'high' (integer, high temperature in °C),\n"
            f"   - 'low' (integer, low temperature in °C),\n"
            f"   - 'description' (string, summary of the day),\n"
            f"   - 'weather_type' (string, like 'Sunny', 'Rainy', 'Cloudy', 'Snowy', etc.) use this also along with string to represent (string, a weather emoji like ☀️, 🌧️, ☁️, 🌩️),\n"
            f"   - 'icon' (string, a weather emoji like ☀️, 🌧️, ☁️, 🌩️ or an image URL for visualization).\n"
            f"2. 'recommendations' → a string with clothing and travel tips based on the forecast.\n\n"
            f"Return only a valid JSON object in this exact structure."
        )
        context = f"Destination: {destination}\nDates: {dates}"
        response = cls.run(context, instruction)

        try:
            return json.loads(response)
        except json.JSONDecodeError:
            print("WARNING: Could not parse weather response as JSON. Returning raw text.")
            return response






    @classmethod
    def search_flights(cls, origin : str, destination: str, dates: str, budget: int):
        instruction = (
            f"Find top 5 affordable flights from {origin}  to {destination} for dates {dates} under a ₹{budget} budget. "
            f"Respond as a Text list with fields: 'airline', 'departure', 'arrival', 'price', 'duration'."
            f"You have to return the text format only no extra text or explanation."
        )
        context = f"Searching for budget flights to {destination} on {dates}."
        response = cls.run(context, instruction)

        try:
            return response
        except json.JSONDecodeError:
            print("WARNING: Could not parse flight response as JSON. Returning raw text.")
            return response

    @classmethod
    def summarize_trip(cls, destination: str, trip_type: str, budget: int, travel_dates):
        instruction = (
            f"Summarize a {trip_type.lower()} trip to {destination} with a budget of ₹{budget:,} during {travel_dates}. "
            f"Include highlights, travel tips, and key points."
        )
        context = f"Destination: {destination}\nTrip Type: {trip_type}\nBudget: ₹{budget}\nDates: {travel_dates}"
        response = cls.run(context, instruction)
        return response
