#include <XBee.h>
#include <SimpleDHT.h>

#define DHTPIN 8
#define READ_DELAY 5000

XBee xbee = XBee();
SimpleDHT11 dht11(DHTPIN);

uint8_t payload[] = { 0, 0, 0, 0 };
Tx16Request tx = Tx16Request(0x5001, payload, sizeof(payload));

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
  Serial.begin(9600);
  xbee.setSerial(Serial);
}

void loop() {
  delay(READ_DELAY);

  byte h = 0;
  byte t = 0;

  int err = dht11.read(&t, &h, NULL);

  if (err != SimpleDHTErrSuccess)  {
    payload[0] = 'e';
    payload[1] = (int8_t)err;
    payload[2] = 0;
    payload[3] = 0;    
  } else {
    payload[0] = 0;
    payload[1] = 0;
    payload[2] = t;
    payload[3] = h;
  }
  
  // digitalWrite(LED_BUILTIN, HIGH);
  xbee.send(tx);
  // digitalWrite(LED_BUILTIN, LOW);
  
}
