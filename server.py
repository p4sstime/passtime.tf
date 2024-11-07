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

@app.route("/maps/pass_amperage")
def pass_amperage():
    return render_template('pass_amperage.html')

@app.route("/maps/pass_plexiglass")
def pass_plexiglass():
    return render_template('pass_plexiglass.html')

@app.route("/maps/pass_torii")
def pass_torii():
    return render_template('pass_torii.html')

@app.route("/maps/pass_boutique")
def pass_boutique():
    return render_template('pass_boutique.html')

@app.route("/maps/pass_ore")
def pass_ore():
    return render_template('pass_ore.html')

@app.route("/maps/pass_greece")
def pass_greece():
    return render_template('pass_greece.html')

@app.route("/maps/pass_aquarium")
def pass_aquarium():
    return render_template('pass_aquarium.html')

@app.route("/maps/pass_park")
def pass_park():
    return render_template('pass_park.html')

@app.route("/maps/pass_ruin")
def pass_ruin():
    return render_template('pass_ruin.html')

@app.route("/maps/pass_tanoa")
def pass_tanoa():
    return render_template('pass_tanoa.html')

@app.route("/maps/pass_skyline")
def pass_skyline():
    return render_template('pass_skyline.html')

@app.route("/maps/pass_poptart")
def pass_poptart():
    return render_template('pass_poptart.html')

@app.route("/maps/pass_arena2_seasons")
def pass_arena2_seasons():
    return render_template('pass_arena2_seasons.html')

@app.route("/maps/pass_dugout")
def pass_dugout():
    return render_template('pass_dugout.html')

@app.route("/maps/pass_arena3")
def pass_arena3():
    return render_template('pass_arena3.html')

@app.route("/maps/pass_medieval_arena")
def pass_medieval_arena():
    return render_template('pass_medieval_arena.html')

@app.route("/maps/pass_waterpolo2")
def pass_waterpolo2():
    return render_template('pass_waterpolo2.html')

@app.route("/maps/pass_ammo")
def pass_ammo():
    return render_template('pass_ammo.html')

@app.route("/maps/pass_colosseum")
def pass_colosseum():
    return render_template('pass_colosseum.html')

@app.route("/maps/pass_smalltown")
def pass_smalltown():
    return render_template('pass_smalltown.html')

@app.route("/maps/pass_experiment1")
def pass_experiment1():
    return render_template('pass_experiment1.html')

@app.route("/maps/arena_glass")
def arena_glass():
    return render_template('arena_glass.html')

@app.route("/maps/pass_frag")
def pass_frag():
    return render_template('pass_frag.html')

@app.route("/maps/pass_mountain")
def pass_mountain():
    return render_template('pass_mountain.html')

@app.route("/maps/pass_concepts_laxson")
def pass_concepts_laxson():
    return render_template('pass_concepts_laxson.html')

@app.route("/maps/jump_jackingoff")
def jump_jackingoff():
    return render_template('jump_jackingoff.html')

if __name__ == "__main__":
    port = 5000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 5000.")
    app.run(host='0.0.0.0', port=port)