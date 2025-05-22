

from taskflowai import Agent, WebTools, WikipediaTools
from src.agentic.utils.main_utils import LoadModel
from src.agentic.logger import logging
from src.agentic.exception import CustomException
from src.agentic.tools.serper_search import SerperSearch
from src.agentic.tools.search_articles import WikiArticles
from src.agentic.agents.search_images import WikiImages


class WebResearchAgent:
    @classmethod
    def run(cls, context, instruction):
        try:
            prompt = f"{context}\n\n{instruction}"
            logging.info("Running Gemini LLM directly (agent is not callable).")
            return cls.gemini_llm(prompt)

        except Exception as e:
            raise CustomException(f"Error running WebResearchAgent: {e}")

    @staticmethod
    def gemini_llm(prompt, *args, **kwargs):
        try:
            model = LoadModel.load_gemini_model()
            response = LoadModel.generate_content_with_rate_limit(model, prompt)
            return response.text
        except Exception as e:
            raise CustomException(f"Gemini LLM error: {e}")

    @classmethod
    def initialize_web_research_agent(cls):
        try:
            logging.info("Initializing Web Research Agent.")

            # Validate tools
            tools = [
                SerperSearch.search_web,
                WikiArticles.fetch_articles,
                WikiImages.search_images,
            ]

            web_research_agent = Agent(
                role="Web Research Agent",
                goal="Research destinations and find relevant images",
                attributes="diligent, thorough, comprehensive, visual-focused",
                llm=cls.gemini_llm,
                tools=tools,
            )

            logging.info("Web Research Agent initialized successfully.")
            return web_research_agent

        except Exception as e:
            raise CustomException(f"Error initializing WebResearchAgent: {e}")
