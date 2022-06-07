import requests
from requests.auth import HTTPBasicAuth
import os
import json
import restore_history
restore_history.restore()

def get_data(key):
    reached_last_page = False
    commit_count = 0
    commit_data = []
    while not reached_last_page:
        data_ = requests.get('https://api.github.com/repos/{}/commits?page={}'.format(key[0]), auth=HTTPBasicAuth(key[1], key[2])).json()
        data = []
        for commit in data_:
            data.append(commit['commit'])
        commit_data += data
        commit_count += len(data)
        if len(data) < 30:
            reached_last_page = True
        else:
            page_count += 1
    return page_count, commit_count, commit_data

keyf = open('key', 'r')
key = keyf.read().split(':')
keyf.close()
page_count, commit_count, commit_data = get_data(key)
os.remove('stored_history.json')
historyf = open('stored_history.json', 'x')
history_data = {
    'commit_count': commit_count,
    'commit_data': commit_data
}

historyf.write(json.dumps(history_data))
historyf.close()
requests.get('http://localhost:5636/update_stored_commit_history')
