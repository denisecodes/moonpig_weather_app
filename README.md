# Moonpig Weather App

## Introduction

This was completed as part of a coding test for Moongpig.

## Prerequisites

Please ensure you have the following installed on your laptop locally before running the project.

- Python 3.11 installed on your local machine.
- [Pipenv](https://pipenv.pypa.io/en/latest/) installed. You can install it using pip: `pip install pipenv`.
- An API key from [WeatherAPI.com](https://www.weatherapi.com/). You will need to sign up for an account and obtain your API key.

## Installation

Follow these steps to set up and run the Moonpig Weather App locally:

1. **Get an API Key:**
   - Visit [WeatherAPI.com](https://www.weatherapi.com/) and sign up for an account if you don't already have one.
   - Log in to your account and obtain an API key. You will need this key to access weather data.

2. **Create a .env File:**
   - In the root directory of the project, create a file named `.env`.
   - Open the `.env` file using a text editor and add the following line, replacing `your_api_key` with the API key you obtained from WeatherAPI.com:
     ```plaintext
     API_KEY=your_api_key
     ```

3. **Install Dependencies:**
   - Open your terminal and navigate to the project's root directory.
   - Run the following command to install the project's dependencies using Pipenv:
     ```shell
     pipenv install
     ```

4. **Run the App:**
   - After the installation is complete, you can now run the Moonpig Weather App with the following command:
     ```shell
     python app.py
     ```

## Usage

Once the app is running, open your web browser and navigate to `http://localhost:5000`. You will be presented with a simple web interface that allows you to enter a city or postcode and retrieve weather information.
