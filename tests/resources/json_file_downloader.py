import os
import json
import datetime
import requests

def write_json_file(repo_full_name, data_to_be_saved, iso_date):
    for specific_dir in ['latest_json_files_captured', iso_date]:
        filename = os.path.normpath(
            './tests/resources/json_files_captured/'
            + specific_dir
            + '/'
            + repo_full_name.replace('/', '_') 
            + '.json')
        dirpath = os.path.dirname(filename)
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        print 'New Json file downloaded in: ', filename
        with open(filename, 'w') as f:
            json.dump(data_to_be_saved, f, indent=4)

def request_json_data(repo_full_name):
    github_url = 'https://api.github.com/repos/'
    url = github_url + repo_full_name.replace('_','/')
    response = requests.get(url)
    return response.json()

#https://api.github.com/repos/pallets/flask
#https://api.github.com/repos/django/django
#https://api.github.com/repos/tornadoweb/tornado
iso_date = datetime.datetime.utcnow().replace(microsecond=0).isoformat()
for repo in ['pallets/flask', 'django/django', 'tornadoweb/tornado']:
    json_data = request_json_data(repo)
    write_json_file(repo, json_data, iso_date)
