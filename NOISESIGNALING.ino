	const int soundPin = A0;
const int greenLED = 8;
const int yellowLED = 9;
const int redLED = 10;

void setup() {
  Serial.begin(9600);
  pinMode(soundPin, INPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(yellowLED, OUTPUT);
  pinMode(redLED, OUTPUT);
}

void loop() {
  int soundValue = analogRead(soundPin);
  float voltage = soundValue * (5.0 / 1023.0);
  float db = map(soundValue, 0, 1023, 30, 100);  // Approximate range

  Serial.print("Sound Level (approx): ");
  Serial.print(db);
  Serial.println(" dB");

  if (db < 60) {
    digitalWrite(greenLED, HIGH);
    digitalWrite(yellowLED, LOW);
    digitalWrite(redLED, LOW);
  } else if (db < 80) {
    digitalWrite(greenLED, LOW);
    digitalWrite(yellowLED, HIGH);
    digitalWrite(redLED, LOW);
  } else {
    digitalWrite(greenLED, LOW);
    digitalWrite(yellowLED, LOW);
    digitalWrite(redLED, HIGH);
  }

  delay(200);
}