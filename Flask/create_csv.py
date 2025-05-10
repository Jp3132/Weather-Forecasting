from data_call import get_json_data,url
import csv
import json

# temporary json to avoid over exceeding api limit when testing
"""
with open('./data/temp.json','w') as file:
    json.dump(json_file,file,indent = 4)

with open('./data/temp.json','r') as file:
    json_file = json.load(file)
"""


def future_data():
    json_file = get_json_data(url)
    csvheader = ["datetime",
                "datetimeEpoch",
                "tempmax",
                "tempmin", 
                "temp",
                "feelslikemax",
                "feelslikemin",
                "feelslike",
                "dew",
                "humidity",
                "precip",
                "precipprob", 
                "precipcover", 
                "preciptype", 
                "snow", 
                "snowdepth", 
                "windgust",
                "windspeed", 
                "winddir", 
                "sealevelpressure", 
                "cloudcover", 
                "visibility", 
                "solarradiation", 
                "solarenergy",
                "uvindex",
                "sunrise",
                "sunriseEpoch", 
                "sunset",
                "sunsetEpoch", 
                "moonphase", 
                "conditions", 
                "description",
                "icon",
                "stations", 
                ]

    final_data = []

    for i in json_file['days']:
        temp = [i["datetime"],
                i["datetimeEpoch"],
                i["tempmax"],
                i["tempmin"], 
                i["temp"],
                i["feelslikemax"],
                i["feelslikemin"],
                i["feelslike"],
                i["dew"],
                i["humidity"],
                i["precip"],
                i["precipprob"], 
                i["precipcover"], 
                i["preciptype"], 
                i["snow"], 
                i["snowdepth"], 
                i["windgust"],
                i["windspeed"], 
                i["winddir"], 
                i["pressure"], 
                i["cloudcover"], 
                i["visibility"], 
                i["solarradiation"], 
                i["solarenergy"],
                i["uvindex"],

                i["sunrise"],
                i["sunriseEpoch"], 
                i["sunset"],
                i["sunsetEpoch"], 
                i["moonphase"], 
                i["conditions"], 
                i["description"],
                i["icon"],
                i["stations"]]
        final_data.append(temp)

    with open('.\data\weather_data.csv','w',newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(csvheader)
        writer.writerows(final_data)

a = future_data()