from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor

def getDockerCommandLineExecutor():
    docker = DockerCommandLineCodeExecutor(
        work_dir='temp',  # Just this
        timeout=120,
        image='python-data-tools:latest'
    )
    return docker


async def start_docker_container(docker):
    print("Starting Docker Container")
    await docker.start()
    print("Docker Container Started")


async def stop_docker_container(docker):
    print("Stop Docker Container")
    await docker.stop()
    print("Docker Container Stopped")
