from __future__ import annotations
import sys
from dataclasses import dataclass
from flask import Flask, render_template

app = Flask(__name__)

@dataclass
class Map:
    """Class for storing Map data for the pages page."""
    name: str
    author: str
    description: str
    img_path: str = "imgs/arena2.webp"
    contribution_description: str|None = None
    alternate_url: str|None = None

maps_dict = {
    "Active Rotation": [
        Map("pass_arena2", "Jaguar", "The original.", "imgs/arena2.webp", "Contributors: exer, EaasyE, Danmar, Crutch"),
        Map("pass_boutique", "kin", "GEM ALERT!!!!!💎💎", "imgs/pass_boutique_b7.webp"),
        Map("pass_maple", "kingfin", "An encapsulation of Autumn.", "imgs/pass_maple_a10.webp"),
        Map("pass_plexiglass", "ShearsTF", "Jumper's playground.", "imgs/pass_plexiglass.webp", "Contributor: Danmar"),
        Map("pass_ruin", "DropKnock", "Dunk for your life; satisfy the Mayan gods.", "imgs/pass_ruin_a11.webp"),
        Map("pass_stadium", "exer", "The Superbowl, but bigger.", "imgs/stadium.webp"),
        Map("pass_stonework", "exer", "Ancient ruins with ancient secrets.", "imgs/stonework.webp"),
        Map("pass_torii", "kingfin", "PASS Time ❌<br> PASS Time, Japan ✔️", "imgs/pass_torii_a5.webp"),
    ],
    "Reserve": [
        Map("pass_amsterdam", "flaresh", "Het volgende station is Duivendrecht.", "imgs/pass_amsterdam_a2.webp"),
        Map("pass_aerosol", "flaresh", "Tony Hawk's PASS Time.", "imgs/pass_aerosol_a9.webp", "Original Author: obamid"),
        Map("pass_mario", "kingfin", "Do the Mario!", "imgs/pass_mario_a4.webp"),
        Map("pass_amperage", "exer", "It's not the voltage that kills you...", "imgs/pass_amperage_a11.webp"),
        Map("pass_ore", "kingfin & Kibble Bites", "COAL ALERT!!!!!🚂🚂", "imgs/pass_ore_a5.webp"),
        Map("pass_MannDamm", "owen608", "Stop the Dams.", "imgs/pass_mann_damm_a14.webp", alternate_url="maps/pass_manndamm"),
        Map("pass_colosseum2", "exer", "A modern reimagining of two classics.", "imgs/colosseum2.webp", "Inspired by: obamid"),
        Map("pass_greenhouse", "exer", "Now eco-friendly!", "imgs/greenhouse.webp"),
        Map("pass_ufo", "DropKnock", "Whoever loses gets probed.", "imgs/ufo.webp"),
        Map("pass_greece", "fronz", "Demos kratos.", "imgs/pass_greece_b5.webp", "Inspired by pl_odyssey"),
        Map("pass_aquarium", "Bobby Joe", "The common jack is a powerful, predatory species.", "imgs/pass_aquarium_a15.webp"),
        Map("pass_park", "Bobby Joe", "A third place.", "imgs/pass_park_b27.webp", "Original Author: Kibble Bites"),
        Map("pass_tanoa", "ShearsTF", "Concrete jungle.", "imgs/pass_tanoa_a2.webp", "Inspired by arena2"),
        Map("pass_skyline", "Bobby Joe", "Featuring Neotokyo's most popular bloodsport.", "imgs/pass_skyline_b7.webp", "Original Author: Kibble Bites"),
        Map("pass_junglegroove", "owen608", "His coconut gun can fire in spurts!", "imgs/pass_junglegroove_a10.webp"),
        Map("pass_poptart", "exer", "Remember him.", "imgs/pass_poptart_a3.webp"),
        Map("pass_arena2 Seasons", "exer", "All the seasons! Fall, Winter, Halloween... Uh.", "imgs/pass_arena2_b8_winter_fix.webp", "Built off of arena2", alternate_url="maps/pass_arena2_seasons"),
        Map("pass_dugout", "Bobby Joe", "BEGIN WORK ZONE. TRAFFIC FINES DOUBLE.", "imgs/pass_dugout_b2.webp", "Built off of arena2"),
        Map("pass_arena3", "exer", "[REDACTED]", "imgs/pass_arena3_a1.webp", "Built off of arena2"),
        Map("pass_medieval_arena", "sagejay", "LARPing is required.", "imgs/pass_medieval_arena_v01.webp", "Built off of arena2"),
    ],
    "Jump": [
        Map("pass_training_arena", "owen608", "T2. Welcome to Basic Training.", "imgs/pass_training_arena.webp"),
        Map("jump_jackingoff", "EaasyE", "T3. The original.", "imgs/jump_jackingoff_a7_rampfix2.webp"),
        Map("jump_jackjam", "exer", "T4. Feeling froggy?", "imgs/jump_jackjam_jam2.webp"),
        Map("jump_elongatedjack", "owen608", "T5. Go nuclear or go home.", "imgs/jump_elongatedjack_a5.webp"),
    ],
    "Alternative": [
        Map("pass_krab", "moose", "Lock-off.", "imgs/pass_krab_m1.webp"),
        Map("pass_waterpolo2", "Kibble Bites", "So special it has its own whitelist.", "imgs/pass_waterpolo2_b8d.webp"),
        Map("pass_experiment1", "exer", "Beyond the wall.", "imgs/pass_experiment1_test6.webp", "Built off of...gullywash"),
        Map("cpass_gullywash", "Bobby Joe", "5CP PASS Time. On Gullywash.", "imgs/cpass_gullywash_a1.webp", "Built off of...gullywash"),
        Map("pass_ulama", "BurntVenom", "Goals with added security.", "imgs/pass_ulama.webp"),
        Map("pass_constantinople", "Crutch", "It's kinda green.", "imgs/pass_constantinople_a1.webp", "Built off of arena2"),
        Map("pass_ammo", "exer", "Conjured up from another dimension.", "imgs/pass_ammo_b1.webp"),
        Map("pass_court", "exer", "2v2 BBall. But PASS Time.", "imgs/pass_court_test1.webp"),
        Map("poggers", "EaasyE", "2v2 PASS Time.", "imgs/poggers.webp", "Built off of arena2"),
    ],
    "Templates": [
        Map("pass_4v4_template", "exer", "Essential to create 4v4 PASS Time maps.", "imgs/pass_4v4_template_bobby.webp", "Contributor: Bobby Joe"),
        Map("pass_jump_template", "owen608", "Essential to create PASS Time jump maps.", "imgs/pass_jump_template.webp"),
    ],
    "Antiquated": [
        Map("pass_colosseum", "obamid", "Are you not entertained!?", "imgs/pass_colosseum_a11.webp", "Original Author: waves"),
        Map("pass_smalltown", "obamid", "Ten paces and turn.", "imgs/pass_smalltown_a3.webp", "Original Author: waves"),
        Map("pass_mountain", "Laxson", "A highly iterated experiment from early PASS Time.", "imgs/pass_mountain_b1.webp"),
        Map("pass_frag", "UNKNOWN", "Missing info.", "imgs/pass_frag_a6.webp"),
        Map("arena_glass", "gwd_KOFT", "One and done.", "imgs/arena_glass_a1.webp"),
        Map("pass_genesis", "Construction Zombie", "What Paul Revere warned us about.", "imgs/pass_genesis_a1.webp", "Built off of arena1"),
        Map("pass_concepts", "Laxson", "A collection of very early tests.", "imgs/pass_football2.webp", alternate_url="maps/pass_concepts_laxson"),
    ],
    "Unplayable": [

        Map("pass_industry5", "Hu Hubris", "Please hubris i have to play the map before i die.", "imgs/industry5.webp"),
        Map("pass_hockey", "weeabruh", "Will be finished soon™", "imgs/hockey.webp"),
    ],
}

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/maps")
def maps():
    return render_template('maps.html', maps=maps_dict)

@app.route("/maps/faq")
def faq():
    return render_template('faq.html')

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

@app.route("/maps/pass_amsterdam")
def pass_amsterdam():
    return render_template('pass_amsterdam.html')

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

@app.route("/maps/pass_junglegroove")
def pass_junglegroove():
    return render_template('pass_junglegroove.html')

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

@app.route("/maps/pass_training_arena")
def pass_training_arena():
    return render_template('pass_training_arena.html')

@app.route("/maps/jump_jackjam")
def jump_jackjam():
    return render_template('jump_jackjam.html')

@app.route("/maps/jump_elongatedjack")
def jump_elongatedjack():
    return render_template('jump_elongatedjack.html')

@app.route("/maps/pass_krab")
def pass_krab():
    return render_template('pass_krab.html')

@app.route("/maps/cpass_gullywash")
def cpass_gullywash():
    return render_template('cpass_gullywash.html')

@app.route("/maps/pass_ulama")
def pass_ulama():
    return render_template('pass_ulama.html')

@app.route("/maps/pass_constantinople")
def pass_constantinople():
    return render_template('pass_constantinople.html')

@app.route("/maps/pass_court")
def pass_court():
    return render_template('pass_court.html')

@app.route("/maps/poggers")
def poggers():
    return render_template('poggers.html')

@app.route("/maps/pass_4v4_template")
def pass_4v4_template():
    return render_template('pass_4v4_template.html')

@app.route("/maps/pass_jump_template")
def pass_jump_template():
    return render_template('pass_jump_template.html')

@app.route("/maps/pass_industry5")
def pass_industry5():
    return render_template('pass_industry5.html')

@app.route("/maps/pass_genesis")
def pass_genesis():
    return render_template('pass_genesis.html')

@app.route("/maps/pass_hockey")
def pass_hockey():
    return render_template('pass_hockey.html')

if __name__ == "__main__":
    port = 5000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 5000.")
    app.run(host='0.0.0.0', port=port)

