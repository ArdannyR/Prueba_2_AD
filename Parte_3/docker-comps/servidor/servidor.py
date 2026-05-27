from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SERVICIOS = {
    "URL_CREATE": "http://suma:5001/create",
    "URL_READ": "http://suma:5002/read",
    "URL_UPDATE": "http://suma:5003/update",
    "URL_DELETE": "http://suma:5004/delete"
}

usuarios = {} # id_usuario: {nombre: str, edad: int}

@app.route("/create", methods=["POST"])
def create_usuario():
    data = request.json
    accion = data.get("accion")
    id_usuario = data.get("id_usuario")
    nombre = data.get("nombre")
    edad = data.get("edad")

    if accion not in SERVICIOS:
        return jsonify({"error": "Acción no válida"}), 400
    
    if not id_usuario or not nombre or not edad:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    if id_usuario in usuarios:
        return jsonify({"error": "El usuario ya existe"}), 400

    respuesta = requests.post(
        SERVICIOS[accion], 
        json={"id_usuario": id_usuario, "nombre": nombre, "edad": edad}
    )
    return jsonify({"message": "Usuario creado exitosamente"}), 201




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# el comando docker-compose up --build va desde la carpeta a nivel de docker-compose.yml
# en postman esto se prueba como http://localhost:5000/user/create

# {
#     "id_usuario": "1",
#     "nombre": "Ardanny",
#     "edad": "21"
# }
