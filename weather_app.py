import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "YOUR_OPENWEATHER_API_KEY"  # free at openweathermap.org

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name!")
        return
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        resp = requests.get(url)
        data = resp.json()
        if data.get("cod") != 200:
            messagebox.showerror("Error", data.get("message", "Failed to get data"))
            return
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"].title()
        result_label.config(text=f"Temp: {temp}°C\nHumidity: {humidity}%\nDescription: {desc}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")
tk.Label(root, text="Enter City:", font=("Arial", 12)).pack(pady=5)
city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)
tk.Button(root, text="Get Weather", command=get_weather,
          bg="#2196F3", fg="white", font=("Arial", 12)).pack(pady=5)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)
root.mainloop()