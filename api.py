from flask import Flask, redirect, render_template_string, request, render_template
from cs50 import SQL
import json
import communities


app = Flask(__name__)

db = SQL("sqlite:///mikros.db")

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




@app.route("/mikros",  methods=['GET', 'POST'])
def mikros():
    if request.method == "POST":
        input = request.form.get("input")
        # DB stuff
        db.execute("INSERT INTO mikro3mar(alias) VALUES(?)", input)
        return render_template("registrado.html")
    return render_template("mikros.html")

if __name__ == '__main__':
    app.run(host= '178.79.181.140' ,port=9999, debug=True)
    
