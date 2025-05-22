import requests
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

class UnsplashImages:
    def __init__(self):
        self.access_key = os.getenv("UNSPLASH_ACCESS_KEY")
        if not self.access_key:
            raise ValueError("UNSPLASH_ACCESS_KEY not set in environment variables.")
        self.api_url = "https://api.unsplash.com/search/photos"

    def search_images(self, query, per_page=6):
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
            st.error(f"❌ Error fetching Unsplash images: {e}")
            return []

def display_images(query: str):
    unsplash = UnsplashImages()
    image_urls = unsplash.search_images(query)

    if image_urls:
        st.markdown(f"### Related Images for: {query}")
        # Display images in block (vertical) format with wider container width
        for url in image_urls:
            st.image(url, use_container_width=True)
            st.write("---")  # horizontal separator between images
    else:
        st.info("No images found.")
