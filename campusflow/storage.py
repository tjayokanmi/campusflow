import json
from pathlib import Path

def save_tickets(records, file_path): 
    path_obj = Path(file_path)

    parent_path = path_obj.parent
    parent_path.mkdir(parents=True, exist_ok=True)

    with open(path_obj, "w", encoding="utf-8") as file:
        json.dump(records, file)
