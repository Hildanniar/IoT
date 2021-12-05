#include <Wire.h>
#include <LiquidCrystal_I2C.h>
float trigPin = 11;
float echoPin = 10;
LiquidCrystal_I2C lcd(0x27,16,2);
void setup()
{
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  lcd.init();
}
void loop()
{
  lcd.backlight();
  int duration, distance;
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance =(duration/2)/29,4117647;
  lcd.setCursor(0,0);
  lcd.print("Jarak Benda");
  lcd.setCursor(0,1);
  lcd.print("= ");
  lcd.print(distance);
  lcd.print("cm");
  delay(1000);
}
