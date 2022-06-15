from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(120), unique=False, nullable=True)
    hair_color = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    population = db.Column(db.Integer, nullable=True)
    climate = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return '<Planets %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "climate": self.climate,
            # do not serialize the password, its a security breach
        }

class Starships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    model = db.Column(db.String(120), unique=True, nullable=True)
    length = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Starships %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "length": self.length,
            # do not serialize the password, its a security breach
        }

class Fav_people(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #quien le dio a favoritos
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))
    #quien es el favorito
    people_id= db.Column(db.Integer, db.ForeignKey('people.id'))
    #definir las relaciones
    rel_user= db.relationship(User)
    rel_people= db.relationship(People)

    def __repr__(self):
        return '<FavPeople %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id,
            # do not serialize the password, its a security breach
        }

class Fav_planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))
    planets_id= db.Column(db.Integer, db.ForeignKey('planets.id'))
    rel_user= db.relationship(User)
    rel_planets= db.relationship(Planets)

    def __repr__(self):
        return '<FavPlanets %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planets_id": self.planets_id,
            # do not serialize the password, its a security breach
        }

class Fav_starships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))
    starships_id= db.Column(db.Integer, db.ForeignKey('starships.id'))
    rel_user= db.relationship(User)
    rel_starships= db.relationship(Starships)

    def __repr__(self):
        return '<FavStarships %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "starships_id": self.starships_id,
            # do not serialize the password, its a security breach
        }