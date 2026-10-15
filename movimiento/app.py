from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

CODIGOS = {
    "adelante": "01",
    "atras": "02",
    "izquierda": "03",
    "derecha": "04",
    "detener": "05",
}

@app.get("/api/movimientos")
def listar():
    return jsonify(CODIGOS)

@app.post("/api/mover")
def mover():
    data = request.get_json(silent=True) or {}
    orden = str(data.get("orden", "")).strip().lower().replace("á", "a")

    if orden not in CODIGOS:
        return jsonify({"error": "Orden no válida", "validas": list(CODIGOS)}), 400

    return jsonify({"orden": orden, "codigo": CODIGOS[orden]})

if __name__ == "__main__":
    app.run(port=5001, debug=True)