# ProjectArchitect

**ProjectArchitect** is a Python-based agent that automatically generates a project file system and populates it with appropriate code based on architecture descriptions. It simplifies rapid prototyping by leveraging language models like **OpenAI's GPT-4** to read architecture inputs and build the corresponding file structure with relevant code.

## Features

- **Automated File System Creation**: Generates directories and files based on architecture descriptions.
- **Code Injection**: Populates created files with relevant content.
- **Multi-LLM Support**: Supports multiple language models (e.g., OpenAI, Anthropic).
- **Environment Management**: Securely manages sensitive information like API keys using a `.env` file.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ProjectArchitect.git
   cd ProjectArchitect
   ```

2. **Install Dependencies**

   Install the required Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**

   Create a `.env` file in the root directory of the project to store the **OpenAI API Key** (or **Anthropic API Key**, if applicable):

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here  # Optional, if using Anthropic models
   ```

## Usage

Run the `architect.py` script with the following parameters:

```bash
python architect.py --name <project_name> --description <path_to_architecture.txt> --llm <llm_name>
```

### Parameters

- `--name` (required): Name of the project/directory to create.
- `--description` (optional): Path to the architecture description file. If not provided, you will be prompted to enter the architecture manually.
- `--llm` (optional): LLM to use for generating the structure:
  - `openai` (default): Uses OpenAI's GPT-4.
  - `anthropic`: Intended for Anthropic's models (e.g., Claude).

### Example Command

```bash
python architect.py --name my_fastapi_backend --description architecture.txt --llm openai
```

### Example Architecture Description (`architecture.txt`)

```plaintext
backend/
├── .env
├── main.py                 # FastAPI entry point
├── auth.py                 # Handles authentication, JWT generation
├── datasets.py             # Manages dataset uploads
├── validate.py             # Validates datasets
... also contains code for each files
```

## Future Enhancements

- **Merging Existing Content**: Avoid overwriting files by merging content intelligently.
- **Interactive Prompts**: Ask users whether to overwrite, skip, or back up files.
- **Automatic Git Initialization**: Option to initialize a Git repository after project creation.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

