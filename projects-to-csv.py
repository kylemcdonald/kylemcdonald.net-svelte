import pandas as pd
import json

# load projects.json
with open('src/routes/projects.json') as f:
    projects = json.load(f)
    
clients = []
collaborators = []
links = []
works = []
for work in projects:
    works.append([
        work['key'],
        work['name'],
        work['year'],
        work['description']
    ])
    if 'client' in work:
        clients.append([
            work['key'],
            work['client']['name'],
            work['client']['url']
        ])
    for collaborator in work['collaborators']:
        collaborators.append([
            work['key'],
            collaborator['name'],
            collaborator['url']
        ])
    for link in work['links']:
        links.append([
            work['key'],
            link['text'],
            link['url']
        ])
        
works_df = pd.DataFrame(works, columns=['key', 'name', 'year', 'description'])
clients_df = pd.DataFrame(clients, columns=['key', 'name', 'url'])
collaborators_df = pd.DataFrame(collaborators, columns=['key', 'name', 'url'])
links_df = pd.DataFrame(links, columns=['key', 'text', 'url'])

works_df.to_csv('works.tsv', index=False, sep='\t')
clients_df.to_csv('clients.tsv', index=False, sep='\t')
collaborators_df.to_csv('collaborators.tsv', index=False, sep='\t')
links_df.to_csv('links.tsv', index=False, sep='\t')