from flask_sqlalchemy import SQLAlchemy
import os
import sys
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship, Mapped
from typing import List
from sqlalchemy import ForeignKey

db = SQLAlchemy()

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = mapped_column(Integer, primary_key=True)
    email = mapped_column(String(120), unique=True, nullable=False)
    password = mapped_column(String(80), unique=False, nullable=False)
    is_active = mapped_column(Boolean(), unique=False, nullable=False)
    favorites: Mapped[List["City"]] = relationship()
    favorites: Mapped[List["Restaurant"]] = relationship()
    favorites: Mapped[List["Interest_point"]] = relationship()
    favorites: Mapped[List["Hotel"]] = relationship()
    

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class City (Base):
    __tablename__ = 'city'
    id = mapped_column(Integer, primary_key=True)
    city_name = mapped_column(String(30),unique=True, nullable=False)
    country_name = mapped_column(String(30),nullable=False)
    favorites: Mapped[List["Favorites"]] = relationship()
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    def serialize(self):
        return {
            "id": self.id,
            "city_name": self.city_name,
            "country_name": self.country_name
            # do not serialize the password, its a security breach
        }

class Restaurant (Base):
    __tablename__ = 'restaurant'
    id =mapped_column(Integer,primary_key=True)
    restaurant_name = mapped_column (String(30), unique=True, nullable=False)
    address = mapped_column(String(100),unique=False, nullable=False)
    favorites: Mapped[List["Favorites"]] = relationship()
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    def serialize(self):
        return {
            "id": self.id,
            "restaurant_name": self.restaurant_name,
            "address": self.address
            # do not serialize the password, its a security breach
        }

class Interest_point(Base):
    __tablename__ = 'interest_point'
    id = mapped_column(Integer, primary_key=True)
    int_name = mapped_column(String(100),unique=True, nullable=False)
    locality = mapped_column(String(100),unique=False , nullable=False)
    point_address = mapped_column(String(100),unique=True , nullable=False)
    favorites: Mapped[List["Favorites"]] = relationship()
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    def serialize(self):
        return {
            "id": self.id,
            "int_name": self.int_name,
            "point_address": self.point_address
            # do not serialize the password, its a security breach
        }

class Hotel(Base):
    __tablename__ = 'hotel'
    id = mapped_column(Integer, primary_key=True)
    hotel_name = mapped_column(String(50),unique=True, nullable=False)
    hotel_address = mapped_column(String(100),unique=True, nullable=False)
    favorites: Mapped[List["Favorites"]] = relationship()
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    def serialize(self):
        return {
            "id": self.id,
            "hotel_name": self.hotel_name,
            "hotel_address": self.hotel_address
            # do not serialize the password, its a security breach
        }

class Favorites (Base):
    __tablename__ = 'favorites'
    id = mapped_column(Integer, primary_key=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotel.id"))
    interest_point_id: Mapped[int] = mapped_column(ForeignKey("interest_point.id"))
    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurant.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    def serialize(self):
        return {
            "id": self.id,
            "hotel_id": self.hotel_id,
            "interest_point": self.interest_point.id,
            "restaurant_id": self.restaurant_id,
            "city_id": self.city_id            
            

            # do not serialize the password, its a security breach
        }
    

    
