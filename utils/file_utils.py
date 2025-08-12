import json
import yaml

def read_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def write_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

def write_yaml(file_path, data):
    with open(file_path, "w") as f:
        yaml.safe_dump(data, f)
