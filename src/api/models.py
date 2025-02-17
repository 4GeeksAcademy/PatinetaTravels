from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(120), nullable=False)
    email = db.Column(String(120), nullable=False)
    password = db.Column(String(80), nullable=False)
    is_active = db.Column(Boolean(), nullable=False)

    # Relaciones corregidas
    favorites = db.relationship("Favorites", backref="user")
    city = db.relationship("City", backref="user")
    restaurant = db.relationship("Restaurant", backref="user")
    hotel = db.relationship("Hotel", backref="user")
    interest_point = db.relationship("Interest_point", backref="user")

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

class City(db.Model):
    __tablename__ = "city"
    id = db.Column(Integer, primary_key=True)
    city_name = db.Column(String(30), nullable=False)
    country_name = db.Column(String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    favorites = db.relationship("Favorites", backref="city")

    def serialize(self):
        return {
            "id": self.id,
            "city_name": self.city_name,
            "country_name": self.country_name
        }

class Restaurant(db.Model):
    __tablename__ = "restaurant"
    id = db.Column(Integer, primary_key=True)
    restaurant_name = db.Column(String(30), nullable=False)
    address = db.Column(String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    favorites = db.relationship("Favorites", backref="restaurant")

    def serialize(self):
        return {
            "id": self.id,
            "restaurant_name": self.restaurant_name,
            "address": self.address
        }

class Interest_point(db.Model):
    __tablename__ = "interest_point"
    id = db.Column(Integer, primary_key=True)
    int_name = db.Column(String(100), nullable=False)
    locality = db.Column(String(100), nullable=False)
    point_address = db.Column(String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    favorites = db.relationship("Favorites", backref="interest_point")

    def serialize(self):
        return {
            "id": self.id,
            "int_name": self.int_name,
            "point_address": self.point_address
        }

class Hotel(db.Model):
    __tablename__ = "hotel"
    id = db.Column(Integer, primary_key=True)
    hotel_name = db.Column(String(50), nullable=False)
    hotel_address = db.Column(String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    favorites = db.relationship("Favorites", backref="hotel")

    def serialize(self):
        return {
            "id": self.id,
            "hotel_name": self.hotel_name,
            "hotel_address": self.hotel_address
        }

class Favorites(db.Model):
    __tablename__ = "favorites"
    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id")) 
    city_id = db.Column(db.Integer, db.ForeignKey("city.id"), nullable=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey("hotel.id"), nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"), nullable=True)
    interest_point_id = db.Column(db.Integer, db.ForeignKey("interest_point.id"), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "hotel_id": self.hotel_id,
            "interest_point_id": self.interest_point_id,
            "restaurant_id": self.restaurant_id,
            "city_id": self.city_id
        }
