urls = {
    "works": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQW0OzOpxMwaB2mTNQFDgqwrZjCX4ORHQcXBzqMUc-FcsR5Qhxftl3_JqGdjIfpkDZShZarfUG8H_ba/pub?gid=1340996408&single=true&output=csv",
    "links": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQW0OzOpxMwaB2mTNQFDgqwrZjCX4ORHQcXBzqMUc-FcsR5Qhxftl3_JqGdjIfpkDZShZarfUG8H_ba/pub?gid=661932165&single=true&output=csv",
    "collaborators": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQW0OzOpxMwaB2mTNQFDgqwrZjCX4ORHQcXBzqMUc-FcsR5Qhxftl3_JqGdjIfpkDZShZarfUG8H_ba/pub?gid=1388006609&single=true&output=csv",
    "clients": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQW0OzOpxMwaB2mTNQFDgqwrZjCX4ORHQcXBzqMUc-FcsR5Qhxftl3_JqGdjIfpkDZShZarfUG8H_ba/pub?gid=1415275685&single=true&output=csv"
}

import pandas as pd
import json
import requests
import os

data = {}
for key, url in urls.items():
    df = pd.read_csv(url)
    data[key] = df.to_dict(orient='records')
    
projects = data['works']
projects = {e['key']: e for e in projects}

for link in data['links']:
    key = link['key']
    if 'links' not in projects[key]:
        projects[key]['links'] = []
    projects[key]['links'].append({
        "text": link['text'],
        "url": link['url']
    })
    
for collaborator in data['collaborators']:
    key = collaborator['key']
    if 'collaborators' not in projects[key]:
        projects[key]['collaborators'] = []
    projects[key]['collaborators'].append({
        "name": collaborator['name'],
        "url": collaborator['url']
    })
    
for client in data['clients']:
    key = client['key']
    projects[key]['client'] = {
        "name": client['name'],
        "url": client['url']
    }
    
# save to projects.json
projects = [v for k, v in projects.items()]
with open('src/routes/projects.json', 'w') as f:
    json.dump(projects, f, indent=2)