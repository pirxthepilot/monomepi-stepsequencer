#include <Servo.h>

Servo myservo;

const int servoPin = 3;
const int ledPins[] = {8, 9, 10, 11, 12};
const int initpos = 80; // initial servo position

byte b[] = {0x00, 0x00, 0x00};
int dlyCat;


void setup() 
{
  pinMode(servoPin, OUTPUT);
  for (int i = 0; i < 5; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
  myservo.attach(servoPin);
  myservo.write(initpos);
  Serial.begin(115200); 
}


void loop() 
{ 
  if (Serial.available()) {
    //blink();
    //runLed(Serial.read() - '0');
    //b = Serial.read();
    Serial.readBytes(b, 3);
    dlyCat = (b[1] << 8) + b[2];
    runServo((unsigned char)(b[0]), dlyCat);
    //runServo(char(b[0]), int(b[1]));
  }
  //delay(10);
}

void runServo(int pos, int dur)
{
  myservo.write(pos);
  delay(dur);
}

void runLed(int n)
{
  digitalWrite(ledPins[n], HIGH);
  delay(1000);
  digitalWrite(ledPins[n], LOW);
}

void blink() {
  digitalWrite(ledPins[0], HIGH);
  delay(50);
  digitalWrite(ledPins[0], LOW);
  delay(50);
}
