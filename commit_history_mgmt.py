import json
import restore_history
class CommitHistory:
    def __init__(self):
        self.commit_data = []
        self.commit_count = 0
        restore_history.restore()
    def update_data(self):
        f = open('stored_history.json')
        data = f.read()
        f.close()
        data = json.loads(data)
        self.commit_count = data['commit_count']
        self.commit_data = data['commit_data']
