import json
from fastapi import FastAPI
from pprint import pprint

app = FastAPI()

def parse_archive_gh_lines(archive_path):
    events = []
    with open(archive_path, 'r') as file:
        for line in file:
            event = json.loads(line)
            events.append(event)
    return events

archive = parse_archive_gh_lines("2017-09-25-22.json")

print(len(archive))

@app.get("/parse-archive")
def read_archive(archive_path: str = "2017-09-25-22.json"):
    #parsed_data = parse_archive_gh_lines(archive_path)
    return archive

@app.get("/parse-archive/pagination/{page}")
def read_archive(page : int, archive_path: str = "2017-09-25-22.json"):
    #parsed_data = parse_archive_gh_lines(archive_path)
    nbResultats = 10
    debut = page*nbResultats
    

    retourPagination = archive[debut: debut+nbResultats]
    return retourPagination

@app.get("/parse-archive/id_type")
def read_archive_id_type(archive_path: str = "2017-09-25-22.json"):
    #parsed_data = parse_archive_gh_lines(archive_path)
    id_type_list = [{"id": event.get("id"), 
                    "login": (event.get("actor") or {}).get("login")} for event in archive]
    return id_type_list

@app.get("/parse-archive/status/{status_id}")
def read_status_detail(status_id: str, archive_path: str = "2017-09-25-22.json"):
       
    for event in archive :
        
        if event.get("id") == status_id:
            return event
        else:
            pass
         
    return {"error": "Status ID not found"} 
       
    
