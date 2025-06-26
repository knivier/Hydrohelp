# Code Structure Overview

## 1. Packet Sending (Home Module)
- **Language:** C++ or Python (undecided, both implemented)
- **Function:** Collects sensor data and sends packets (JSON or binary format)

## 2. Packet Receiving (`receiver.py`)
- **Function:** Receives packets via LORA
- **Action:** Dumps received data into a JSON log file

## 3. Dashboard Update (`dashboard.py`)
- **Function:** Reads the latest JSON log
- **Action:** Updates the dashboard with new sensor data

**Flow:**  
Sensor Data → Packet Sender (Home Module) → LORA → `receiver.py` (JSON log) → `dashboard.py` (Dashboard Update)

> **Note**:
The OLED display on the home module will be updated through receiver.py. 