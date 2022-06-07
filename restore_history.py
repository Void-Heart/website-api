import os
def restore():
    if not os.path.exists('stored_history.json'):
        historyf = open('stored_history.json', 'x')
        historyf.write(
            '{"commit_count": 0, "commit_data": []}'
        )
        historyf.close()
