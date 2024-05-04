import json
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "../../strings.json")

with open(json_path, "r") as file:
    jsonData = json.load(file)

def get_string(key):
    return jsonData[key]