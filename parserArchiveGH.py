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

@app.get("/parse-archive")
def read_archive(archive_path: str = "2017-09-25-22.json"):
    parsed_data = parse_archive_gh_lines(archive_path)
    return parsed_data


@app.get("/parse-archive/id_type")
def read_archive_id_type(archive_path: str = "2017-09-25-22.json"):
    parsed_data = parse_archive_gh_lines(archive_path)
    id_type_list = [{"id": event.get("id"), "type": event.get("type")} for event in parsed_data]
    return id_type_list