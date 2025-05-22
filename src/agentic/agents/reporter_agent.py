
from taskflowai import Agent
from src.agentic.utils.main_utils import LoadModel
from src.agentic.logger import logging
from src.agentic.exception import CustomException
import sys

class TravelReportAgent:
    @staticmethod
    def gemini_llm(prompt):
        model = LoadModel.load_gemini_model()
        # Adjust the following line to match your model's API
        # response = model.generate_content(prompt)
        response = LoadModel.generate_content_with_rate_limit(model, prompt)
        return response.text  # or response['choices'][0]['text'] or similar
    
    @classmethod
    def initialize_travel_report_agent(cls):
        try:
            logging.info("Initializing the Travel Report Agent.")

            travel_report_agent = Agent(
                role="Travel Report Agent",
                goal="Write comprehensive travel reports with visual elements",
                attributes="friendly, hardworking, visual-oriented, and detailed in reporting",
                llm=cls.gemini_llm
            )

            logging.info("Travel Report Agent initialized successfully.")
            return travel_report_agent

        except Exception as e:
            raise CustomException(e)
