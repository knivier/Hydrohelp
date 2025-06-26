# HydroHelp

**HydroHelp** is a solar-powered, waterproof weather station that uses LoRa telemetry to send real-time environmental data to a home base. The goal? Help people (me) remember to water the grass but also learn embedded systems, sensors, CAD, and solar power along the way.

> **Note**: All MD documents are composed with the Obsidian text editor, and are best viewed by it :D

## 📡 Features
- Temp, humidity, pressure, and air quality monitoring (I have asthma so having a warning based AQM would be very nice)
- LoRa transmission between outdoor node and indoor base
- Solar-charged 18650 battery system (off-grid capable)
- Clock-based alerts if conditions suggest watering
- Compact OLED-based display for real-time data
- All housed in a weatherproof enclosure

## 💡 Technologies
- ESP32 (TTGO T-Beam)
- LoRa 433/868MHz
- AHT21, BMP280, MQ135 sensors (or similar, check BOM for last updated)
- CAD-designed housing
- Deep sleep power management

## 📦 Project Goals
- [x] Define feature set and hardware needs
- [x] Source components
- [ ] Order components
- [ ] Prototype and test sensors
- [ ] Finish CAD and 3D print enclosure
- [ ] Build power and solar system
- [ ] Develop and test LoRa telemetry link
- [ ] Create home base interface (OLED + optional PC logging)
- [ ] Deploy on roof & field test
- [ ] Ship as a final product that's easy to replicate (my goal? make this entire setup easy for those that may want to replicate)
- [ ] Connect (in a separate project) Hydrohelp to an automatic water sprinkler hose attachment thing