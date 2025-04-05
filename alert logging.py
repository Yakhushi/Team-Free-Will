from flask import Flask, request, jsonify
from datetime import datetime
import csv

app = Flask(__name__)
log_file = "zone_violations.csv"

@app.route('/zone-alert', methods=['POST'])
def zone_alert():
    data = request.get_json()
    zone = data.get("zone", "unknown")
    dB = float(data.get("dB", 0))
    time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{time_str}] ALERT in {zone} | {dB:.1f} dB")
    log_violation(time_str, zone, dB)

    # Add notification logic here if needed (e.g., SMS, app)
    return jsonify({"status": "alert received"})

def log_violation(timestamp, zone, dB):
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, zone, dB])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

