import struct, json, time
from SX127x.LoRa import *
from SX127x.board_config import BOARD

OUTPUT_FILE = "latest.json"

def unpack_packet(data):
    try:
        unpacked = struct.unpack('<B I h H i H H B B', data)
        return {
            'packet_id': unpacked[0],
            'timestamp': unpacked[1],
            'temperature_c': unpacked[2] / 100.0,
            'humidity_percent': unpacked[3] / 100.0,
            'pressure_pa': unpacked[4],
            'eco2_ppm': unpacked[5],
            'tvoc_ppb': unpacked[6],
            'battery_percent': unpacked[7],
            'flags': unpacked[8],
            'received_at': int(time.time())
        }
    except Exception as e:
        print(f"Packet unpack failed: {e}")
        return None

class LoRaReceiver(LoRa):
    def __init__(self, verbose=False):
        super(LoRaReceiver, self).__init__(verbose)
        self.set_mode(MODE.STDBY)
        self.set_pa_config(pa_select=1)
        self.set_dio_mapping([0] * 6)

    def on_rx_done(self):
        self.clear_irq_flags(RxDone=1)
        payload = self.read_payload(nocheck=True)
        print(f"Received {len(payload)} bytes")
        if len(payload) == 19:
            data = unpack_packet(payload)
            if data:
                with open(OUTPUT_FILE, 'w') as f:
                    json.dump(data, f, indent=2)
                print("→ Packet logged to JSON.")
        else:
            print("Invalid packet size.")
        self.set_mode(MODE.RXCONT)

def main():
    BOARD.setup()
    try:
        lora = LoRaReceiver()
        lora.set_freq(915.0)
        lora.set_tx_power(14)
        lora.set_mode(MODE.RXCONT)
        print("LoRa listening...")
        while True:
            lora.handle_irq()
    except KeyboardInterrupt:
        print("Stopped.")
    finally:
        BOARD.teardown()

if __name__ == "__main__":
    main()
