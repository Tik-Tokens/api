from flask import Flask, redirect, request
import json
import communities

app = Flask(__name__)



@app.route("/")
def index():
    if request.method == 'POST':
        # call cummunities and create entry database
        return 'yo man this is post'
    
    token = request.args.get('token')
    # token number -> hash function to community // call helpers?
    community = communities.mikros()
    if token:
        return json.dumps(community)

    return 'Not your day brah'

if __name__ == '__main__':
    app.run(host= '178.79.181.140' ,port=9999, debug=True)
    