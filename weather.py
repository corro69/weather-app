import requests, json
from datetime import datetime
import PySimpleGUI as sg 
import wget
import os

api_key = "23db0c3a7f6d8aa22af08f7ea39a0603"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
icon_url = "http://openweathermap.org/img/wn/"

now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")

layout = [
          [sg.Text("Local Weather")],
          [sg.Text("Enter City Name or Zip Code"), sg.InputText()],
          [sg.OK(), sg.Cancel()],
          [sg.Text(size=(40,1), key='OUTPUT1')],
          [sg.Text(size=(40,1), key='OUTPUT2')],
          [sg.Text(size=(40,1), key='OUTPUT3')],
          [sg.Text(size=(40,1), key='OUTPUT4')],
          [sg.Text(size=(40,1), key='OUTPUT5')], 
          [sg.Image(size=(40,1), pad=(150,0), key='OUTPUT6')]
          ]

window = sg.Window("Local Weather", layout, size=(400,325))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event =="Cancel":
        break

    if event == "OK":    
 
        city_name = values[0]
        complete_url = base_url + "q=" + city_name + "&appid=" + api_key
        response = requests.get(complete_url)
        x = response.json()
        
        if x["cod"] != "404":

            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y     %I:%M:%S %p")

            y = x["main"]
            q = x["wind"]

            temperature = y["temp"]
            current_temperature = "{:.2f}".format(temperature * 9/5 -459.76) 

            current_pressure = y["pressure"]

            current_humidity = y["humidity"]

            feelslike = y["feels_like"]
            current_feelslike = "{:.2f}".format(temperature * 9/5 - 459.76)

            current_wind_speed = q["speed"]

            current_direction = q["deg"]

            z = x["weather"]

            weather_description = z[0]["description"]
            weather_icon = z[0]["icon"]
            current_weather_icon = icon_url + weather_icon
            Import_current_weather_icon = wget.download(current_weather_icon +".png")
        
        window['OUTPUT1'].update('Date and Time:   ' + dt_string)
        window['OUTPUT2'].update('Temperature:   ' + str(current_temperature) + " \u2109")
        window['OUTPUT3'].update('Atmospheric Pressure:   ' + str(current_pressure) + " hPa")
        window['OUTPUT4'].update('Humidity:   ' + str(current_humidity) + " %")
        window['OUTPUT5'].update('Current Conditions:   ' + str(weather_description))
        window['OUTPUT6'].update((weather_icon) + ".png")
        
        os.remove(weather_icon + ".png")

window.close()  
