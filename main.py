from flask import Flask
from flask_restful import Api, Resource
import errors

app = Flask(__name__)
api = Api(app, errors=errors.errors, catch_all_404s=True)

class GetCommitHistory(Resource):
    def get(self):
        data = [{'message': 'test'}, {'message': 'test2'}, {'message': 'test3'}]
        return data

api.add_resource(GetCommitHistory, '/get_commit_history')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5636)