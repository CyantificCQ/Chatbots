import json 
from difflib import get_close_matches 

#Load the knowledge base from a Json file 
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, "r") as f: 
        data: dict = json.load(f)
    return data

# def print_hi(name):
#     print(f"Hi {name}")
    
    
# if __name__ == "__main__":
#     print_hi("Pycharm")