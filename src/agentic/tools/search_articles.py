from taskflowai import WikipediaTools
from src.agentic.logger import logging
from src.agentic.exception import CustomException
import sys

class WikiArticles:
    @classmethod
    def fetch_articles(cls, query: str):
        """
        Fetch articles from Wikipedia based on the query.
        """
        try:
            logging.info(f"Fetching Wikipedia articles for query: {query}")
            articles = WikipediaTools.search_articles(query)
            logging.info("Articles fetched successfully.")
            return articles
        except Exception as e:
            logging.error("Failed to fetch articles from Wikipedia.")
            raise CustomException(sys, e)
