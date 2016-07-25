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
    if (servo_id == 0) {
      //dlyCat = (b[1] << 8) + b[2];
      //runS4((unsigned char)(b[1]));
      s4.write((unsigned char)(b[1]));
    } else if (servo_id == 1) {
      s5.write((unsigned char)(b[1]));
    } else if (servo_id == 2) {
      s6.write((unsigned char)(b[1]));
    } else if (servo_id == 3) {
      s7.write((unsigned char)(b[1]));
    } else if (servo_id == 4) {
      s8.write((unsigned char)(b[1]));
    } else if (servo_id == 5) {
      s9.write((unsigned char)(b[1]));
    } else if (servo_id == 6) {
      s10.write((unsigned char)(b[1]));
    } else if (servo_id == 7) {
      s11.write((unsigned char)(b[1]));
    }

  }

}
