# RaspiSolarControl

RaspiSolarControl is a Raspberry Pi-based system for monitoring and controlling solar power generation and storage. It includes functionalities for interfacing with sensors, managing data, and controlling the solar system.

## Technologies Used

- ![Raspberry Pi Icon](https://img.icons8.com/color/48/000000/raspberry-pi.png) Raspberry Pi
- ![Python Icon](https://img.icons8.com/color/48/000000/python.png) Python
- ![SVG Icon](https://img.icons8.com/ios-filled/50/000000/svg.png) SVG Animation
- ![HTML Icon](https://img.icons8.com/color/48/000000/html-5.png) HTML
- ![CSS Icon](https://img.icons8.com/color/48/000000/css3.png) CSS
- ![JavaScript Icon](https://img.icons8.com/color/48/000000/javascript.png) JavaScript
- ![Git Icon](https://img.icons8.com/color/48/000000/git.png) Git
- ![GitHub Icon](https://img.icons8.com/ios-glyphs/30/000000/github.png) GitHub
- ![GreenSock Icon](https://www.gstatic.com/webp/gallery/2.png) GreenSock (GSAP) (Icon not available, so using placeholder)

## Animation

# RaspiSolarControl Automation Process

## Overview

This document outlines the automation process for the RaspiSolarControl project, from coding to deployment and output stages.

## Stages

### 1. Development

- **Coding**: Write Python scripts to interface with sensors, control the solar system, and log data.
- **Testing**: Conduct unit tests and integration tests to ensure the functionality of the code.
- **Version Control**: Use Git for version control, tracking changes, and collaboration.

### 2. Deployment

- **Hardware Setup**: Connect Raspberry Pi board with temperature and humidity sensors, as well as solar panels and batteries.
- **Script Installation**: Install Python dependencies and deploy the main script to the Raspberry Pi.

### 3. Operation

- **Sensor Monitoring**: Continuously monitor temperature and humidity levels using the sensors.
- **Solar System Control**: Dynamically control the solar system based on sensor data to optimize energy production and storage.
- **Data Logging**: Log sensor data to CSV files for analysis and visualization.

### 4. Output

- **Web Dashboard**: Access the web dashboard to visualize real-time sensor data, system performance metrics, and historical trends.
- **Data Analysis**: Analyze logged data to identify patterns, trends, and optimize system settings.
- **Energy Optimization**: Use insights from data analysis to improve energy efficiency and optimize solar power utilization.

## Conclusion

The automation process outlined above streamlines the development, deployment, and operation of the RaspiSolarControl project. By automating tasks such as sensor monitoring, system control, and data logging, the project aims to efficiently utilize solar power resources while providing insights for optimization and improvement.

![RaspiSolarControl Animation](/assets/raspi_solar_control.svg)

## Features

- **Sensor Interface:** Interfacing with temperature and humidity sensors.
- **Data Logging:** Logging sensor data to a CSV file for analysis.
- **System Control:** Controlling the solar system based on sensor data.
- **Web Dashboard:** A simple web dashboard to visualize sensor data.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Raspberry Pi board
- Temperature and humidity sensors (replace with your specific sensors)
- Python 3 installed on Raspberry Pi

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/niladrridas/raspisolarcontrol.git
    ```

2. Navigate to the project directory:

    ```
    cd RaspiSolarControl
    ```

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Connect the temperature and humidity sensors to the Raspberry Pi.
2. Run the main Python script:

    ```
    python src/main.py
    ```

3. Access the web dashboard by opening `web_app/index.html` in a web browser.

## Configuration

- Update sensor configurations in `config/sensors_config.json`.
- Adjust system settings in `config/settings.json`.

## Contributing

Contributions are welcome! Please follow the [Contributing Guidelines](https://github.com/niladrridas/raspisolarcontrol/blob/main/CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](https://github.com/niladrridas/raspisolarcontrol/blob/main/LICENSE).

## Acknowledgements

- Thanks to [OpenWeather](https://openweathermap.org/) for providing weather data for testing.
- Special thanks to Ubidots for providing a platform for real-time data visualization.
- Inspired by the Maker community and open-source projects driving innovation in environmental monitoring.
