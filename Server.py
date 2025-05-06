from flask import Flask, jsonify
import json

app = Flask(__name__)

# Baca data dari file JSON
with open("starlink_data.json", "r") as f:
    data = json.load(f)

@app.route("/")
def home():
    return "<h2>API Satelit Starlink</h2><p>Akses data di endpoint /data</p>"

@app.route("/data")
def get_data():
    return jsonify(data)

@app.route("/data/<int:index>")
def get_data_by_index(index):
    if 0 <= index < len(data):
        return jsonify(data[index])
    else:
        return jsonify({"error": "Index tidak valid"}), 404

if __name__ == "__main__":
    app.run(debug=True)





