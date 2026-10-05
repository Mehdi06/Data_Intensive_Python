import sqlite3
import json

def parse_archive_gh_lines(archive_path):
    events = []
    with open(archive_path, 'r') as file:
        for line in file:
            event = json.loads(line)
            events.append(event)
    return events


if __name__ == "__main__":
    
    #Initialisation

    archive = parse_archive_gh_lines("2017-09-25-22.json")
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    # Creation de la table
    c.execute("CREATE TABLE github(id, type, auteur)")

    #Remplissage de la table 
    
    for event in archive:
        event_id = event.get('id')
        event_type = event.get('type')
        actor_login = event.get('actor', {}).get('login')
        c.execute("INSERT OR IGNORE into github (id, type, auteur) VALUES (?, ?, ?)",
        (event_id, event_type, actor_login))

    conn.commit()
    conn.close() 

    print("Fin d'embasement")



