#include <Wire.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
const int pulsePin = A0;

void setup() {
  Serial.begin(9600);
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("Error con OLED"));
    while(true);
  }
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0,0);
  display.println("Sistema BioPulse AI");
  display.display();
}

void loop() {
  int pulseValue = analogRead(pulsePin);
  Serial.println(pulseValue);
  display.clearDisplay();
  display.setCursor(0,0);
  display.println("Pulso en tiempo real:");
  display.setCursor(0,10);
  display.println(pulseValue);
  display.display();
  delay(100);
}
