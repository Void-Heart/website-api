from flask import Flask
from flask_restful import Api, Resource, reqparse
import errors
import commit_history_mgmt

app = Flask(__name__)
api = Api(app, errors=errors.errors, catch_all_404s=True)
commit_history = commit_history_mgmt.CommitHistory()
commit_history.update_data()
class GetCommitHistory(Resource):
    def get(self):
        if page is None:
            page = 1
        data = {
            'commit_count': commit_history.commit_count,
            'commit_data': commit_history.commit_data
        }
        return data

class UpdateStoredCommitHistory(Resource):
    def get(self):
        commit_history.update_data()

api.add_resource(GetCommitHistory, '/get_commit_history')
api.add_resource(UpdateStoredCommitHistory, '/update_stored_commit_history')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5636)