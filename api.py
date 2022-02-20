from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def index():
    return 'hello mom'

if __name__ == '__main__':
    app.run(host= '178.79.181.140' ,port=9999, debug=True)
