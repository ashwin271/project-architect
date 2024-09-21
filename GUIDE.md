## Project Guide: **ProjectArchitect**

**ProjectArchitect** is a Python-based agent that reads a project architecture description and automatically generates the corresponding file system and populates each file with relevant content. This guide provides a breakdown of the files in the project, explaining their roles and purpose.

---

### Directory Structure Overview

```plaintext
ProjectArchitect/
├── agent.py
├── anthropic_llm.py
├── create_project_structure.py
├── file_system_manager.py
├── llm_interface.py
├── llm_manager.py
├── openai_llm.py
├── requirements.txt
├── .env
└── README.md
```

---

### File Explanations

### 1. **`agent.py`**

- **Purpose**: The "conductor" of ProjectArchitect. It orchestrates the interactions between the components (LLM, file system manager, etc.).
- **Key Responsibilities**:
  - Initialize the appropriate language model (e.g., OpenAI or Anthropic).
  - Use the LLM to parse architecture descriptions.
  - Manage file system creation using `FileSystemManager`.
  - Provides the entry point for the entire project structure generation workflow.

---

### 2. **`anthropic_llm.py`**

- **Purpose**: Handles interactions with **Anthropic's API** to get responses from their language model (e.g., Claude).
- **Key Responsibilities**:
  - Loads the **Anthropic API key** from the `.env` file.
  - Implements the `generate_response()` method to query Anthropic's LLM.
- **Note**: This is currently a placeholder file and will require specific implementation when using Anthropic.

---

### 3. **`create_project_structure.py`**

- **Purpose**: The **main script** that you run to generate the project files based on the architecture description.
- **Key Responsibilities**:
  - Takes user input (e.g., the name of the project and the path to an architecture description file).
  - Initializes the `ProjectStructureAgent` and executes the process to generate the file structure.
  
- **How to Run**:
  ```bash
  python create_project_structure.py --name <project_name> --description <path_to_architecture.txt>
  ```

---

### 4. **`file_system_manager.py`**

- **Purpose**: Manages interactions with the file system, including creating directories, files, and writing content to files.
- **Key Responsibilities**:
  - Creates directories and files based on the parsed JSON from the architecture.
  - Writes content into files, or skips/backs up existing ones if applicable.
  
- **Key Methods**:
  - `create_structure()` – Recursively creates directories, files, and writes content.

---

### 5. **`llm_interface.py`** (Abstract Base Class)

- **Purpose**: Defines the interface for interacting with any **Language Model**.
- **Key Responsibilities**:
  - Standardizes the method that each LLM class should implement (`generate_response()`).
- **Abstract**:
  - This is an abstract base class; concrete classes (like **OpenAI** or **Anthropic**) must implement it.

---

### 6. **`llm_manager.py`**

- **Purpose**: Facilitates the querying of the selected LLM (OpenAI or Anthropic) and manages retries and error handling.
- **Key Responsibilities**:
  - Query language models based on the architecture description.
  - Handle multiple attempts and prompt corrections in case of malformed JSON or incorrect responses from the LLM.
  
- **Key Methods**:
  - `get_structure()` – Obtains a valid project structure from the LLM.
  - `parse_json()` – Parses the response into a usable JSON structure.

---

### 7. **`openai_llm.py`**

- **Purpose**: Handles interactions with **OpenAI's GPT-4** (or GPT-3.5) API to get responses from OpenAI's language model.
- **Key Responsibilities**:
  - Loads the **OpenAI API key** from the `.env` file.
  - Implements the `generate_response()` method to query OpenAI's models.
  - Sends architecture descriptions and retrieves structured, descriptive responses.
  
- **Key Methods**:
  - `generate_response()` – Sends a prompt to OpenAI's GPT-4 and returns the language model's response.

---

### 8. **`requirements.txt`**

- **Purpose**: Lists the necessary Python packages that your project depends on.
- **Key Responsibilities**:
  - Ensures all necessary dependencies (like `openai`, `python-dotenv`) are installed.
  
- **Usage**:
  ```bash
  pip install -r requirements.txt
  ```

- **Example Dependencies**:
  - `openai`: Required to interact with OpenAI's API.
  - `python-dotenv`: To load API keys and secrets from `.env` files.

---

### 9. **`.env`**

- **Purpose**: Stores sensitive environment-specific configuration variables like API keys.
- **Key Responsibilities**:
  - Store your API keys without hard-coding them directly into the code.
  
- **Example Content**:
  ```plaintext
  OPENAI_API_KEY=your_openai_api_key_here
  ANTHROPIC_API_KEY=your_anthropic_api_key_here (if applicable)
  ```

---

### 10. **`README.md`**

- **Purpose**: The main documentation for the project to help users understand what the project does, how to set it up, and how to use it.
  
- **Key Sections**:
  - Overview of the project
  - Setup instructions
  - Usage examples
  - Contributing guidelines

---

### How to Extend or Modify This Project

- **Adding New LLM Providers**:
  - You can create new LLM connectors by extending the `LLMInterface` (e.g., for **Anthropic**, **Hugging Face**, etc.)
  - Add a new file like `my_llm.py`, implement the `generate_response()` method, add support for initializing the respective LLM, and make any necessary API calls.
  
- **Customizable**:
  - Modify the agent (`agent.py`) to ask for additional inputs or apply filters on the architecture description.
  - You can easily extend the abilities by involving more language models or add more custom logic to handle other programming languages.

---

## Conclusion

Now you have a solid overview of what each file does and how it fits into the overall **ProjectArchitect** system. This guide should help users understand the role of each file and how to navigate and extend the project based on their needs.

