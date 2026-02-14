import serial
import pandas as pd

ser = serial.Serial('COM3', 115200)  # Change COM port
data_list = []

print("Collecting data... Press Ctrl+C to stop.")

try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        print("Received:", line)
        values = line.split(",")

        if len(values) == 3:
            temp = float(values[0])
            hr = int(values[1])
            act = int(values[2])

            data_list.append([temp, hr, act])

except KeyboardInterrupt:
    df = pd.DataFrame(data_list, columns=["Temperature", "HeartRate", "Activity"])
    df.to_csv("animal_data.csv", index=False)
    print("Data saved to animal_data.csv")
