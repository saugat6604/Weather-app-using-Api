import tkinter as tk
import requests
import time

#to get the data from api
def getWeather(canvas):
    city = textfield.get()
    api ="https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=06c921750b9a82d8f5d1294e1586276f"
    json_data = requests.get(api).json()
    #weather only one object so can access main with index 0
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%M", time.gmtime(json_data['sys']['sunrise']))
    sunset = time.strftime("%I:%M:%M", time.gmtime(json_data['sys']['sunset']))
    final_info = condition + "\n" +str(temp) + "C"
    final_data = "\n" + "Max temp:" +str(max_temp) +"\n" + "Min temp:" +str(min_temp)+"\n"+"Pressure:"+str(pressure)+"\n"+"Humidity:"+str(humidity)
    label1.config(text = final_info)
    label2.config(text= final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins" ,15 ,"bold")
t= ("poppins" , 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>',getWeather)

label1 = tk.Label(canvas , font = t)
label1.pack()
label2 = tk.Label(canvas, font =f)
label2.pack()

canvas.mainloop()