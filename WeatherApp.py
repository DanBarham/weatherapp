import tkinter as tk
import requests

# Window dimensions
HEIGHT = 700
WIDTH = 800


# Output formatting for the main display
def format_output(weather):
    try:
        name = weather["name"]
        current_conditions = weather["weather"][0]["main"]
        temp = weather["main"]["temp"]
        final_str = "City: %s \nConditions: %s\nTemperature (°F): %s" % (name, current_conditions, temp)
    except:
        final_str = "There was a problem with your request"

    return final_str

# OpenWeatherMap API call https://openweathermap.org/api
def get_weather(city):
    weather_key = "f2807fb18358708964d1fcdd59b41bce"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "APPID": weather_key,
        "q": city,
        "units": "imperial"
    }
    response = requests.get(url, params=params)
    bf_label["text"] = format_output(response.json())


# Main Window
root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)

canvas.pack()

background_image = tk.PhotoImage(file="landscape.png")
background_label = tk.Label(root, image=background_image)

background_label.place(relwidth=1, relheight=1)

# Top Frame
top_frame = tk.Frame(root, bg="#80c1ff", bd=5)
tf_entry = tk.Entry(top_frame, font=("Courier", 18), selectborderwidth=10)
tf_button = tk.Button(top_frame, font=("Courier", 18), text="Get Weather",
                      command=lambda: get_weather(tf_entry.get()))

top_frame.place(relx=.5, rely=.1, relwidth=.75, relheight=.1, anchor="n")
tf_entry.place(relwidth=.65, relheight=1)
tf_button.place(relx=.7, relheight=1, relwidth=.3)

# Bottom Frame
bottom_frame = tk.Frame(root, bg="#80c1ff", bd=5)
bf_label = tk.Label(bottom_frame, font=("Courier", 18), justify="left", anchor="nw", bd=4)

bottom_frame.place(relx=.5, rely=.25, relwidth=.75, relheight=.6, anchor="n")
bf_label.place(relwidth=1, relheight=1)

root.mainloop()
