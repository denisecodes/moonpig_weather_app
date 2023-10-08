from flask import Flask, render_template, request, url_for
import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/show_weather', methods=['POST'])
def show_weather():
    user_input = request.form['search-bar']
    parameters = {
        "key": os.environ.get("API_KEY"),
        "q": user_input,
        "api": "no"
    }
    response = requests.get("http://api.weatherapi.com/v1/current.json", params=parameters)
    print(response)
    print(f"User's input: {user_input}")
    data = response.json()
    location_data = data['location']
    print(location_data)
    current_data = data['current']
    print(current_data)
    return render_template('weather.html', location=location_data, current=current_data)

if __name__ == '__main__':
    app.run(debug=True)
