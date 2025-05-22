import os
import sys
import requests
from dotenv import load_dotenv
from src.agentic.logger import logging
from src.agentic.exception import CustomException
from taskflowai import WebTools

# Load environment variables
load_dotenv()
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

class SerperSearch:
    @classmethod
    def search_web(cls, query: str):
        try:
            logging.info(f"Performing web search for query: {query}")
            search_results = WebTools.serper_search(query=query)
            logging.info("Web search completed successfully.")
            return search_results
        except Exception as e:
            logging.error("Failed to perform web search.")
            raise CustomException(sys, e)

    @classmethod
    def search_images(cls, query: str, max_results=3):
        try:
            # Try Pexels first
            if PEXELS_API_KEY:
                logging.info(f"Searching Pexels images for: {query}")
                headers = {"Authorization": PEXELS_API_KEY}
                response = requests.get(
                    "https://api.pexels.com/v1/search",
                    params={"query": query, "per_page": max_results},
                    headers=headers,
                )
                if response.status_code == 200:
                    data = response.json()
                    urls = [{"url": photo["src"]["large"]} for photo in data.get("photos", [])]
                    if urls:
                        return urls
                logging.warning("No images found on Pexels or API limit reached.")

            # Fallback to Unsplash
            if UNSPLASH_ACCESS_KEY:
                logging.info(f"Falling back to Unsplash for: {query}")
                response = requests.get(
                    "https://api.unsplash.com/search/photos",
                    params={"query": query, "per_page": max_results},
                    headers={"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"},
                )
                if response.status_code == 200:
                    data = response.json()
                    return [{"url": photo["urls"]["regular"]} for photo in data.get("results", [])]
                logging.warning("No images found on Unsplash or API limit reached.")

            raise RuntimeError("No valid image results found.")
        except Exception as e:
            logging.error(f"Image search failed: {e}")
            raise CustomException(sys, e)
