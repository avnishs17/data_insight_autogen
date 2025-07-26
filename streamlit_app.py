import streamlit as st
import asyncio
import os

from teams.data_analyzer import get_data_analyzer_team
from models.llm_client import get_llm_client
from config.docker_utils import get_docker_code_executor,start_docker_container,stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult


st.title('Analyser GPT- Digital Data Analyzer') 

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])


# streamlit's variable


if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'autogen_team_state' not in st.session_state:
    st.session_state.autogen_team_state = None
if('images_shown') not in st.session_state:
    st.session_state.images_shown=[]

task = st.chat_input("Enter your task here...")


async def run_analyser_gpt(docker,openai_model_client,task):
    try:
        await start_docker_container(docker)
        team = get_data_analyzer_team(docker,openai_model_client)

        if st.session_state.autogen_team_state is not None:
            await team.load_state(st.session_state.autogen_team_state)

        async for message in team.run_stream(task=task):
            # print(message)
            if isinstance(message,TextMessage):
                if message.source.startswith('user'):
                    with st.chat_message('user',avatar='👤'):
                        st.markdown(message.content)
                elif message.source.startswith('Data_Analyzer_agent'):
                    with st.chat_message('Data Analyzer',avatar='🤖'):
                        st.markdown(message.content)
                elif message.source.startswith('Python_Code_Executor'):
                    with st.chat_message('Data Analyzer',avatar='👨‍💻'):
                        st.markdown(message.content)
                st.session_state.messages.append(message.content)
                # st.markdown(f"{message.content}")
            elif isinstance(message,TaskResult):
                st.markdown(f'Stop Reason :{message.stop_reason}')

                st.session_state.messages.append(message.stop_reason)

        st.session_state.autogen_team_state = await team.save_state()
            
        return None
    except Exception as e:
        st.error(f"Error: {e}")
        return e
    finally:   
        await stop_docker_container(docker)


if st.session_state.messages:
    for msg in st.session_state.messages:
        st.markdown(msg)

if task:
   if uploaded_file is not None: 
        
        if not os.path.exists('temp'):
            os.makedirs('temp', exist_ok=True)
   
        with open('temp/data.csv','wb') as f:
            f.write(uploaded_file.getbuffer())

        openai_model_client= get_llm_client()
        docker = get_docker_code_executor()

        error = asyncio.run(run_analyser_gpt(docker,openai_model_client,task))

        if error:
            st.error(f'An error occured: {error}')

        # # see all the *.png in temp and show them on streamlit app
        # png_files = [f for f in os.listdir('temp') if f.endswith('.png')]
        # if png_files:
        #     for png_file in png_files:
        #         st.image(os.path.join('temp', png_file), caption=png_file)
        
        if os.path.exists('temp/output.png'):
            # if('output.png' not in st.session_state.images_shown):
            #     st.session_state.images_shown.append('output.png')
            # if 'output.png' not in st.session_state.images_shown:
            st.image('temp/output.png')
   
   else:
       st.warning('Please upload the file and provide the task')

else:
    st.warning('Please provide the task')