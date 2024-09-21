import argparse
from pathlib import Path
from agent import ProjectStructureAgent

def main():
    parser = argparse.ArgumentParser(description="Generate project structure based on architecture description.")
    parser.add_argument(
        '--llm',
        type=str,
        default='openai',
        help='Language model to use (e.g., openai, anthropic).'
    )
    parser.add_argument(
        '--description',
        type=str,
        required=False,
        help='Path to the file containing the architecture description.'
    )
    parser.add_argument(
        '--name',
        type=str,
        required=True,
        help='Name of the project/directory to create.'
    )

    args = parser.parse_args()

    # Read the architecture description
    if args.description:
        description_path = Path(args.description)
        if not description_path.exists():
            print(f"Description file not found: {description_path}")
            return
        with open(description_path, 'r', encoding='utf-8') as f:
            architecture_description = f.read()
    else:
        # If no file is provided, use a default or prompt the user
        architecture_description = input("Enter the system architecture description:\n")

    # Initialize and execute the agent
    try:
        agent = ProjectStructureAgent(llm_type=args.llm, base_path=Path.cwd())
        agent.execute(architecture_description, args.name)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()