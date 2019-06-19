import tkinter as tk
from tkinter import Menu
from tkinter import ttk     #  'themed' tkinter
import requests

win = tk.Tk()
win.title('Check Weather')


def inc_size():
    win.minsize(width=250, height=1)  # 1 == default


menuBar = Menu()
win.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")
menuBar.add_cascade(label="File", menu=fileMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="File 1")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="File 2")
tabControl.pack(expand=0, fill="both")

weath_cond = ttk.LabelFrame(tab1, text="Current Weather Condition")
weath_cond.grid(column=0, row=0, padx=8, pady=4)

city = tk.StringVar()
citySelected = ttk.Combobox(weath_cond, width=12, textvariable=city)
citySelected['values'] = ('Kanpur', "Agra", "Jalandhar", "Brazil")

max_width = max([len(x) for x in citySelected['values']])
new_width = max_width
citySelected.config(width=new_width)

entry_width = max_width + 3

ttk.Label(weath_cond, text="Clouds:").grid(column=0, row=1, sticky="W", padx=10, pady=4)
updated = tk.StringVar()
updatedEntry = ttk.Entry(weath_cond, width=entry_width, textvariable=updated, state="readonly")
updatedEntry.grid(column=1, row=1, sticky="W")


ttk.Label(weath_cond, text="Temperature(F):").grid(column=0, row=2, sticky="W", padx=10, pady=4)
temp = tk.StringVar()
tempEntry = ttk.Entry(weath_cond, width=entry_width, textvariable=temp, state="readonly")
tempEntry.grid(column=1, row=2, sticky="W")

ttk.Label(weath_cond, text="Tempprature(max):").grid(column=0, row=3, sticky="W", padx=10, pady=4)
weather = tk.StringVar()
weatherEntry = ttk.Entry(weath_cond, width=entry_width, textvariable=weather, state="readonly")
weatherEntry.grid(column=1, row=3, sticky="W")

ttk.Label(weath_cond, text="Wind Direction(deg):").grid(column=0, row=4, sticky="W", padx=10, pady=4)
dew = tk.StringVar()
dewEntry = ttk.Entry(weath_cond, width=entry_width, textvariable=dew, state="readonly")
dewEntry.grid(column=1, row=4, sticky="W")

ttk.Label(weath_cond, text="Relative Humidity:").grid(column=0, row=5, sticky="W", padx=10, pady=4)
rel_humi = tk.StringVar()
rel_humiEntry = ttk.Entry(weath_cond, width=entry_width, textvariable=rel_humi, state="readonly")
rel_humiEntry.grid(column=1, row=5, sticky="W")

ttk.Label(weath_cond, text="Wind Speed(km/hr):").grid(column=0, row=6, sticky="W", padx=10, pady=4)
wind = tk.StringVar()
windEntry = ttk.Entry(weath_cond, width=entry_width, textvariable=wind, state="readonly")
windEntry.grid(column=1, row=6, sticky="W")

ttk.Label(weath_cond, text="Visibility(mt):").grid(column=0, row=7, sticky="W", padx=10, pady=4)
visi = tk.StringVar()
visiEntry = ttk.Entry(weath_cond, width=entry_width, textvariable=visi, state="readonly")
visiEntry.grid(column=1, row=7, sticky="W")

ttk.Label(weath_cond, text="MSL_Pressure:").grid(column=0, row=8, sticky="W", padx=10, pady=4)
press = tk.StringVar()
pressEntry = ttk.Entry(weath_cond, width=entry_width, textvariable=press, state="readonly")
pressEntry.grid(column=1, row=8, sticky="W")



weath_cond.grid_configure(column=0, row=1, padx=8, pady=4)

weather_cities = ttk.LabelFrame(tab1, text=" Check Weather For ")
weather_cities.grid(column=0, row=0, padx=8, pady=4)

ttk.Label(weather_cities, text="Location:  ").grid(column=0, row=0, padx=10, pady=4)

city = tk.StringVar()


def action():
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=ee9133747d7277d4974f74b431ee3042".format(city.get())
    res = requests.get(url)
    data = res.json()
    updated.set(data['clouds']['all'])
    weather.set(data['main']['temp_max'])
    temp.set(data['main']['temp'])
    dew.set(data['wind']['deg'])
    rel_humi.set(data['main']['humidity'])
    wind.set(data['wind']['speed'])
    visi.set(data['visibility'])
    press.set(data['main']['pressure'])


citySelected = ttk.Entry(weather_cities, width=13, textvariable=city)
citySelected.grid(column=1, row=0, padx=13)
btn = ttk.Button(weather_cities, width=13, text="Check", command=action)
btn.grid(row=1, column=1, padx=13, pady=5)

inc_size()
win.resizable(0, 0)
win.mainloop()
