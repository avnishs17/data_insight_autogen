from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor

from config.constants import WORK_DIR_DOCKER, TIMEOUT_DOCKER

def get_docker_code_executor(uploaded_files=None):
    
    docker = DockerCommandLineCodeExecutor(
        timeout=TIMEOUT_DOCKER,
        work_dir=WORK_DIR_DOCKER
    )

    return docker


async def start_docker_container(docker):

    print("Starting Docker container...")
    await docker.start()
    print("Docker container started.")


async def stop_docker_container(docker):
    
    print("Stopping Docker container...")
    await docker.stop()
    print("Docker container stopped.")