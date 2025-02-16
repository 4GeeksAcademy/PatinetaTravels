"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, City, Restaurant, Interest_point, Hotel, Favorites
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from sqlalchemy import select

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

# Endpoint Singup 

@api.route("/signup", methods=["POST"])
def signup():
    name = request.json.get("name", None)
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    if not name or not email or not password:
        return jsonify({"msg": "Todos los campos son obligatorios"}), 400

    user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one_or_none()

    if user:
        return jsonify({"msg": "El usuario ya existe"}), 400

    new_user = User(name=name, email=email, password=password, is_active=True) 
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "Usuario creado exitosamente"}), 201

# Endpoint LOGIN
# Cree una ruta para autenticar a sus usuarios y devolver JWT. El
# La función create_access_token() se utiliza para generar el JWT.
@api.route("/login", methods=["POST"])
def login():
           
        email = request.json.get("email", None)
        password = request.json.get("password", None)
        #Tenemos que hacer una consulta de usuario 
        # user = User.query.filter_by(email=email).first()
        user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one_or_none()
        print(User)
        if user is None:
           return jsonify({"msg": "Email not found "}), 401   

        if email == user.email and password == user.password:
           access_token = create_access_token(identity=email)    
           return jsonify(access_token=access_token), 200
        else:
            return jsonify({"msg": "bad email or password"}), 401 
        

# Gets Usuarios_________ 

@api.route('/User', methods=['GET'])
def todos_los_usuarios():


    data = db.session.scalars(select(User)).all()
    results = list(map(lambda User: User.serialize(),data))
   
    response_body = {
        "msg": "Hola, aqui tienes la lista de todos los usuarios: ",
        "results":results
    }

    return jsonify(response_body), 200

@api.route('/User/<int:id>', methods=['GET'])
def solo_un_usuario(id):
   
 try:

    usuario = db.session.execute(select(User).filter_by(id=id)).scalar_one()
   
    response_body = {
        "msg": "Hola, aqui esta el usuario que buscabas ",
        "results":usuario.serialize()
    }


    return jsonify(response_body), 200

 except:

    return jsonify({"msg":"user not exist"}), 404



# Gets Ciudades________


@api.route('/City', methods=['GET'])
def todas_las_ciudades():

    data = db.session.scalars(select(City)).all()
    results = list(map(lambda City: City.serialize(),data))
   
    response_body = {
        "msg": "Hola, aqui tienes la lista de todas las ciudades: ",
        "results":results
    }

    return jsonify(response_body), 200

# @api.route('/City/<int:id>', methods=['GET'])
# def solo_una_ciudad(id):
   
#  try:

#     ciudad = db.session.execute(select(City).filter_by(id=id)).scalar_one()
   
#     response_body = {
#         "msg": "Hola, aqui esta la ciudad que buscas ",
#         "results":ciudad.serialize()
#     }


#     return jsonify(response_body), 200

#  except:

#     return jsonify({"msg":"City not exist"}), 404



# # Gets Restaurant_________


# @api.route('/Restaurant', methods=['GET'])
# def todas_loss_restaurantes():


#     data = db.session.scalars(select(Restaurant)).all()
#     results = list(map(lambda Restaurant: Restaurant.serialize(),data))
   
#     response_body = {
#         "msg": "Hola, aqui tienes la lista de todas los Restaurantes: ",
#         "results":results
#     }

#     return jsonify(response_body), 200

# @api.route('/Restaurant/<int:id>', methods=['GET'])
# def solo_un_restaurante(id):
   
#  try:

#     restaurante = db.session.execute(select(Restaurant).filter_by(id=id)).scalar_one()
   
#     response_body = {
#         "msg": "Hola, aqui esta la ciudad que buscas ",
#         "results":restaurante.serialize()
#     }


#     return jsonify(response_body), 200

#  except:

#     return jsonify({"msg":"Restaurant not exist"}), 404




# # Gets Interest_point _________


# @api.route('/Interest_point', methods=['GET'])
# def all_interest_point():


#     data = db.session.scalars(select(Interest_point)).all()
#     results = list(map(lambda Interest_point: Interest_point.serialize(),data))
   
#     response_body = {
#         "msg": "Hola, aqui tienes la lista de todos los puntos de interes: ",
#         "results":results
#     }

#     return jsonify(response_body), 200

# @api.route('/Interest_point/<int:id>', methods=['GET'])
# def one_interest_point(id):
   
#  try:

#     interest_point = db.session.execute(select(Interest_point).filter_by(id=id)).scalar_one()
   
#     response_body = {
#         "msg": "Hola, aqui esta el punto de interes que buscas ",
#         "results":interest_point.serialize()
#     }


#     return jsonify(response_body), 200

#  except:

#     return jsonify({"msg":"Interest point not exist"}), 404



# # _________# Gets Hotel _________


# @api.route('/Hotel', methods=['GET'])
# def todos_los_hoteles():


#     data = db.session.scalars(select(Hotel)).all()
#     results = list(map(lambda Hotel: Hotel.serialize(),data))
   
#     response_body = {
#         "msg": "Hola, aqui tienes la lista de todos los hoteles: ",
#         "results":results
#     }

#     return jsonify(response_body), 200

# @api.route('/Hotel/<int:id>', methods=['GET'])
# def solo_un_hotel(id):
   
#  try:

#     hotel = db.session.execute(select(Hotel).filter_by(id=id)).scalar_one()
   
#     response_body = {
#         "msg": "Hola, aqui esta el hotel  que buscas ",
#         "results":hotel.serialize()
#     }


#     return jsonify(response_body), 200

#  except:

#     return jsonify({"msg":"Hotel not exist"}), 404




# # Get Favorites _________



# @api.route('/Favorites', methods=['GET'])
# def todos_los_favoritos():


#     data = db.session.scalars(select(Favorites)).all()
#     results = list(map(lambda Favorites: Favorites.serialize(),data))
   
#     response_body = {
#         "msg": "Hola, aqui tienes la lista de todos los favoritos: ",
#         "results":results
#     }
#     return jsonify(response_body), 200



# #  Metodos post______

# # CITY
# @api.route('/favorite/City/<int:city_id>', methods=['POST'])
# def agregar_ciudad_favorita(city_id):
#     # Obtener el user_id desde el request (se recomienda que venga en el JSON)
#     data = request.get_json()
#     user_id = data.get('user_id')

#     if not user_id:
#         return jsonify({"msg": "User ID is required"}), 400

#     # Verificar que el usuario existe
#     user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one_or_none()
#     if not user:
#         return jsonify({"msg": "User not found"}), 404

#     # Crear el favorito y asignar la ciudad
#     new_favorito = Favorites(user_id=user.id, city_id=city_id)
#     db.session.add(new_favorito)
#     db.session.commit()

#     return jsonify({"msg": "Ciudad favorita agregada"}), 201


# # Restaurant
# @api.route('/favorite/Restaurant/<int:restaurant_id>', methods=['POST'])
# def agregar_restaurant_favorito(restaurant_id):
#     # Obtener el user_id desde el request (se recomienda que venga en el JSON)
#     data = request.get_json()
#     user_id = data.get('user_id')

#     if not user_id:
#         return jsonify({"msg": "User ID is required"}), 400

#     # Verificar que el usuario existe
#     user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one_or_none()
#     if not user:
#         return jsonify({"msg": "User not found"}), 404

#     # Crear el favorito y asignar la ciudad
#     new_favorito = Favorites(user_id=user.id, restaurant_id=restaurant_id)
#     db.session.add(new_favorito)
#     db.session.commit()

#     return jsonify({"msg": "Ciudad favorita agregada"}), 201

# # Interest_point
# @api.route('/favorite/Interest_point/<int:interest_point_id>', methods=['POST'])
# def agregar_interest_point_favorito(interest_point_id):
#     # Obtener el user_id desde el request (se recomienda que venga en el JSON)
#     data = request.get_json()
#     user_id = data.get('user_id')

#     if not user_id:
#         return jsonify({"msg": "User ID is required"}), 400

#     # Verificar que el usuario existe
#     user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one_or_none()
#     if not user:
#         return jsonify({"msg": "User not found"}), 404

#     # Crear el favorito y asignar la ciudad
#     new_favorito = Favorites(user_id=user.id, interest_point_id=interest_point_id)
#     db.session.add(new_favorito)
#     db.session.commit()

#     return jsonify({"msg": "Ciudad favorita agregada"}), 201

# # Hotel
# @api.route('/favorite/Hotel/<int:hotel_id', methods=['POST'])
# def agregar_hotel_favorito(hotel_id):
#     # Obtener el user_id desde el request (se recomienda que venga en el JSON)
#     data = request.get_json()
#     user_id = data.get('user_id')

#     if not user_id:
#         return jsonify({"msg": "User ID is required"}), 400

#     # Verificar que el usuario existe
#     user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one_or_none()
#     if not user:
#         return jsonify({"msg": "User not found"}), 404

#     # Crear el favorito y asignar el hotel 
#     new_favorito = Favorites(user_id=user.id, hotel_id=hotel_id)
#     db.session.add(new_favorito)
#     db.session.commit()

#     return jsonify({"msg": "Ciudad favorita agregada"}), 201


# DELETE 

#City

# @api.route('/favorite/city/<int:city_id>', methods=['DELETE'])
# def delete_city(city_id):

#     user = db.session.execute(db.select(User).filter_by(id=id)).scalar_one()
#     # hacer filtrado
#     if not user:
#         return jsonify({"msg": "User not found"}), 404

#     buscar_cityfavorito_borrar = Favorites(user_id=user.id,city_id=city_id)
#     db.session.delete(buscar_cityfavorito_borrar)
#     db.session.commit()

#     response_body = {
#         "msg":"Ciudad favorita del usuario deleted"
#     }

#     return jsonify(response_body), 200

#Restaurant
# @api.route('/favorite/restaurant/<int:restaurant_id>', methods=['DELETE'])
# def delete_restaurant(restaurant_id):

#     user = db.session.execute(db.select(User).filter_by(id=id)).scalar_one()
#     # hacer filtrado
#     if not user:
#         return jsonify({"msg": "User not found"}), 404

#     buscar_restaurantfavorito_borrar = Favorites(user_id=user.id,restaurant_id=restaurant_id)
#     db.session.delete(buscar_restaurantfavorito_borrar)
#     db.session.commit()

#     response_body = {
#         "msg":"Restaurant favorita del usuario deleted"
#     }

#     return jsonify(response_body), 200


#Interest_point
# @api.route('/favorite/interest_point/<int:interest_point_id>', methods=['DELETE'])
# def delete_interest_point(interest_point_id):

#     user = db.session.execute(db.select(User).filter_by(id=id)).scalar_one()
#     # hacer filtrado
#     if not user:
#         return jsonify({"msg": "User not found"}), 404

#     buscar_interestpointfavorito_borrar = Favorites(user_id=user.id,interest_point_id=interest_point_id)
#     db.session.delete(buscar_interestpointfavorito_borrar)
#     db.session.commit()

#     response_body = {
#         "msg":"Restaurant favorita del usuario deleted"
#     }

#     return jsonify(response_body), 200


#Hotel
# @api.route('/favorite/hotel/<int:hotel_id>', methods=['DELETE'])
# def delete_restaurant(hotel_id):

#     user = db.session.execute(db.select(User).filter_by(id=id)).scalar_one()
#     # hacer filtrado
#     if not user:
#         return jsonify({"msg": "User not found"}), 404

#     buscar_hotel_borrar = Favorites(user_id=user.id,hotel_id=hotel_id)
#     db.session.delete(buscar_hotel_borrar)
#     db.session.commit()

#     response_body = {
#         "msg":"Hotel favorita del usuario deleted"
#     }

#     return jsonify(response_body), 200

    

     
#ENDPOINT PROTEGIDO 
# Proteger una ruta con jwt_required, que eliminará las solicitudes
# sin un JWT válido presente.
@api.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200  


