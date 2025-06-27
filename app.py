from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = 'a3dba3a71917f48d7ee953db3794a595'

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

# Add the get_icon function here
def get_icon(weather_description):
    icons = {
        "thunderstorm": "cloud_lightning.png",
        "drizzle": "light_rain.png",
        "rain": "rain_cloud.png",
        "snow": "snow.png",
        "clear": "partly_cloudy_day.png",
        "clouds": "clouds.png",
        "light rain" : "light_rain.png",
        "clear sky" : "sun.png",
        "few clouds" : "clouds.png",
        "scattered clouds" : "cloud.png",
        "broken clouds" : "clouds.png",
        "shower rain": "heavy_rain",
        "mist" : "fog.png",
        "thunderstorm with light rain" : "cloud_lightning.png",
        "thunderstorm with rain" : "storm.png",
        "thunderstorm with heavy rain" : "cloud_lightning.png",
        "light thunderstorm" : "storm.png",
        "heavy thunderstorm" : "cloud_lightning.png",
        "ragged thunderstorm" : "cloud_lightning.png",
        "thunderstorm with light drizzle" : "storm.png",
        "thunderstorm with drizzle" : "storm.png",
        "thunderstorm with heavy drizzle" : "cloud_lightning.png",
}
    
    for key in icons:
        if key in weather_description.lower():
            return icons[key]
    return "default_icon.png"  # Fallback icon

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None
    icon_file = None
    
    if request.method == 'POST':
        city = request.form.get('city')
        weather_data = get_weather(city)
        if weather_data:
            icon_file = get_icon(weather_data['weather'][0]['description'])
        else:
            error = f"Could not retrieve data for {city}. Please try again."
            
    return render_template('index.html', weather_data=weather_data, error=error, icon_file=icon_file)

if __name__ == '__main__':
    app.run(debug=True)