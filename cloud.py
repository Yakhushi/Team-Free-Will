
from flask import Flask, request, jsonify
from datetime import datetime
import csv

app = Flask(__name__)
csv_file = "noise_data.csv"

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    data['timestamp'] = datetime.now().isoformat()

    with open(csv_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([data['timestamp'], data['location'], data['dB']])
    
    return jsonify({"status": "saved"})

@app.route('/data', methods=['GET'])
def fetch_data():
    rows = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for r in reader:
            rows.append({"timestamp": r[0], "location": r[1], "dB": float(r[2])})
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
