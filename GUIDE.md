# ProjectArchitect - File Guide

This guide provides a breakdown of each file in **ProjectArchitect** to help contributors and users understand its structure.

## Directory Structure

```plaintext
ProjectArchitect/
├── agent.py
├── anthropic_llm.py
├── architect.py
├── file_system_manager.py
├── llm_interface.py
├── llm_manager.py
├── openai_llm.py
├── requirements.txt
├── .env
└── GUIDE.md
```

## File Overview

### 1. `agent.py`
- **Purpose**: Coordinates all components. Initializes the LLM, parses the architecture description, and manages file creation.
  
### 2. `anthropic_llm.py`
- **Purpose**: Manages interactions with **Anthropic's API** (e.g., Claude). Currently requires implementation for Anthropic models.

### 3. `architect.py`
- **Purpose**: The main execution point for generating the project structure.
  
  **Key Responsibilities**:
  - Takes inputs as command-line arguments.
  - Initializes and runs the agent to generate the project structure.

### 4. `file_system_manager.py`
- **Purpose**: Creates directories and files and writes content. Can handle existing files (e.g., overwrite or backup).
  
### 5. `llm_interface.py`
- **Purpose**: Defines the abstract base class (`LLMInterface`) for the interaction models. Concrete models must implement its `generate_response()` method.

### 6. `llm_manager.py`
- **Purpose**: Manages communication with the LLM, including error handling and response validation.
  
### 7. `openai_llm.py`
- **Purpose**: Handles interactions with **OpenAI's GPT-4** API to get responses based on the architecture description.

### 8. `requirements.txt`
- **Purpose**: Lists the external Python libraries required by the project.
  
### 9. `.env`
- **Purpose**: Stores environment variables such as API keys for secure access.

---

## Project Anatomy

When the project agent runs, here’s how the process works:

1. **`architect.py`**
   - Accepts parameters (`--name`, `--description`, `--llm`) and reads the architecture file or user input.
   - Initializes the **agent**.
   
2. **`agent.py`**
   - Selects the appropriate LLM based on the provided LLM type (`openai` or `anthropic`).
   - Calls the **LLM Manager** to parse the architecture description.
   
3. **`llm_manager.py`**
   - Sends the architecture description to the LLM to retrieve a structured JSON-like response.
   - Re-attempts if the LLM provides malformed responses.

4. **`file_system_manager.py`**
   - Creates the project structure (folders and files) and writes relevant content to the files.

---

## Running the Agent

### Command Example:
```bash
python architect.py --name my_fastapi_backend --description architecture.txt --llm openai
```

This will:
- Create a project directory named `my_fastapi_backend`.
- Generate files and directories as specified in `architecture.txt`.
- Populate the files with boilerplate code, using **OpenAI's GPT-4**.

---

## Extending the Project

### Adding New LLMs

1. **Create a New LLM Class**: Implement the `LLMInterface` for another LLM provider (e.g., Hugging Face).
2. **Update the Agent**: Modify `agent.py` to support the new LLM.

### Additional Features:
- Modify `file_system_manager.py` to ask users about overwriting files, or introduce merge strategies.

---

## Troubleshooting

### Common Issues

1. **API Key Not Found**: Ensure the `.env` file contains the correct API key and that you're using the right environment for running the script (`python-dotenv` must be installed).
   
2. **Incomplete Architecture Output**: Make sure your architecture description provides sufficient detail for the LLM to generate a JSON structure. Review the architecture description if necessary.
   
3. **Existing Files Overwritten**: Customize `file_system_manager.py` to skip or back up files instead of overwriting.

---
