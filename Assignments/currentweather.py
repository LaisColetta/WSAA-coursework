
# Assignment 1
# Student: Lais Coletta Pereira
# References: https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
# 

import requests

def get_current_weather():
    # Define the API URL
    url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_direction_10m"

    # Send a GET request to the API
    response = requests.get(url)
        
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
            
        # request temperature and wind direction from the json file
        temperature = data['current']['temperature_2m']
        wind_direction = data['current']['wind_direction_10m']
            
        # Print the current temperature and wind direction
        print("Current Temperature:", temperature)
        print("Current Wind Direction (10m):", wind_direction)
    else:
        print("Failed to fetch data. Status code:", response.status_code)

# Call the function to fetch and print current weather data
get_current_weather()
