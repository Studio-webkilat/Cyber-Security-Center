from flask import Flask, jsonify, send_from_directory
import json
import os

app = Flask(__name__)

# Route untuk file index.html
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Route untuk mengambil data audit (API)
@app.route('/api/audit')
def get_audit_data():
    if os.path.exists('report.json'):
        with open('report.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    else:
        return jsonify({"error": "Data belum tersedia"}), 404

if __name__ == '__main__':
    print("Server berjalan di http://127.0.0.1:5000")
    app.run(debug=True, port=5000)

