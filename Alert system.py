from flask import Flask, request, jsonify
from datetime import datetime
import csv

app = Flask(__name__)
alert_threshold = 75  # dB value that triggers a security alert
log_file = "security_alerts.csv"

@app.route('/alert', methods=['POST'])
def handle_alert():
    data = request.get_json()
    timestamp = datetime.now().isoformat()
    dB = float(data.get("dB", 0))
    location = data.get("location", "Unknown")

    if dB > alert_threshold:
        print(f"[ALERT] {timestamp} - Noise at {location}: {dB} dB")
        notify_security(location, dB)
        log_alert(timestamp, location, dB)

    return jsonify({"status": "received", "dB": dB})

def log_alert(timestamp, location, dB):
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, location, dB])

def notify_security(location, dB):
    # Simulated action (could be SMS, Telegram Bot, walkie-talkie integration, etc.)
    print(f">>> Notifying security: Excessive noise at {location} ({dB} dB)")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
