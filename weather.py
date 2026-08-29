import requests

city = input("Enter city name: ").strip()

if not city:
    print("Please enter a city name.")
    exit()
print()
try:
    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url, timeout=10)

    data = response.json()

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

except Exception:
    print("Something went wrong.")
    print("Could not find weather information for that input.")