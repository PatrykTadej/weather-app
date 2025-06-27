from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = 'a3dba3a71917f48d7ee953db3794a595'

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None
    if request.method == 'POST':
        city = request.form.get('city')
        weather_data = get_weather(city)
        if weather_data is None:
            error = f"Could not retrieve data for {city}. Please try again."
    return render_template('index.html', weather_data=weather_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)