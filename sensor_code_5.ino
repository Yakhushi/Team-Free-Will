const int micPin = 34;      // Analog input from sound sensor
const int ledPin = 14;      // Red LED output
int threshold = 85;         // dB limit for visual alert

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int raw = analogRead(micPin);  // Read analog value
  float dB = map(raw, 0, 4095, 30, 120);  // Approximate conversion to dB

  Serial.print("Sound Level (dB): ");
  Serial.println(dB);

  if (dB > threshold) {
    digitalWrite(ledPin, HIGH);  // Turn on LED
  } else {
    digitalWrite(ledPin, LOW);   // Turn off LED
  }

  delay(1000);  // Read every second
}

