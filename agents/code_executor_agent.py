from autogen_agentchat.agents import CodeExecutorAgent

def get_code_executor_agent(code_executor):
    """    
    Returns a CodeExecutorAgent instance configured with 
    the provided code executor.
    """
    code_executor_agent = CodeExecutorAgent(
        name='python_code_executor',
        code_executor=code_executor
    )

    return code_executor_agent