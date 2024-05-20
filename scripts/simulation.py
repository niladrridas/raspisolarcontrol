import requests
import random
import time

# Ubidots authentication token
TOKEN = 'BBUS-ml1LT3jGgdBozuHKmwo0J3CaQJzwxb'

# Device label and variable names
DEVICE_LABEL = 'raspi-solar-control'
VARIABLE_TEMPERATURE = 'temperature'
VARIABLE_HUMIDITY = 'humidity'

# Function to generate simulated sensor data
def generate_sensor_data():
    temperature = round(random.uniform(20, 30), 2)  # Simulate temperature readings between 20°C and 30°C
    humidity = round(random.uniform(40, 60), 2)     # Simulate humidity readings between 40% and 60%
    return temperature, humidity

# Function to send data to Ubidots
def send_data_to_ubidots(temperature, humidity):
    data = {
        VARIABLE_TEMPERATURE: temperature,
        VARIABLE_HUMIDITY: humidity
    }
    url = f'https://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_LABEL}'
    headers = {'X-Auth-Token': TOKEN, 'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Data sent successfully to Ubidots!")
    else:
        print("Failed to send data to Ubidots.")
        print("Error:", response.text)

# Main loop to generate and send simulated data
while True:
    temperature, humidity = generate_sensor_data()
    send_data_to_ubidots(temperature, humidity)
    time.sleep(5)  # Adjust the interval as needed
