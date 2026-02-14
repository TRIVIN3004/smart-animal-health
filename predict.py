import serial
import joblib
import pandas as pd

model = joblib.load("animal_health_model.pkl")
ser = serial.Serial('COM3', 115200)

print("Live Health Monitoring Started...")

while True:
    line = ser.readline().decode('utf-8').strip()
    values = line.split(",")

    if len(values) == 3:
        temp = float(values[0])
        hr = int(values[1])
        act = int(values[2])

        data = pd.DataFrame([[temp, hr, act]],
                            columns=["Temperature", "HeartRate", "Activity"])

        prediction = model.predict(data)[0]

        print(f"Temp: {temp} | HR: {hr} | Act: {act} → Health: {prediction}")
