from crewai import Agent, Task
# Assuming CompilerTool is defined to interact with the Docker sandbox
from compiler_tool import CompilerTool

class DevelopmentAgent(Agent):
    def __init__(self, tools, memory=True, verbose=True):
        super().__init__(role='Software Developer',
                         goal='Write and compile code to meet the project requirements.',
                         tools=tools,
                         memory=memory,
                         verbose=verbose,
                         backstory="Expert in Python, tasked with turning requirements into a functioning software solution.")

    def develop_code(self, requirements):
        # Simulate code generation based on requirements
        code = """
def greet():
    print("Hello, World! Following the requirements closely.")

greet()
"""
        return code

    def compile_code(self, code):
        # Simulate using the CompilerTool to compile code
        # In reality, this function would interact with the Docker sandbox
        # The CompilerTool's _run method should handle those details
        compiler_tool = self.tools[0]  # Assuming the first tool is CompilerTool
        compile_result = compiler_tool.run(code)
        return compile_result

# Assuming an instance of CompilerTool is already created
compiler_tool_instance = CompilerTool()

# Instantiate the DevelopmentAgent with the CompilerTool
development_agent = DevelopmentAgent(tools=[compiler_tool_instance])

# Define a task for code development and compilation
development_task = Task(
    description="Develop and compile the software based on requirements.",
    expected_output="Compiled code without errors, ready for the next development stage.",
    function=development_agent.compile_code,  # Here we pass the code compilation method
    agent=development_agent,
    inputs={"code": development_agent.develop_code(None)}  # Normally, requirements would be passed here
)
