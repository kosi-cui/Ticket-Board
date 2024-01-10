from src.model import *

class MainModel:
    def __init__(self):
        self.config = config.Config()
        self.api_agent = api_agent.APIAgent()