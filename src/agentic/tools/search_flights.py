# from taskflowai import AmadeusTools
# from src.agentic.logger import logging
# from src.agentic.exception import CustomException
# import sys

# class SearchFlights:
#     @classmethod
#     def search_flights_tool(cls):
#         try:
#             logging.info("Initiating flight search using AmadeusTools.")
#             search_flights = AmadeusTools.search_flights
#             logging.info("Flight search initiated successfully.")
#             return search_flights
#         except Exception as e:
#             logging.info("Failed to initiate flight search.")
#             raise CustomException(sys, e)




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
            raise CustomException(e)
