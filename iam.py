import json
import os

def importJSON(filename):
    try:
        if os.path.exists(filename)==False:
            raise  FileNotFoundError(f"File not found")
        with open(filename) as json_file:
            return json.load(json_file)
    except json.JSONDecodeError as e:
        raise Exception(f"Invalid JSON data: {e}")

def checkValidity(json_data):
    for check in json_data["PolicyDocument"]["Statement"]:
        if check.get("Resource") == "*":
            print(False)
        else:
            print(True)

filename="test.json"
json_data=importJSON(filename)
checkValidity(json_data)



