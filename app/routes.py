from flask import Blueprint, jsonify, request, abort, make_response
from app.models.planets import Planet
from app import db

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"msg": f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"msg": f"planet {planet_id} not found"}, 404))

    return planet

@planets_bp.route('', methods=['POST'])
def create_one_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body['name'], 
                description=request_body['description'],
                color=request_body['color'])
    db.session.add(new_planet)
    db.session.commit()
    return {
        "id": new_planet.id,
        "msg": f"Successfully created planet with id {new_planet.id}"
    }, 201

@planets_bp.route('', methods=['GET'])
def get_all_planet():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "color": planet.color
        })
    return jsonify(planets_response)


@planets_bp.route('/<planet_id>', methods=['GET'])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    
    rsp = {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "color": planet.color
    }
    return jsonify(rsp)


@planets_bp.route('/<planet_id>', methods=['PUT'])
def put_one_planet(planet_id):
    chosen_planet = validate_planet(planet_id)
    
    request_body = request.get_json()
    chosen_planet.name = request_body["name"]
    chosen_planet.description = request_body["description"]
    chosen_planet.color = request_body["color"]
    db.session.commit()
    rsp = {
        "msg": f"{planet_id} sucessfully updated"
    }
    return jsonify(rsp), 200

@planets_bp.route('/<planet_id>', methods=['DELETE'])
def delete_one_planet(planet_id):
    chosen_planet = validate_planet(planet_id)
    db.session.delete(chosen_planet)
    db.session.commit()
    rsp = {
        "msg": f"{planet_id} sucessfully deleted"
    }
    return jsonify(rsp), 200

# class Planet:
#     def __init__(self, id, name, description, color):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.color = color

# planets = [
#     Planet(1, "Mercury", "this is mercury", "light grey"),
#     Planet(2, "Venus", "this is venus", "yellow/white"),
#     Planet(3, "Earth", "this is earth", "blue/green")
# ]



# @planets_bp.route("", methods=["GET"])
# def get_all_planets():
#     all_planet_list = []
#     for planet in planets:
#         all_planet_list.append({
#             "id": planet.id, 
#             "name": planet.name,
#             "description": planet.description,
#             "color": planet.color
#         })
#     return jsonify(all_planet_list)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def get_one_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         return jsonify({"msg": f"Invalid planet id: {planet_id}"}), 400
    
#     chosen_planet = None
#     for planet in planets:
#         if planet.id == planet_id:
#             chosen_planet = planet
#             break
    
#     if chosen_planet is None:
#         return jsonify({"msg": f"Could not find planet id: {planet_id}"}), 404

#     rsp = {
#         "id": chosen_planet.id, 
#         "name": chosen_planet.name,
#         "description": chosen_planet.description,
#         "color": chosen_planet.color
#     }
#     return jsonify(rsp), 200