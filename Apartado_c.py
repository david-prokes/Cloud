import requests

url = 'https://api.open-meteo.com/v1/forecast?latitude=39.56939&longitude=2.65024&hourly=temperature_2m'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperatures = data["hourly"]["temperature_2m"]
    avg_temp = sum(temperatures) / len(temperatures)
    
    print(f"Temperatura media: {avg_temp:.2f}°C")
else:
    print("Error al obtener los datos:", response.status_code)