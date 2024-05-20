# main.py

import time
from sensors import TemperatureSensor, HumiditySensor
from controllers import SolarController

def main():
    # Initialize sensors
    temperature_sensor = TemperatureSensor(pin=4)
    humidity_sensor = HumiditySensor(pin=5)
    
    # Initialize controller
    solar_controller = SolarController()

    while True:
        # Read sensor values
        temperature = temperature_sensor.read_value()
        humidity = humidity_sensor.read_value()

        # Control solar system based on sensor data
        solar_controller.control_system(temperature, humidity)

        # Log sensor data
        log_sensor_data(temperature, humidity)

        # Wait for next iteration
        time.sleep(60)  # Sampling interval of 60 seconds

def log_sensor_data(temperature, humidity):
    # Log sensor data to CSV file
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("data/sensor_data.csv", "a") as f:
        f.write(f"{timestamp},{temperature},{humidity}\n")

if __name__ == "__main__":
    main()
