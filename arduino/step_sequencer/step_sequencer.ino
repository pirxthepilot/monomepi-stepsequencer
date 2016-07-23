#include <Servo.h>

Servo s4, s5, s6, s7, s8, s9, s10, s11;

const int initpos = 80; // initial servo position
byte b[] = {0x00, 0x00, 0x00};

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

  Serial.begin(115200); 
}

void loop() 
{ 

  if (Serial.available()) {

    Serial.readBytes(b, 2);
    int servo_id = b[0];
    if (servo_id == 4) { 
      //dlyCat = (b[1] << 8) + b[2];
      runS4((unsigned char)(b[1]));
    }
    if (servo_id == 5) { 
      //dlyCat = (b[1] << 8) + b[2];
      runS5((unsigned char)(b[1]));
    }

  }

}

void runS4(int pos)
{
  s4.write(pos);
}

void runS5(int pos)
{
  s5.write(pos);
}

void runS6(int pos)
{
  s6.write(pos);
}
