Features:

City Search: Geocode any city worldwide using Open-Meteo's free geocoding service.
Real-Time Weather: Fetch current temperature (°C), wind speed (km/h), weather conditions, and timestamp.
Modern UI: Gradient backgrounds, glass cards, animations, and responsive design (works on mobile!).
Error Handling: Graceful messages for invalid cities or API issues.
No Backend Dependencies: Uses only Flask and requests—lightweight and fast.


Technology used:

Python 3          Core language
Flask             Web framework for routing and templates
requests          HTTP client for API calls
Open-Meteo API    Free weather data (geocoding + forecast)
HTML/CSS          Frontend with Poppins font and custom styles
Jinja2            Templating (built into Flask)


APIs Used:
Open-Meteo Weather API

Geocoding Endpoint: GET /v1/search?name={city}&count=1 → Returns lat/lon.
Forecast Endpoint: GET /v1/forecast?latitude={lat}&longitude={lon}&current_weather=true → Current weather data.

