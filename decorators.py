from datetime import datetime
import pytz

def print_current_time(city_func):
    def wrapper(city, timezone):
        current_time = get_current_time(timezone)
        print(f"\nCity: {city}")
        print(f"Current time: {current_time}")
        city_func(city, timezone)
    return wrapper

@print_current_time
def get_weather(city, timezone):
    # Placeholder for weather retrieval logic (if needed)
    print(f"Weather information for {city}.")

def get_current_time(timezone):
    now = datetime.now(pytz.timezone(timezone))
    return now.strftime("%H:%M:%S %Z")

def main():
    locations = {
        'Berlin': 'Europe/Berlin',
        'New York': 'America/New_York',
        'London': 'Europe/London',
        'Tokyo': 'Asia/Tokyo',
        'Kathmandu': 'Asia/Kathmandu',
    }

    for city, timezone in locations.items():
        get_weather(city, timezone)

if __name__ == "__main__":
    main()
