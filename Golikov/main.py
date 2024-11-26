from opencage.geocoder import OpenCageGeocode

def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language = "ru")
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            return lat, lon
        else:
            return "Город не найден"
    except Exception as er:
        return f"Возникла ошибка:{er}"

key = '8b4a33d6325641709f146b214f0c1c78'
city = "Samara"
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")