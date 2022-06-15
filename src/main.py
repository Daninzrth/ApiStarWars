"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, People, Planets, Starships, User, Fav_people, Fav_planets, Fav_starships
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#en este archivo creamos nuestras rutas
@app.route('/user', methods=['GET'])
def get_user():
    alluser = User.query.all()
    alluser = list(map(lambda x: x.serialize(), alluser))
    print(alluser)
    return jsonify({"resultado": alluser})

@app.route('/user/favorites/<int:id>', methods=['GET'])
def get_favorites(id):
    peoplefavorites = Fav_people.query.filter_by(user_id=id)
    peoplefavorites = list(map(lambda x: x.serialize(), peoplefavorites))
    starshipsfavorites = Fav_starships.query.filter_by(user_id=id)
    starshipsfavorites = list(map(lambda x: x.serialize(), starshipsfavorites))
    planetfavorites = Fav_planets.query.filter_by(user_id=id)
    planetfavorites = list(map(lambda x: x.serialize(), planetfavorites))
    return jsonify({"resultado": peoplefavorites + starshipsfavorites +planetfavorites})
    


@app.route('/people', methods=['GET'])
def get_people():
    allpeople = People.query.all()
    allpeople = list(map(lambda x: x.serialize(), allpeople))
    print(allpeople)
    return jsonify({"resultado": allpeople})

@app.route('/people/<int:id>', methods=['GET'])
def get_one_people(id):
    onepeople = People.query.get(id)
    if onepeople:
        onepeople = onepeople.serialize()
        return jsonify({"resultado": onepeople})
    else: 
        return jsonify({"resultado": "personaje no existe"})

@app.route("/favorite/people/<int:people_id>", methods=['POST'])
def add_fav_people(people_id):
    onepeople= People.query.get(people_id)
    if onepeople:
        new = Fav_people() #instancio clase
        new.user_id = 1 
        new.people_id = people_id
        db.session.add(new) #se agregan los registros en la base de dato
        db.session.commit() #guardar los cambios realizados
        return jsonify({"mensaje": "Todo salio bien"})
    else: 
        return jsonify({"resultado": "personaje no existe"})

@app.route("/favorite/people/<int:id>", methods=['DELETE'])
def delete_fav_people(id):
    onepeople = Fav_people.query.get(id)
    print(onepeople)
    if onepeople:
        db.session.delete(onepeople)
        db.session.commit()
        return jsonify({"mensaje": "Todo salio bien"})
    else: 
        return jsonify({"resultado": "personaje no existe"})

@app.route('/planets', methods=['GET'])
def get_planets():
    allplanets = Planets.query.all()
    allplanets = list(map(lambda x: x.serialize(), allplanets))
    print(allplanets)
    return jsonify({"resultado": allplanets})

@app.route('/planets/<int:id>', methods=['GET'])
def get_one_planets(id):
    oneplanets = Planets.query.get(id)
    if oneplanets: 
        oneplanets = oneplanets.serialize()
        return jsonify({"resultado": oneplanets})
    else: 
        return jsonify({"resultado": "planeta no existe"})

@app.route("/favorite/planets/<int:planets_id>", methods=['POST'])
def add_fav_planets(planets_id):
    oneplanets= Planets.query.get(planets_id)
    if oneplanets:
        new = Fav_planets() 
        new.user_id = 1 
        new.planets_id = planets_id
        db.session.add(new) 
        db.session.commit() 
        return jsonify({"mensaje": "Todo salio bien"})
    else: 
        return jsonify({"resultado": "planeta no existe"})

@app.route("/favorite/planets/<int:planets_id>", methods=['DELETE'])
def delete_fav_planets(planets_id):
    oneplanets = Fav_people.query.get(id)
    print(oneplanets)
    if oneplanets:
        db.session.delete(oneplanets)
        db.session.commit()
        return jsonify({"mensaje": "Todo salio bien"})
    else: 
        return jsonify({"resultado": "planeta no existe"})

@app.route('/starships', methods=['GET'])
def get_starships():
    allstarships = Starships.query.all()
    allstarships = list(map(lambda x: x.serialize(), allstarships))
    print(allstarships)
    return jsonify({"resultado": allstarships})

@app.route('/starships/<int:id>', methods=['GET'])
def get_one_starships(id):
    onestarships = Starships.query.get(id)
    if onestarships:
        onestarships = onestarships.serialize()
        return jsonify({"resultado": onestarships})
    else: 
        return jsonify({"resultado": "nave no existe"})

@app.route("/favorite/starships/<int:starships_id>", methods=['POST'])
def add_fav_starships(starships_id):
    onestarships= Starships.query.get(starships_id)
    if onestarships:
        new = Fav_starships() 
        new.user_id = 1 
        new.starships_id = starships_id
        db.session.add(new) 
        db.session.commit() 
        return jsonify({"mensaje": "Todo salio bien"})
    else: 
        return jsonify({"resultado": "nave no existe"})

@app.route("/favorite/starships/<int:starships_id>", methods=['DELETE'])
def delete_fav_starships(planets_id):
    onestarships = Fav_starships.query.get(id)
    print(onestarships)
    if onestarships:
        db.session.delete(onestarships)
        db.session.commit()
        return jsonify({"mensaje": "Todo salio bien"})
    else: 
        return jsonify({"resultado": "nave no existe"})

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
