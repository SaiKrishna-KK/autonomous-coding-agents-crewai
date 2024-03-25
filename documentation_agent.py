import os
import re
from crewai import Agent, Task

class DocumentationAgent(Agent):
    def __init__(self, name="DocumentationAgent", tools=[], memory=True, verbose=True):
        super().__init__(role='Documentation Specialist',
                         goal='Automatically generate documentation from code.',
                         name=name, tools=tools, memory=memory, verbose=verbose,
                         backstory="Expert in creating accessible documentation for developers.")

    def parse_docstrings_and_comments(self, code):
        """
        Extracts docstrings and marked comments from the code.
        Assumes docstrings are triple-quoted strings at the start of a module, class, or def.
        """
        docstrings = re.findall(r'""".*?"""', code, re.DOTALL)
        comments = re.findall(r'# DOC:.*', code)
        
        documentation_items = docstrings + comments
        documentation_content = "\n".join(documentation_items)
        
        # Process for Markdown
        documentation_md = documentation_content.replace('"""', '').replace('# DOC:', '').strip()
        documentation_md = re.sub(r'\n+', '\n', documentation_md)  # Remove extra newlines
        return documentation_md

    def generate_documentation(self, code, output_file="README.md"):
        documentation_md = self.parse_docstrings_and_comments(code)
        
        if not documentation_md:
            documentation_md = "No documentation found in the code."
        
        # Write to README.md file
        with open(output_file, 'w') as md_file:
            md_file.write(documentation_md)
        
        return f"Documentation generated and written to {output_file}"

# Instantiate the DocumentationAgent
documentation_agent = DocumentationAgent()

# Define a task for generating documentation - in a real scenario, replace the placeholder code input with actual code
documentation_task = Task(
    description="Generate documentation based on code comments and docstrings.",
    expected_output="A README.md file containing the compiled documentation.",
    function=documentation_agent.generate_documentation,  # Linking the agent's function
    agent=documentation_agent,
    inputs={"code": """\"\"\"Example Module
This module demonstrates documentation as specified by the `DocumentationAgent`.
\"\"\"
# DOC: This is an example of a marked comment for documentation.
def example_function():
    \"\"\"Example Function
    This is a docstring example for a function.
    \"\"\"
    pass
"""}
)
