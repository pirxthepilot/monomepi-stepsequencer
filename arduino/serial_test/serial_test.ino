#include <Servo.h>

Servo myservo;

const int servoPin = 3;
const int ledPins[] = {8, 9, 10, 11, 12};
const int initpos = 90; // initial servo position

byte b[] = {0x00, 0x00};
unsigned long dlyCat;


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
    //runServo(Serial.read() - '0');
    //runLed(Serial.read() - '0');
    //runServo('10');
    //b = Serial.read();
    Serial.readBytes(b, 2);
    runServo(char(b[0]), int(b[1]));
    //dlyCat = ((unsigned long)(b[1]) << 8) | b[2];
    //runServo(char(b[0]), char(dlyCat));
  }
  //delay(10);
}

void runLed(int n)
{
  digitalWrite(ledPins[n], HIGH);
  delay(1000);
  digitalWrite(ledPins[n], LOW);
}

void runServo(int pos, int dur)
{
  myservo.write(pos);
  delay(dur);
}

void blink() {
  digitalWrite(ledPins[0], HIGH);
  delay(100);
  digitalWrite(ledPins[0], LOW);
  delay(100);
}
