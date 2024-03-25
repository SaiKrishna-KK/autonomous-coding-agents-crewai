import os
from dotenv import load_dotenv
from crewai import Crew, Process, Task
from requirements_agent import requirements_agent, requirements_task
from development_agent import development_agent, development_task
from testing_agent import testing_agent, testing_task
from documentation_agent import documentation_agent, documentation_task

# Load API keys from .env file
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
serper_api_key = os.getenv('SERPER_API_KEY')

# Assuming the API keys are used in your agents or tools,
# here is where you would configure them with the keys.
# For example, if your CompilerTool uses the SERPER_API_KEY:
# compiler_tool_instance.configure_api_key(serper_api_key)

# Define the main function to run the SDLC simulation
def run_sdlc_simulation():
    # Initialize the Crew with the agents and their tasks
    sdlc_crew = Crew(
        agents=[requirements_agent, development_agent, testing_agent, documentation_agent],
        tasks=[requirements_task, development_task, testing_task, documentation_task],
        process=Process.sequential  # Sequential execution of tasks
    )

    # Kick off the SDLC process
    # The `inputs` dict can be populated with initial inputs required for the process
    result = sdlc_crew.kickoff(inputs={
        'initial_input': 'Write a code that could reverse the list of numbers with time complexity of O(n)'
    })

    print(result)

if __name__ == "__main__":
    run_sdlc_simulation()
