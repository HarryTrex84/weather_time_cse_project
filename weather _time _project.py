import requests

def get_weather(city_name):
    
    WTTR_URL = f"http://wttr.in/{city_name}?format=j1&m"

    try:
        response = requests.get(WTTR_URL, timeout=10)
        response.raise_for_status()

        data = response.json()

        if not data.get('nearest_area'):
            print(f"Error: Weather data not found for '{city_name}'. Check the spelling.")
            return

        location_data = data['nearest_area'][0]
        city = location_data['areaName'][0]['value']
        country = location_data['country'][0]['value']
        
        current = data['current_condition'][0]
        
        temperature = current.get('temp_C', 'N/A')
        description = current['weatherDesc'][0]['value']
        local_time = current.get('localObsDateTime', 'N/A')
        
        print("-" * 50)
        print(f"Weather Report for {city}, {country}:")
        print(f"  Local Time:  {local_time}")
        print(f"  Temperature: {temperature}°C")
        print(f"  Condition:   {description}")
        print("-" * 50)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while connecting to the weather service: {e}")
    except KeyError as e:
        print(f"Error: Could not parse weather data (missing key: {e}).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    try:
        import requests
    except ImportError:
        print("The 'requests' library is not installed.")
        print("Please install it using: pip install requests")
        exit()
        
    print("--- Simple Weather Checker (Now with Local Time!) ---")
    while True:
        city_input = input("Enter the city name (or 'quit' to exit): ").strip()
        
        if city_input.lower() == 'quit':
            print("Exiting weather checker. Goodbye!")
            break
        
        if city_input:
            get_weather(city_input)
        else:
            print("Please enter a valid city name.")