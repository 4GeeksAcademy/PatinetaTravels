"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

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
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    # Verificar si el usuario ya existe
    user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one_or_none()

    if user:
        return jsonify({"msg": "El usuario ya existe"}), 400


    # Crear nuevo usuario
    new_user = User(email=email, password=password, is_active=True) 
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
        user = User.query.filter_by(email=email).first()
        print(User)
        if user is None:
           return jsonify({"msg": "Email not found "}), 401   

        if email == user.email or password == user.password:
           access_token = create_access_token(identity=email)    
           return jsonify(access_token=access_token), 200
        else:
            return jsonify({"msg": "bad email or password"}), 401 

    
    

     
#ENDPOINT PROTEGIDO 
# Proteger una ruta con jwt_required, que eliminará las solicitudes
# sin un JWT válido presente.
@api.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200  
