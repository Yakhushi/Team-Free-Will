#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Your_SSID";
const char* password = "Your_PASSWORD";
const char* server = "http://YOUR_PUBLIC_IP/upload";

int micPin = 34;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) delay(500);
}

void loop() {
  int raw = analogRead(micPin);
  float dB = map(raw, 0, 4095, 30, 120);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(server);
    http.addHeader("Content-Type", "application/json");
    String data = "{\"location\":\"Block A\",\"dB\":" + String(dB) + "}";
    http.POST(data);
    http.end();
  }

  delay(5000);
}
