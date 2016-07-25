#include <Servo.h>

Servo s4, s5, s6, s7, s8, s9, s10, s11;

const int initpos = 80; // initial servo position
const int hitpos = 120; // hit position
const int hitdly = 100; // hit delay in millisecs
byte b[] = {0x00};
unsigned long s4start = 0;
unsigned long s5start = 0;
boolean s4run = false;
boolean s5run = false;

void setup() 
{
  s4.attach(4);
  s4.write(initpos);
  s5.attach(5);
  s5.write(initpos);
  s6.attach(6);
  s6.write(initpos);
  s7.attach(7);
  s7.write(initpos);
  s8.attach(8);
  s8.write(initpos);
  s9.attach(9);
  s9.write(initpos);
  s10.attach(10);
  s10.write(initpos);
  s11.attach(11);
  s11.write(initpos);

  Serial.begin(57600); 
}

void loop() 
{ 

  unsigned long curtime = millis();

  if (Serial.available()) {

    Serial.readBytes(b, 1);
    int servo_id = b[0];

    if (servo_id == 0) {
      s4.write(hitpos);
      s4start = millis();
      s4run = true;
    } else if (servo_id == 1) {
      s5.write(hitpos);
      s5start = millis();
      s5run = true;     
    }

  }

  if (s4run) {
    if ((curtime - s4start) >= hitdly) {
      s4.write(initpos);
      s4start = 0;
      s4run = false;
    }
  }
  if (s5run) {
    if ((curtime - s5start) >= hitdly) {
      s5.write(initpos);
      s5start = 0;
      s5run = false;
    }
  }

}
