from crewai import Agent, Task

class RequirementsAgent(Agent):
    def __init__(self, name="RequirementsAgent", tools=[], memory=True, verbose=True):
        super().__init__(role='Requirements Gatherer',
                         goal='Identify and outline the project requirements.',
                         name=name, tools=tools, memory=memory, verbose=verbose,
                         backstory="This agent is responsible for gathering all necessary requirements for the project to ensure a successful development process.")

    def define_requirements(self):
        # Simulating the action of gathering requirements
        project_requirements = {
            "title": "CrewAI Project Development",
            "description": "Develop a CrewAI project that simulates a software development lifecycle with multiple agents.",
            "functional_requirements": [
                "System must allow defining different roles for agents.",
                "System must compile and run code in a sandboxed environment.",
                "System must automatically test the compiled code.",
                "System must generate documentation based on the code."
            ],
            "non_functional_requirements": [
                "System should be easy to extend with additional agents.",
                "System should ensure the security of the compilation and execution environment."
            ]
        }
        return project_requirements

# Initialize the agent
requirements_agent = RequirementsAgent()

# Define a task for the agent
requirements_task = Task(
    description="Gather all necessary project requirements.",
    expected_output="A detailed list of project requirements.",
    function=requirements_agent.define_requirements,  # Linking the agent's function
    agent=requirements_agent,
)
