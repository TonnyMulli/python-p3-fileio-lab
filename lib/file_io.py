from pathlib import Path

def write_file(file_name, file_content):
    file_path = Path(str(file_name) + '.txt')
    with file_path.open('w') as f:
        f.write(file_content)

def append_file(file_name, file_content):
    file_path = Path(str(file_name) + '.txt')
    with file_path.open('a') as f:
        f.write(file_content)

def read_file(file_name):
    file_path = Path(str(file_name) + '.txt')
    with file_path.open('r') as f:
        return f.read()
