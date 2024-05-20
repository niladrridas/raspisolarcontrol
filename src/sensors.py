# sensors.py

import random

class TemperatureSensor:
    def __init__(self, pin):
        self.pin = pin

    def read_value(self):
        # Simulate reading temperature value (replace with actual sensor reading)
        return round(random.uniform(20, 30), 2)

class HumiditySensor:
    def __init__(self, pin):
        self.pin = pin

    def read_value(self):
        # Simulate reading humidity value (replace with actual sensor reading)
        return round(random.uniform(40, 60), 2)
