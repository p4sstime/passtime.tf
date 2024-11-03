import sys

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/maps")
def maps():
    return render_template('maps.html')

@app.route("/pass_arena2")
def pass_arena2():
    return render_template('pass_arena2.html')

@app.route("/pass_stadium")
def pass_stadium():
    return render_template('pass_stadium.html')

@app.route("/pass_greenhouse")
def pass_greenhouse():
    return render_template('pass_greenhouse.html')

@app.route("/pass_stonework")
def pass_stonework():
    return render_template('pass_stonework.html')

@app.route("/pass_ufo")
def pass_ufo():
    return render_template('pass_ufo.html')

@app.route("/pass_colosseum2")
def pass_colosseum2():
    return render_template('pass_colosseum2.html')

if __name__ == "__main__":
    port = 5000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 5000.")
    app.run(host='0.0.0.0', port=port)