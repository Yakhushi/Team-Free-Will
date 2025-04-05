#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Your_SSID";
const char* password = "Your_PASSWORD";
const char* server = "http://YOUR_SERVER_IP/alert";  // alert endpoint

int micPin = 34;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  Serial.println("WiFi connected");
}

void loop() {
  int raw = analogRead(micPin);
  float dB = map(raw, 0, 4095, 30, 120);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(server);
    http.addHeader("Content-Type", "application/json");

    String data = "{\"location\":\"Library\",\"dB\":" + String(dB) + "}";
    int status = http.POST(data);
    Serial.print("POST status: "); Serial.println(status);
    http.end();
  }

  delay(5000); // Send every 5 seconds
}

