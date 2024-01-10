from datetime import datetime
import pytz

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
        current_time = get_current_time(timezone)

        print(f"\nCity: {city}")
        print(f"Current time: {current_time}")

if __name__ == "__main__":
    main()
