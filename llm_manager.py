import json
from typing import Optional
from llm_interface import LLMInterface

class LLMManager:
    def __init__(self, llm_model: LLMInterface, max_retries: int = 5):
        self.llm = llm_model
        self.max_retries = max_retries

    def get_structure(self, description: str) -> dict:
        prompt = f"""
You are an assistant that converts detailed system architecture descriptions into a JSON structure representing the file and directory layout with file contents.

Description:
{description}

JSON Structure:
{{
    "name": "root_directory",
    "type": "directory",
    "children": [
        {{
            "name": "sub_directory",
            "type": "directory",
            "children": [
                {{
                    "name": "file.py",
                    "type": "file",
                    "content": "def main():\\n    pass\\n\\nif __name__ == '__main__':\\n    main()"
                }}
            ]
        }},
        {{
            "name": "file2.py",
            "type": "file",
            "content": "#!/usr/bin/env python3\\nprint('Hello, World!')"
        }}
    ]
}}
        """
        attempt = 0
        response = ""
        while attempt < self.max_retries:
            try:
                response = self.llm.generate_response(prompt)
                structure = self.parse_json(response)
                return structure
            except ValueError as ve:
                print(f"Attempt {attempt + 1}: {ve}")
                correction_prompt = f"""
The JSON structure provided was invalid. Please correct it.

Original Response:
```
{response}
```

Provide a valid JSON structure as per the specified format, including file paths and their content.
"""
                prompt = correction_prompt
                attempt += 1
        raise RuntimeError("Max retries exceeded. Failed to obtain a valid JSON structure from the LLM.")

    @staticmethod
    def parse_json(response: str) -> dict:
        try:
            # Attempt to locate the JSON block within the response
            json_start = response.find('{')
            json_end = response.rfind('}') + 1
            json_str = response[json_start:json_end]
            structure = json.loads(json_str)
            # Validate the structure
            if not isinstance(structure, dict):
                raise ValueError("Parsed JSON is not a dictionary.")
            if 'name' not in structure or 'type' not in structure:
                raise ValueError("JSON structure missing required fields ('name', 'type').")
            return structure
        except json.JSONDecodeError as e:
            raise ValueError(f"JSON decoding failed: {e}")