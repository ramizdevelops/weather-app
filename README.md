# Weather App

A simple GUI app to fetch and display current weather data using the OpenWeatherMap API.

## Features
- Enter city name → shows temperature, humidity, and description
- Clean Tkinter interface
- Handles invalid input or connection errors

## Setup
1. Get your free API key from [OpenWeatherMap](https://openweathermap.org/)
2. Add it to `weather_app.py` (replace `YOUR_OPENWEATHER_API_KEY`)
3. Install dependencies:
```bash
pip install requests
```
4. Run the app:
```bash
python weather_app.py
```

## Steps to Get Free API Key

1. Go to [OpenWeatherMap](https://home.openweathermap.org/users/sign_up)  
2. **Sign up** for a free account (just email + password).  
3. After logging in, go to **API Keys** section:  
   - Direct link: [https://home.openweathermap.org/api_keys](https://home.openweathermap.org/api_keys)  
4. You’ll see a **default API key** (usually named *“Default”*).  
5. You can also create a new one with any name (e.g., *weather_app*).  
6. Copy that key and paste it in your code:  
   ```python
   API_KEY = "your_api_key_here"