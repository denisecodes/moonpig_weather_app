from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def find_weather():
    user_postcode = request.form['postcode']
    parameters = {
        "key": os.environ.get("API_KEY"),
        "q": user_postcode,
        "api": "no"
    }
    response = requests.get("http://api.weatherapi.com/v1/current.json", params=parameters)
    print(response)
    print(f"User's postcode: {user_postcode}")
    data = response.json()
    location_data = data['location']
    print(location_data)
    current_data = data['current']
    print(current_data)
    return render_template('index.html', location=location_data, current=current_data)

if __name__ == '__main__':
    app.run(debug=True)
