import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

API_KEY = 'Your_API_Key'   # replace locally

def get_weather_icon(condition):
    condition = condition.lower()
    if "clear" in condition:
        return "icons/sunny.png"
    elif "cloud" in condition:
        return "icons/cloudy.png"
    elif "rain" in condition:
        return "icons/rainy.png"
    elif "snow" in condition:
        return "icons/snow.png"
    else:
        return "icons/default.png"

def get_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") == 200:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]

        result_label.config(
            text=f"Weather in {city}\n{weather.title()}\nTemperature: {temp} °C"
        )

        icon_path = get_weather_icon(weather)
        img = Image.open(icon_path).resize((80, 80))
        photo = ImageTk.PhotoImage(img)

        weather_icon_label.config(image=photo)
        weather_icon_label.image = photo 

    else:
        messagebox.showerror("Error", data.get("message"))



root = tk.Tk()
root.title("Weather Predictor")
root.geometry("350x350")
root.resizable(False, False)

title_label = tk.Label(root, text="Weather Predictor", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

city_label = tk.Label(root, text="Enter City Name:")
city_label.pack()

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

get_button = tk.Button(root, text="Get Weather", command=get_weather)
get_button.pack(pady=10)

weather_icon_label = tk.Label(root)
weather_icon_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11), justify="center")
result_label.pack(pady=10)

root.mainloop()
