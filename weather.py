# -*- coding: utf-8 -*-
"""weather

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wMBOzwh7XUq-Yg_Yiz0hxzdzclnZ1bGk
"""

import requests

from datetime import datetime

api_key = '56114590a218909b42cbf82ec0e42196'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
coor_d = api_data ['coord']
wind_spd = api_data['wind']['speed']
v_isibility = api_data['visibility']
time_zone = api_data['timezone']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is  = {:.2f} deg C".format(temp_city))
print ("Current weather desc    =",weather_desc)
print ("Current Humidity        =",hmdt, '%')
print ("coorde                  =",coor_d,)
print ("Current wind speed      =",wind_spd ,'kmph')
print ("visibility data         =",v_isibility)
print ("timezone                =",time_zone)