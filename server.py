import sys

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/maps")
def maps():
    return render_template('maps.html')

@app.route("/maps/pass_arena2")
def pass_arena2():
    return render_template('pass_arena2.html')

@app.route("/maps/pass_stadium")
def pass_stadium():
    return render_template('pass_stadium.html')

@app.route("/maps/pass_greenhouse")
def pass_greenhouse():
    return render_template('pass_greenhouse.html')

@app.route("/maps/pass_stonework")
def pass_stonework():
    return render_template('pass_stonework.html')

@app.route("/maps/pass_ufo")
def pass_ufo():
    return render_template('pass_ufo.html')

@app.route("/maps/pass_colosseum2")
def pass_colosseum2():
    return render_template('pass_colosseum2.html')

@app.route("/maps/pass_manndamm")
def pass_manndamm():
    return render_template('pass_manndamm.html')

@app.route("/maps/pass_maple")
def pass_maple():
    return render_template('pass_maple.html')

@app.route("/maps/pass_aerosol")
def pass_aerosol():
    return render_template('pass_aerosol.html')

@app.route("/maps/pass_mario")
def pass_mario():
    return render_template('pass_mario.html')

if __name__ == "__main__":
    port = 5000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 5000.")
    app.run(host='0.0.0.0', port=port)