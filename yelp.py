import config # 💡importing our env variables from dotenv
import requests # 💡open a web url 
import json # 💡json stands for Javascript Object Notation and is commonly used to transmit web data

###
# 🆘 Help us fix this file!! 🆘
###

# 1. 🆘✨ we want to get events for the city name a user types in. Replace the placeholder variable with city 🏙 as a parameter!
def get_events( FIX_ME ):

    # 2. 🆘✨ use the dotenv file to find the correct variable for Yelp!
    # We need to use our key! Look in the .env file for the Yelp key name
    headers = { "Authorization": f"Bearer {config.FIX_ME}" }
    params = {"location": city, "limit": 5, "term": "seafood"}

    # 💡the Request() method calls an external URL from our Python server
    request = requests.get(
        "https://api.yelp.com/v3/businesses/search",
        params=params,  # 💡parameters are passed via the URL
        headers=headers, # 💡headers are variables passed DIRECTLY to the server
    )

    # 3. 🆘✨we want to get a JSON response from Yelp. 
    # They keep the info we need in the response_body.events. Help us get the data we want!
    events = json.loads(request.text)["FIX_ME"]

    # 💡returns a JSON array of events in a city
    return events
