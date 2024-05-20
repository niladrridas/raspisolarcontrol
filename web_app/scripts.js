// scripts.js

// Function to fetch sensor data from server
function fetchSensorData() {
    // Fetch sensor data from server (replace with actual API call)
    const sensorData = {
        temperature: 25.5,
        humidity: 50.2
    };

    // Update sensor data on web page
    const sensorDataElement = document.getElementById("sensorData");
    sensorDataElement.innerHTML = `
        <p>Temperature: ${sensorData.temperature}°C</p>
        <p>Humidity: ${sensorData.humidity}%</p>
    `;
}

// Fetch sensor data on page load
window.onload = fetchSensorData;
