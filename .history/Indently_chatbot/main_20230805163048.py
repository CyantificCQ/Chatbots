import json 
from difflib import get_close_matches 

#Load the knowledge base from a Json file 
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, "r") as f: 
        data: dict = json.load(f)
    return data


def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)
        
    
def find_best_match(user_question:str, question:list(str))->str: