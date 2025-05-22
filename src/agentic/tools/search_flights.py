from taskflowai import AmadeusTools
from src.agentic.logger import logging
from src.agentic.exception import CustomException
import sys

class SearchFlights:
    @classmethod
    def search_flights_tool(cls, origin: str, destination: str, departure_date: str):
        """
        Search for flights using the AmadeusTools.
        """
        try:
            logging.info(f"Searching flights from {origin} to {destination} on {departure_date}.")
            results = AmadeusTools.search_flights(
                origin=origin,
                destination=destination,
                departure_date=departure_date
            )
            logging.info("Flight search completed successfully.")
            return results
        except Exception as e:
            logging.error("Failed to search flights.")
            raise CustomException(sys, e)
