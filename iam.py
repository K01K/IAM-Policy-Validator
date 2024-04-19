import json

def importJSON(filename):
    try:
        with open(filename) as json_file:
            return json.load(json_file)
    except json.JSONDecodeError as e:
        raise Exception(f"Invalid JSON data: {e}")

def checkValidity(json_data):
    for statement in json_data["PolicyDocument"]["Statement"]:
        if statement.get("Resource") == "*":
            print(False)
        else:
            print(True)

filename="test.json"
json_data=importJSON(filename)
checkValidity(json_data)



