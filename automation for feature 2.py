<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Noise Monitoring Dashboard</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
  <script src="https://unpkg.com/leaflet.heat/dist/leaflet-heat.js"></script>
  <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
  <style>
    body {
      font-family: sans-serif;
      margin: 20px;
    }
    #chart-container {
      width: 80%;
      margin: auto;
    }
    #map {
      height: 400px;
      margin-top: 30px;
    }
  </style>
</head>
<body>

  <h2>📈 Noise Level Trends</h2>
  <div id="chart-container">
    <canvas id="noiseChart"></canvas>
  </div>

  <h2>📍 Heatmap of Noisy Areas</h2>
  <div id="map"></div>

  <script>
    // --- Line Chart of Noise Levels Over Time ---
    const ctx = document.getElementById('noiseChart').getContext('2d');
    const noiseChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM'],
        datasets: [{
          label: 'Noise Level (dB)',
          data: [55, 63, 72, 80, 76, 60],
          borderColor: 'red',
          backgroundColor: 'rgba(255,0,0,0.1)',
          tension: 0.3,
          fill: true
        }]
      },
      options: {
        scales: {
          y: {
            min: 40,
            max: 100,
            title: {
              display: true,
              text: 'Decibels (dB)'
            }
          }
        }
      }
    });

    // --- Leaflet Heatmap ---
    const map = L.map('map').setView([28.6139, 77.2090], 16);  // Set to your campus location

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Example noisy locations [lat, lng, intensity]
    const heatPoints = [
      [28.6145, 77.2080, 0.8],  // Cafeteria
      [28.6139, 77.2095, 0.6],  // Library
      [28.6142, 77.2101, 0.9],  // Hostel
    ];

    L.heatLayer(heatPoints, {
      radius: 25,
      blur: 15,
      maxZoom: 17,
    }).addTo(map);
  </script>

</body>
</html>
