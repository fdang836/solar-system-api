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