import requests
import os
from dotenv import load_dotenv
import json
from datetime import  timedelta,date


load_dotenv()
api_key = os.getenv("ALT_WEATHER_API_KEY")
print(api_key)

today = date.today()
past = timedelta(days = 120)
start_date = today - past
end_date = today
print(start_date,end_date)

url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Ottawa%2CCanada/{start_date}/{end_date}?unitGroup=metric&include=days&key={api_key}&contentType=json"

#url2 = f'https://www.meteosource.com/api/v1/free/point?place_id=ottawa&sections=all&timezone=UTC&language=en&units=metric&key={api_key}'


def get_json_data(url):
    data = requests.get(url)
    json_file = data.json()
    #print(data)
    #print(json_file)
    return json_file