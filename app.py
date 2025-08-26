import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

# Serve React build from frontend/build
app = Flask(__name__, static_folder="frontend/build", static_url_path="")
CORS(app)

# API route
@app.route("/api/message")
def message():
    return jsonify({"message": "Hello from Flask + React on Render!"})

# Serve React frontend
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")

# Entry point for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
