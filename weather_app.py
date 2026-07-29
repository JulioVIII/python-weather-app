import requests

def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

    except requests.exceptions.RequestException:
        print("Error connecting to the geocoding service.")
        return None

    if "results" not in data:
        return None

    result = data["results"][0]

    latitude = result["latitude"]
    longitude = result["longitude"]

    return latitude, longitude


def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,apparent_temperature,wind_speed_10m"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

    except requests.exceptions.RequestException:
        print("Error connecting to the weather service.")
        return None

    current = data["current"]

    temperature = current["temperature_2m"]
    apparent_temperature = current["apparent_temperature"]
    wind_speed = current["wind_speed_10m"]

    return temperature, apparent_temperature, wind_speed

    

def main():
    print("\n===== WEATHER APP =====")

    city=input("enter a city: ")

    coordinates=get_coordinates(city)

    if coordinates is None:
        print("City not found.")
        return

    latitude,longitude=coordinates

    weather=get_weather(latitude,longitude)

    temperature,apparent_temperature,wind_speed=weather

    print("\n===== WEATHER REPORT =====")
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Feels like: {apparent_temperature}°C")
    print(f"Wind Speed: {wind_speed} km/h")

if __name__ == "__main__":
    main()
