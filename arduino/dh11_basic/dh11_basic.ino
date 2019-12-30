
#include <SimpleDHT.h>

#define DHTPIN 8
#define READ_DELAY 4900

/*
 * A basic temperature sensor
 * 
 * Required libraries: 
 *   - Simple DHT - https://github.com/winlinvip/SimpleDHT
 */

SimpleDHT11 dht11(DHTPIN);

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  byte h = 0;
  byte t = 0;

  int err;

  if ((err = dht11.read(&t, &h, NULL)) != SimpleDHTErrSuccess)  {
    // Errors will be detectable with a line starting with `e,`
    Serial.print("e,");
    Serial.print(err);
    Serial.print("\n");
  } else {
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.print((int) t);
    Serial.print(",");
    Serial.print((int) h);
    Serial.print("\n");
    delay(100);
    digitalWrite(LED_BUILTIN, LOW);
  }
  delay(READ_DELAY);
}
