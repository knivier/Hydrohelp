#include <LoRa.h>

// Packet structure
typedef struct {
    uint8_t  packet_id;
    uint32_t timestamp;
    int16_t  temperature;    // 0.01 °C
    uint16_t humidity;       // 0.01 %
    int32_t  pressure;       // Pa
    uint16_t air_quality;    // eCO2 ppm
    uint16_t tvoc;           // TVOC ppb
    uint8_t  battery_level;  // %
    uint8_t  flags;
} __attribute__((packed)) LoRaPacket;

LoRaPacket packet;
uint8_t packetCounter = 0;

void setup() {
  Serial.begin(115200);
  while (!Serial);

  // LoRa init (adjust pins for TTGO T-Beam)
  if (!LoRa.begin(915E6)) { // 915 MHz for US; change for your region
    Serial.println("LoRa init failed!");
    while (1);
  }
  Serial.println("LoRa init success.");
}

void loop() {
  // Simulate sensor readings:
  float temp_c = 25.34;     // Replace with AHT21.readTemperature()
  float hum = 45.67;        // Replace with AHT21.readHumidity()
  int32_t pressure_pa = 101325; // Replace with BME280.readPressure()
  uint16_t eco2 = 400;      // Replace with SGP30.getCO2()
  uint16_t tvoc = 15;       // Replace with SGP30.getTVOC()
  uint8_t battery = 85;     // Replace with ADC or battery monitor
  uint8_t flags =_
}