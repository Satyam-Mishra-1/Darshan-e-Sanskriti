from taskflowai import WebTools
from src.agentic.logger import logging
from src.agentic.exception import CustomException

class GetWeatherData:
    @classmethod
    def fetch_weather_data(cls, location: str):
        """
        Fetch weather data for a given location.
        """
        try:
            logging.info(f"Fetching weather data for location: {location}")
            weather_data = WebTools.get_weather_data(location)
            logging.info("Weather data fetched successfully.")
            return weather_data
        except Exception as e:
            logging.error("Failed to fetch weather data.")
            raise CustomException(e)
