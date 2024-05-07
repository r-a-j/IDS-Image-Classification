import json
import os 

class StringProcessor:
        
    def get_string(self, key):
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, "../../strings.json")

        with open(json_path, "r") as file:
            jsonData = json.load(file)
        
        return jsonData[key]