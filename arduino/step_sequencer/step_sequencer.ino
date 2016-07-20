#include <Servo.h>

Servo s4, s5, s6, s7, s8, s9, s10, s11;

const int initpos = 80; // initial servo position
byte b[] = {0x00, 0x00, 0x00};
int dlyCat;
unsigned long s4timer;
unsigned long s5timer;
unsigned long s6timer;
unsigned long s7timer;
unsigned long s8timer;
unsigned long s9timer;
unsigned long s10timer;
unsigned long s11timer;

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
    
    Serial.readBytes(b, 3);
 
    dlyCat = (b[1] << 8) + b[2];
    if ((millis() - s4timer) >= dlyCat ) {
      runS4((unsigned char)(b[0]), dlyCat);
    }
  }

}

void runS4(int pos, int dur)
{
  s4.write(pos);
  s4timer = millis();
}

void runS5(int pos, int dur)
{
  s5.write(pos);
  s5timer = millis();
}
