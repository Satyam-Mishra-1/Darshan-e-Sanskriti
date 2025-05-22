
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class UnsplashImages:
    @classmethod
    def search_images(cls, query: str, per_page=4):
        access_key = os.getenv("UNSPLASH_ACCESS_KEY")
        if not access_key:
            raise ValueError("❌ UNSPLASH_ACCESS_KEY not set in environment variables.")

        url = "https://api.unsplash.com/search/photos"
        params = {
            "query": query,
            "per_page": per_page,
            "client_id": access_key
        }

        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json().get("results", [])
            return [item["urls"]["regular"] for item in data]
        except Exception as e:
            print(f"❌ Error fetching Unsplash images: {e}")
            return []
