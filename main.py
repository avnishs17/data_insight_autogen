import asyncio
from teams.data_analyzer import get_data_analyzer_team
from models.llm_client import get_llm_client
from config.docker_utils import get_docker_code_executor,start_docker_container,stop_docker_container
from autogen_agentchat.messages import TextMessage


async def main():

    openai_model_client = get_llm_client()
    docker = get_docker_code_executor()

    team = get_data_analyzer_team(docker, openai_model_client)

    try:
        task = 'Can you give me a graph of types of flowers in my data iris.csv'

        await start_docker_container(docker)

        async for message in team.run_stream(task=task):
            print(message)

    except Exception as e:
        print(e)
    finally:
        await stop_docker_container(docker)


if(__name__=='__main__'):
    asyncio.run(main())
