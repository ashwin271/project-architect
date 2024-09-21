from pathlib import Path

class FileSystemManager:
    def __init__(self, base_path: Path):
        self.base_path = base_path

    def create_structure(self, structure: dict, current_path: Path = None):
        if current_path is None:
            current_path = self.base_path

        if structure['type'] == 'directory':
            dir_path = current_path / structure['name']
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {dir_path}")
            for child in structure.get('children', []):
                self.create_structure(child, dir_path)
        elif structure['type'] == 'file':
            file_path = current_path / structure['name']
            if not file_path.exists():
                file_path.touch()
                print(f"Created file: {file_path}")
            else:
                print(f"File already exists: {file_path}")
            if 'content' in structure:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(structure['content'])
                print(f"Wrote content to: {file_path}")
        else:
            print(f"Unknown type: {structure['type']} for {structure['name']}")