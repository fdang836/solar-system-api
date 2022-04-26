from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

planets = [
    Planet(1, "Mercury", "this is mercury", "light grey"),
    Planet(2, "Venus", "this is venus", "yellow/white"),
    Planet(3, "Earth", "this is earth", "blue/green")
]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    all_planet_list = []
    for planet in planets:
        all_planet_list.append({
            "id": planet.id, 
            "name": planet.name,
            "description": planet.description,
            "color": planet.color
        })
    return jsonify(all_planet_list)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return jsonify({"msg": f"Invalid planet id: {planet_id}"}), 400
    
    chosen_planet = None
    for planet in planets:
        if planet.id == planet_id:
            chosen_planet = planet
            break
    
    if chosen_planet is None:
        return jsonify({"msg": f"Could not find planet id: {planet_id}"}), 404

    rsp = {
        "id": chosen_planet.id, 
        "name": chosen_planet.name,
        "description": chosen_planet.description,
        "color": chosen_planet.color
    }
    return jsonify(rsp), 200