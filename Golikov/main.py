from opencage.geocoder import OpenCageGeocode
from  tkinter import *




def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language = "ru")
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            country = results[0]["components"]["country"]
            region = results[0]["components"]["state"]
            return f"Широта: {lat}, Долгота: {lon} \n Страна: {country} \n Регион: {region}"
        else:
            return "Город не найден"
    except Exception as er:
        return f"Возникла ошибка:{er}"


def show_coordinates(event=None):
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text = f"Координаты города {city}:\n {coordinates}" )

key = '8b4a33d6325641709f146b214f0c1c78'

window = Tk()
window.title("Координаты городов")
window.geometry("350x200")

entry = Entry()
entry.pack()
entry.bind("<Return>", show_coordinates)

button = Button(text = "Получение координат", command=show_coordinates)
button.pack()

label = Label(text = "Введите город и нажмите на кнопку получение координат")
label.pack()

window.mainloop()

