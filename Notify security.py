import requests

def notify_security(location, dB):
    print(f">>> Notifying security: Excessive noise at {location} ({dB} dB)")
    
    # Construct API request
    patrol_api = "https://campus-patrol.com/api/patrol-request"
    headers = {
        "Authorization": "Bearer YOUR_API_TOKEN",
        "Content-Type": "application/json"
    }
    payload = {
        "location": location,
        "issue": f"Excessive noise detected: {dB:.1f} dB",
        "priority": "High"
    }

    try:
        response = requests.post(patrol_api, headers=headers, json=payload)
        if response.status_code == 200:
            print("✅ Patrol system notified successfully.")
        else:
            print(f"⚠️ Failed to notify patrol system. Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Error notifying patrol system: {e}")

