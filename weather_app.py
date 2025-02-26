import requests
import json

def get_weather(city):
    # Your OpenWeather API key
    api_key = '08776f011101db64cb3fce99543db7d8'  # Replace with your API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Building the complete URL
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    
    # Sending the GET request
    response = requests.get(complete_url)
    
    # Convert the response to JSON
    data = response.json()

    print(data)
    
    # Check if the city was found
    if data["cod"] != "404":
        main_data = data["main"]
        weather_data = data["weather"][0]
        
        # Extracting information
        temperature = main_data["temp"]
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        description = weather_data["description"]
        
        # Displaying the weather information
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        print("City not found!")

if __name__ == "__main__":
    city = input("Enter the city name: ")
    get_weather(city)
