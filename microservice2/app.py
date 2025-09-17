from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # ✅ allow frontend requests

@app.route("/api/hello")
def hello():
    return jsonify({
        "service": "microservice2",
        "message": "Hello from Flask!"
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)

