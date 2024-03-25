import subprocess
from crewai_tools import BaseTool

class CompilerTool(BaseTool):
    name: str = "Python Compiler Tool"
    description: str = "Compiles and executes Python code in a Docker-based sandbox environment."

    def __init__(self):
        # Initialize with any required configurations
        self.docker_image = "python:3.9-slim"  # Example Python Docker image
        self.container_name = "python_sandbox_container"

    def setup_container(self):
        # Setup Docker container for compilation, if not already running
        try:
            subprocess.run(["docker", "run", "--name", self.container_name, "-d", self.docker_image, "tail", "-f", "/dev/null"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Container setup failed: {e}")

    def compile_and_execute(self, code):
        # Function to compile and execute the given code within the Docker sandbox
        try:
            # Writing code to a temporary file
            with open("/tmp/temp_code.py", "w") as code_file:
                code_file.write(code)
            
            # Copying code file to Docker container
            subprocess.run(["docker", "cp", "/tmp/temp_code.py", f"{self.container_name}:/tmp/temp_code.py"], check=True)

            # Executing code inside Docker container
            result = subprocess.run(["docker", "exec", self.container_name, "python", "/tmp/temp_code.py"], capture_output=True, text=True, check=True)

            return result.stdout
        except subprocess.CalledProcessError as e:
            # Handling compilation or execution errors
            return f"Compilation or Execution Error: {e.stderr}"

    def _run(self, code):
        # Ensure the Docker container is ready
        self.setup_container()

        # Compile and execute the code, returning the output
        return self.compile_and_execute(code)
