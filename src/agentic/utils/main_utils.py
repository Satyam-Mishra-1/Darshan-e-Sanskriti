import os
import time
import threading
import google.generativeai as genai
from dotenv import load_dotenv
from src.agentic.logger import logging
from src.agentic.exception import CustomException

# Load environment variables
load_dotenv()

# Validate required API keys
required_keys = ["GEMINI_API_KEY"]
missing_keys = [key for key in required_keys if not os.getenv(key)]
if missing_keys:
    raise CustomException("Missing required environment variables: " + ', '.join(missing_keys))

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class RateLimiter:
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.lock = threading.Lock()
        self.calls = []

    def acquire(self):
        with self.lock:
            now = time.time()
            # Remove calls older than the period
            self.calls = [t for t in self.calls if now - t < self.period]
            if len(self.calls) >= self.max_calls:
                sleep_time = self.period - (now - self.calls[0])
                if sleep_time > 0:
                    time.sleep(sleep_time)
                now = time.time()
                self.calls = [t for t in self.calls if now - t < self.period]
            self.calls.append(time.time())

# Instantiate a rate limiter for 15 requests per 60 seconds
gemini_rate_limiter = RateLimiter(max_calls=15, period=60)


class LoadModel:
    @classmethod
    def load_gemini_model(cls):
        try:
            logging.info("Loading Gemini model.")
            model = genai.GenerativeModel('models/gemini-2.0-flash',
                    system_instruction=( 
                    "You are a markdown content generator. You create structured, clean, informative documents "
                    "with image markdown. Do not reply with questions. Always produce a full report."
           )                      
                                          )  # or your available model
            logging.info("Gemini model loaded successfully.")
            return model
        except Exception as e:
            logging.error("Failed to load Gemini model.")
            raise CustomException(e)

    @staticmethod
    def generate_content_with_rate_limit(model, prompt, *args, **kwargs):
        gemini_rate_limiter.acquire()
        return model.generate_content(prompt, *args, **kwargs)