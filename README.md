# Python Weather App

A console-based weather application built with Python that retrieves current weather information using the Open-Meteo API.

The user enters a city, the application retrieves its geographical coordinates, and then uses those coordinates to request current weather data.

## Features

- Search weather by city name
- Retrieve latitude and longitude automatically
- Display current temperature
- Display apparent temperature
- Display wind speed
- Handle invalid cities
- Handle connection and HTTP errors
- Uses two API requests

## Technologies

- Python 3
- Requests
- Open-Meteo Geocoding API
- Open-Meteo Weather API
- JSON

## Installation

Install the Requests library:

```bash
python -m pip install requests
```

## How to Run

Run the application:

```bash
python weather_app.py
```

Then enter a city:

```text
===== WEATHER APP =====

Enter a city: Cork

===== CURRENT WEATHER =====
City: Cork
Temperature: 18.2 °C
Feels like: 17.6 °C
Wind speed: 12.4 km/h
```

Weather values depend on the current conditions.

## How It Works

1. The user enters a city.
2. The application sends a request to the Open-Meteo Geocoding API.
3. The API returns the latitude and longitude.
4. The application uses those coordinates to request current weather data.
5. The JSON response is converted into Python data.
6. The weather information is displayed to the user.

## What I Learned

- Working with REST APIs
- Making HTTP GET requests with `requests`
- Using query parameters
- Processing JSON responses
- Working with dictionaries
- Returning multiple values from functions
- Tuple unpacking
- Handling HTTP and connection errors
- Organizing an application using functions
- Using `main()` as the program entry point

## Future Improvements

- Add humidity
- Add weather conditions
- Add daily forecasts
- Allow repeated city searches
- Save previous searches
- Add a graphical interface

## Author

Julio
