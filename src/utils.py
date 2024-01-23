import json

def read_json(cfg_path):
    with open(cfg_path) as json_file:
        data = json.load(json_file)
    return data