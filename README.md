# HydroHelp

**HydroHelp** is a solar-powered, waterproof weather station that uses LoRa telemetry to send real-time environmental data to a home base. The goal? Help people (me) remember to water the grass and also have an early asthma warning system while also learning embedded systems, sensors, CAD, and solar power along the way.

> **Note**: All MD documents are composed with the Obsidian text editor, and are best viewed by it :D

**Highway Organizers**: BOMs and CADs are found in their respective files (BOM.md and CADs in the CAD directory). I will not be putting them in this README as I want it as clean as possible.

## The "Problem" I'm trying to solve

I live in an area where construction dominates and there isn't a local weather station near me. Sure, the general Detroit/Ann Arbor Airport weather stations mostly work for weather and general information, but for some reason when it says it'll rain in A2, it doesn't rain in our city. Or when the pollution is all but none in A2, it's giving me an asthma attack back home. The purpose of this project is to bring weather telemetry a lot closer to me so I can get more UTD weather information while also being reminded to water the grass in the summer. Finally, it would be really nice to know if a certain time in the day poses a higher risk to my asthma than other days.

[BOM](https://github.com/knivier/Hydrohelp/blob/main/BOM.md), [CADs](https://github.com/knivier/Hydrohelp/tree/main/CADs)

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
- [x] Basic CAD layouts
- [ ] Project approved by Highway organizers
- [ ] Order components
- [ ] Prototype and test sensors
- [ ] Finish CAD and 3D print enclosure
- [ ] Build power and solar system
- [ ] Develop and test LoRa telemetry link
- [ ] Create home base interface (OLED + optional PC logging)
- [ ] Deploy on roof & field test
- [ ] Ship as a final product that's easy to replicate (my goal? make this entire setup easy for those that may want to replicate)
- [ ] Connect (in a separate project) Hydrohelp to an automatic water sprinkler hose attachment thing
