import json
from pathlib import Path
from llm_interface import LLMInterface
from openai_llm import OpenAIModel
# from anthropic_llm import AnthropicModel  # Uncomment if integrating Anthropic
from llm_manager import LLMManager
from file_system_manager import FileSystemManager

class ProjectStructureAgent:
    def __init__(self, llm_type: str, base_path: Path = Path.cwd(), max_retries: int = 5):
        self.llm = self.initialize_llm(llm_type)
        self.llm_manager = LLMManager(self.llm, max_retries=max_retries)
        self.file_system_manager = FileSystemManager(base_path)

    @staticmethod
    def initialize_llm(llm_type: str) -> LLMInterface:
        if llm_type.lower() == 'openai':
            return OpenAIModel()
        elif llm_type.lower() == 'anthropic':
            # return AnthropicModel()
            raise NotImplementedError("AnthropicModel is not implemented yet.")
        else:
            raise ValueError(f"Unsupported LLM type: {llm_type}")

    def execute(self, architecture_description: str, project_name: str):
        print("Parsing architecture description with LLM...")
        structure = self.llm_manager.get_structure(architecture_description)
        print(f"Received structure: {json.dumps(structure, indent=2)}")

        # Set the base path to the specified project name
        project_path = self.file_system_manager.base_path / project_name
        project_path.mkdir(parents=True, exist_ok=True)
        print(f"Creating project structure in: {project_path}")

        self.file_system_manager.create_structure(structure, project_path)
        print("Project structure created successfully.")