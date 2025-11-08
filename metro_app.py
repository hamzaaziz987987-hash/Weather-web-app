from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def search_city(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    try:
        data = requests.get(url).json()
        if not data.get('results'):
            return None, None, "City not found!"
        result = data['results'][0]
        return result['latitude'], result['longitude'], result['name']
    except:
        return None, None, "Error connecting to API"

def get_weather(lat, lon):
    if lat is None or lon is None:
        return None
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        data = requests.get(url).json()
        w = data['current_weather']
        desc_map = {0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast", 45: "Fog", 61: "Rain", 71: "Snow"}

        desc_lower = desc_map.get(w['weathercode'], "Unknown").lower()
        return {
            'temp': w['temperature'],
            'wind': w['windspeed'],
            'desc': desc_map.get(w['weathercode'], "Unknown"),
            'time': w['time'],
            'desc_lower': desc_lower
        }
    except:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    city_name = ""
    error = ""

    if request.method == 'POST':
        city = request.form['city'].strip()
        if city:
            lat, lon, name = search_city(city)
            if lat and lon:
                city_name = name
                weather = get_weather(lat, lon)
                if not weather:
                    error = "Could not fetch weather data."
            else:
                error = name  # "City not found!" or error
        else:
            error = "Please enter a city."

    return render_template('index.html', weather=weather, city=city_name, error=error)

if __name__ == '__main__':
    app.run(debug=True)