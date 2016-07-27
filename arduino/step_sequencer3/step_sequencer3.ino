#include <Servo.h>

Servo s[8];

const int initpos = 80; // initial servo position
const int hitpos = 50; // hit position
const long hitdly = 100; // hit delay in millisecs
byte b[] = {0x00};
unsigned long servo_start[8] = {0, 0, 0, 0, 0, 0, 0, 0};
boolean is_running[8] = {false, false, false, false, false, false, false, false};

void setup() 
{
  s[0].attach(4);
  s[0].write(initpos);
  s[1].attach(5);
  s[1].write(initpos);
  s[2].attach(6);
  s[2].write(initpos);
  s[3].attach(7);
  s[3].write(initpos);
  s[4].attach(8);
  s[4].write(initpos);
  s[5].attach(9);
  s[5].write(initpos);
  s[6].attach(10);
  s[6].write(initpos);
  s[7].attach(11);
  s[7].write(initpos);
  //pinMode(13, OUTPUT);

  Serial.begin(115200); 
}

void loop() 
{

  if (Serial.available()) {

    Serial.readBytes(b, 1);
    int servodata = b[0];

    for (int i = 0; i < 8; i++) {
      if (bitRead(servodata,i) == 1) {
        s[i].write(hitpos);
        //digitalWrite(13, HIGH);
        servo_start[i] = millis();
        is_running[i] = true;
      }
    }

  }

  for (int i = 0; i < 8; i++) {
    unsigned long curtime = millis();
    if (is_running[i]) {
      if ((curtime - servo_start[i]) >= hitdly) {
        //digitalWrite(13, LOW);
        s[i].write(initpos);
        servo_start[i] = 0;
        is_running[i] = false;
      }
    }
  }

}
