import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)

data = response.json()

current = data["current_condition"][0]

print("\nWeather Report")
print("-" * 20)
print("City:", city)
print("Temperature:", current["temp_C"], "°C")
print("Humidity:", current["humidity"], "%")
print("Weather:", current["weatherDesc"][0]["value"])