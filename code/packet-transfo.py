import struct
from time import time, sleep
from SX127x.LoRa import *
from SX127x.board_config import BOARD

# Initialize LoRa board
BOARD.setup()

class LoRaSender(LoRa):
    def __init__(self, verbose=False):
        super(LoRaSender, self).__init__(verbose)
        self.set_mode(MODE.STDBY)
        self.set_pa_config(pa_select=1)
        self.set_dio_mapping([0] * 6)
    
    def send_packet(self, data_bytes):
        self.write_payload(data_bytes)
        self.set_mode(MODE.TX)
        print("Sending packet...")

try:
    lora = LoRaSender(verbose=False)
    lora.set_freq(915.0)
    lora.set_tx_power(14)

    packet_id = 0
    while True:
        # Sample data (replace with real sensor reads)
        timestamp = int(time())
        temperature = int(25.34 * 100)  # 0.01 °C units
        humidity = int(45.67 * 100)     # 0.01% units
        pressure = 101325               # Pa
        air_quality = 400               # eCO2 ppm
        tvoc = 15                      # ppb
        battery_level = 85             # %
        flags = 0x00                   # status bits

        # Pack data same way as C struct (little endian)
        packet = struct.pack(
            '<B I h H i H H B B',
            packet_id,
            timestamp,
            temperature,
            humidity,
            pressure,
            air_quality,
            tvoc,
            battery_level,
            flags
        )

        lora.send_packet(packet)
        print(f"Sent packet id {packet_id}")
        packet_id = (packet_id + 1) % 256

        sleep(5)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    BOARD.teardown()
