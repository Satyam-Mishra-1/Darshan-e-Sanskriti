
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class UnsplashImages:
    def __init__(self):
        self.access_key = os.getenv("UNSPLASH_ACCESS_KEY")
        if not self.access_key:
            raise ValueError("UNSPLASH_ACCESS_KEY not set in environment variables.")
        self.api_url = "https://api.unsplash.com/search/photos"

    def search_images(self, query, per_page=4):
        params = {
            "query": query,
            "per_page": per_page,
            "client_id": self.access_key,
        }
        try:
            response = requests.get(self.api_url, params=params, timeout=5)
            response.raise_for_status()
            results = response.json().get("results", [])
            return [item["urls"]["regular"] for item in results]
        except Exception as e:
            print(f"❌ Error fetching Unsplash images: {e}")
            return []





class WikiImages:
    def search_images(self, query, limit=3):
        # Return empty list or dummy images
        return []
