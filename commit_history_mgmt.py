import json
class CommitHistory:
    def __init__(self):
        self.commit_data = []
        self.page_count = 1
        self.commit_count = 0
    def update_data(self):
        f = open('stored_history.json')
        data = f.read()
        f.close()
        data = json.loads(data)
        self.page_count = data['page_count']
        self.commit_count = data['commit_count']
        self.commit_data = data['commit_data']
    def commit_data_by_page(self, page):
        pages = []
        for page in range(self.page_count):
            pages.append([])
        index = 0
        for commit in self.commit_data:
            i = 0
