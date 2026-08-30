import requests

def get_city():
    city = input("Enter city name: ").strip()

    if not city:
        print("Please enter a city name.")
        exit()

    return city


def fetch_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url, timeout=10)

    return response.json()


def display_weather(data, city):
    current = data["current_condition"][0]

    area = data["nearest_area"][0]["areaName"][0]["value"]
    country = data["nearest_area"][0]["country"][0]["value"]

    if city.lower() != area.lower():
        print(f"Note: '{city}' was matched to '{area}, {country}'")

    print()
    print(f"Weather in {area}, {country}")
    print(f"Temperature: {current['temp_C']}°C")
    print(f"Feels Like: {current['FeelsLikeC']}°C")
    print(f"Condition: {current['weatherDesc'][0]['value']}")
    print(f"Humidity: {current['humidity']}%")
    print(f"Wind: {current['windspeedKmph']} km/h")


city = get_city()

data = fetch_weather(city)

display_weather(data, city)