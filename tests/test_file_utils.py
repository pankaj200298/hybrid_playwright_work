from utils.file_utils import write_json,read_json,write_yaml,read_yaml


def test_json_yaml_utils(tmp_path):
    json_file = tmp_path / "data.json"
    yaml_file = tmp_path / "data.yaml"

    data = {"username": "test_user", "password": "pass123"}

    write_json(json_file, data)
    assert read_json(json_file) == data

    write_yaml(yaml_file, data)
    assert read_yaml(yaml_file) == data
