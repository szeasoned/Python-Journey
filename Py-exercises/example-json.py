import json


game = {
        "title": "Minecraft",
        "genre": "Sandbox",
        "release_year": 2011,
        "finished": True
    }

file_path = "json-sample.json"

with open(file_path, "w") as file:
    json.dump(game, file, indent=4)