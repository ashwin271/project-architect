# ProjectArchitect

## Overview

**ProjectArchitect** is a Python-based agent designed to automate the creation of a project’s file system based on a well-defined architecture. The agent reads an input description (architecture) and generates directories, files, and writes relevant code to the specified files. This tool is ideal for setting up the skeleton of projects involving various programming languages and frameworks, making rapid prototyping faster and more efficient.

## Features

- Automatically reads architecture descriptions and creates the corresponding file system.
- Adds relevant code to each file in accordance with the architecture.
- Integrates with **OpenAI’s GPT-4** (Other LLMs can be integrated in the future).
- Can be easily extended for different programming languages and projects (e.g., FastAPI, Flask, etc.).
- Environment variables managed securely via `.env` file, including the OpenAI API key.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ashwin271/project-architect.git
cd ProjectArchitect
```

### 2. Install Dependencies

You'll need **Python 3.8+** to run this project. Install the required dependencies using:

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` File

Create a `.env` file in the root folder of the project, and add the OpenAI API key in it:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Prepare an Architecture Description File

Create a text file like `architecture.txt` with a detailed architecture of what you want the project to look like. Example structure:

```plaintext
FastAPI Backend:
backend/
├── main.py                 # FastAPI entry point
├── auth.py                 # User authentication and JWT management
├── models.py               # SQLAlchemy models
├── database.py             # DB setup with SQLAlchemy
```

### 5. Run the Agent

You can now run the agent to generate the file system based on your architecture description:

```bash
python create_project_structure.py --name <project_name> --description <path_to_architecture.txt>
```

Example:

```bash
python create_project_structure.py --name my_fastapi_backend --description architecture.txt
```

### Example Architecture Input

Here’s an example of how your architecture file might look:

```plaintext
backend/
├── main.py                 # FastAPI application entry
├── auth.py                 # Handles authentication, OAuth, JWT
├── models.py               # SQLAlchemy/ORM models
├── database.py             # DB setup for SQLAlchemy (SQLite or PostgreSQL, optional)
```

After running, your directory structure will be generated based on the input, and the output will be similar to:

```plaintext
my_fastapi_backend/
├── main.py
├── auth.py
├── models.py
├── database.py
└── .env
```

## Requirements

- Python 3.8+
- OpenAI GPT-4 (or necessary LLM) API Key

## Future Enhancements

- **Content Merge**: Option to merge content instead of overwriting when files already exist.
- **Multi-LLM Support**: Expand to support more LLM providers (e.g., Anthropic’s Claude).
- **Interactive File Handling**: Provide an interactive option before overwriting existing files.
- **Template Support**: Add support for reusable templates.
- **Automation with Git**: Auto-commit the structured project into an initialized Git repository.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

