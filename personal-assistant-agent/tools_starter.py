import json
import urllib.request

def check_calendar(day):
    events = {
        "monday": "10am Team Standup, 2pm Client Meeting",
        "tuesday": "No events",
        "wednesday": "1pm Lunch with Alex",
        "thursday": "9am Dentist, 3pm Project Review",
        "friday": "No events"
    }
    return f"Events for {day}: {events.get(day.lower(), 'None')}"

def search_web(query):
    # Mock search function
    results = {
        "weather": "Sunny, 72F",
        "news": "Tech stocks rally as AI adoption grows",
        "stock": "AAPL: 185.20, MSFT: 420.50"
    }
    for key, value in results.items():
        if key in query.lower():
            return f"Top result: {value}"
    return "No relevant results found."

def get_user_preferences(category):
    prefs = {
        "travel": "Aisle seat, vegetarian meal",
        "communication": "Email preferred, no calls after 6pm",
        "news": "Tech and science focus"
    }
    return f"Preference for {category}: {prefs.get(category.lower(), 'Not specified')}"

# Add the tool definitions to the TOOLS_SCHEMA list here
TOOLS_SCHEMA = [
]

