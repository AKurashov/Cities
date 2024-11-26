from opencage.geocoder import OpenCageGeocode

def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language = "ru")
        if results:
            return results[0]['geometry']['lat'], results[0]['geometry']['lng']
        else:
            return "Город не найден"
    except Exception as er:
        return f"Возникла ошибка:{er}"

key = '8b4a33d6325641709f146b214f0c1c78'
city = "Samara"
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")