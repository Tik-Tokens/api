from flask import Flask, redirect, request
import json

app = Flask(__name__)

@app.route("/")
def index():
    token = request.args.get('token')
    if token:
        return redirect(f'http://178.79.181.140:9999/static/{token}.jpg')
    return 'Not your day brah'

if __name__ == '__main__':
    app.run(host= '178.79.181.140' ,port=9999, debug=True)
