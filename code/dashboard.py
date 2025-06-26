import json, os, time
import tkinter as tk
from tkinter import ttk

DATA_FILE = "latest.json"

def read_json():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        return None

def update_gui():
    data = read_json()
    if data:
        packet_id_var.set(data['packet_id'])
        timestamp_var.set(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data['timestamp'])))
        temp_var.set(f"{data['temperature_c']:.2f} °C")
        hum_var.set(f"{data['humidity_percent']:.2f} %")
        pres_var.set(f"{data['pressure_pa']} Pa")
        eco2_var.set(f"{data['eco2_ppm']} ppm")
        tvoc_var.set(f"{data['tvoc_ppb']} ppb")
        batt_var.set(f"{data['battery_percent']} %")
        flags_var.set(f"{bin(data['flags'])}")
        updated_var.set(time.strftime('%H:%M:%S', time.localtime(data['received_at'])))

    root.after(1000, update_gui)

# GUI
root = tk.Tk()
root.title("HydroHelp Dashboard (Live)")

labels = {
    'Packet ID': tk.StringVar(),
    'Timestamp': tk.StringVar(),
    'Temperature': tk.StringVar(),
    'Humidity': tk.StringVar(),
    'Pressure': tk.StringVar(),
    'eCO2': tk.StringVar(),
    'TVOC': tk.StringVar(),
    'Battery': tk.StringVar(),
    'Flags': tk.StringVar(),
    'Last Updated': tk.StringVar()
}

row = 0
for label, var in labels.items():
    ttk.Label(root, text=label+":").grid(column=0, row=row, sticky=tk.W, padx=5, pady=2)
    ttk.Label(root, textvariable=var).grid(column=1, row=row, sticky=tk.W, padx=5, pady=2)
    row += 1

# Assign vars
packet_id_var = labels['Packet ID']
timestamp_var = labels['Timestamp']
temp_var = labels['Temperature']
hum_var = labels['Humidity']
pres_var = labels['Pressure']
eco2_var = labels['eCO2']
tvoc_var = labels['TVOC']
batt_var = labels['Battery']
flags_var = labels['Flags']
updated_var = labels['Last Updated']

update_gui()
root.mainloop()
