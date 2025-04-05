#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";

// Change to your Flask endpoint or ngrok HTTPS URL
const char* serverUrl = "http://your-server-ip-or-ngrok-url/upload";

// Microphone analog pin
const int micPin = 34;  // Change if you're using ESP8266 or different pin

void setup() {
  Serial.begin(115200);
  delay(1000);

  // Connect to WiFi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected to WiFi");
}

void loop() {
  int soundReading = analogRead(micPin);

  // Convert raw reading to approximate decibel (rough estimation)
  // Max analogRead is 4095 for ESP32
  float voltage = soundReading * (3.3 / 4095.0);
  float decibel = voltage * 100;  // Simple scaling

  Serial.print("Analog: ");
  Serial.print(soundReading);
  Serial.print(" | Voltage: ");
  Serial.print(voltage);
  Serial.print(" V | Decibel: ");
  Serial.println(decibel);

  // Send to server
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");

    String json = "{\"decibel\": " + String(decibel, 2) + ", \"location\": \"Hostel Block A\"}";
    int httpResponseCode = http.POST(json);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.print("Server response: ");
      Serial.println(response);
    } else {
      Serial.print("Error sending POST: ");
      Serial.println(http.errorToString(httpResponseCode));
    }

    http.end();
  } else {
    Serial.println("WiFi disconnected!");
  }

  delay(5000);  // Send every 5 seconds
}

