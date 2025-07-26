from autogen_agentchat.agents import AssistantAgent
from .data_analyzer_message import DATA_ANALYZER_SYS_PROMPT

def get_data_analyzer_agent(model_client):

    data_analyser_agent = AssistantAgent(
        name = 'data_analyzer_agent',
        model_client=model_client,
        description='An agent that analyzes data and writes Python code to answer user questions about CSV files.',
        system_message=DATA_ANALYZER_SYS_PROMPT,
    )

    return data_analyser_agent