# En este proyecto quiero reflejar los sitios que he visitado
# usando la librería folium

import folium

# Diccionario con lugares, visitas y coordenadas
sitios_visitados = [
    {"nombre": "Lanzarote", "veces": 3, "lat": 28.9611, "lon": -13.5511},
    {"nombre": "La Gomera", "veces": 10, "lat": 28.1167, "lon": -17.2333},  # muchas ≈ 10
    {"nombre": "Fuerteventura", "veces": 1, "lat": 28.3587, "lon": -14.0537},
    {"nombre": "El Hierro", "veces": 1, "lat": 27.7406, "lon": -18.0208},
    {"nombre": "La Palma", "veces": 3, "lat": 28.6836, "lon": -17.7644},
    {"nombre": "Gran Canaria", "veces": 6, "lat": 28.1248, "lon": -15.43},
    {"nombre": "Madrid", "veces": 3, "lat": 40.4168, "lon": -3.7038},
    {"nombre": "Barcelona", "veces": 4, "lat": 41.3874, "lon": 2.1686},
    {"nombre": "Londres", "veces": 2, "lat": 51.5074, "lon": -0.1278},
    {"nombre": "Paris", "veces": 5, "lat": 48.8566, "lon": 2.3522},
    {"nombre": "Salamanca", "veces": 1, "lat": 40.963, "lon": -5.6689},
    {"nombre": "Dublin", "veces": 1, "lat": 53.3498, "lon": -6.2603},
    {"nombre": "Moscu", "veces": 1, "lat": 55.7558, "lon": 37.6176},
    {"nombre": "Normandia", "veces": 1, "lat": 49.1829, "lon": -0.3700},
    {"nombre": "Tarragona", "veces": 1, "lat": 41.1189, "lon": 1.2445},
    {"nombre": "Mallorca", "veces": 1, "lat": 39.6953, "lon": 3.0176},
    {"nombre": "Zaragoza", "veces": 1, "lat": 41.6488, "lon": -0.8891},
    {"nombre": "Formigal", "veces": 1, "lat": 42.7711, "lon": -0.3889},
    {"nombre": "La Molina", "veces": 1, "lat": 42.3356, "lon": 1.9344},
    {"nombre": "Nantes", "veces": 1, "lat": 47.2184, "lon": -1.5536},
    {"nombre": "Cordoba", "veces": 1, "lat": 37.8882, "lon": -4.7794},
    {"nombre": "Sevilla", "veces": 1, "lat": 37.3891, "lon": -5.9845},
    {"nombre": "Krakow - Zawoja", "veces": 1, "lat": 49.6852, "lon": 19.5725},
    {"nombre": "Amsterdam", "veces": 1, "lat": 52.3676, "lon": 4.9041},
]

# Crear el mapa centrado en Europa
m = folium.Map(location=[42.0, 0.0], zoom_start=4)

# Añadir cada lugar al mapa
for sitio in sitios_visitados:
    color = (
        "green" if sitio["veces"] >= 5
        else "orange" if sitio["veces"] >= 2
        else "blue"
    )
    folium.Marker(
        location=[sitio["lat"], sitio["lon"]],
        popup=f'{sitio["nombre"]} - Visitas: {sitio["veces"]}',
        tooltip=f'{sitio["nombre"]}: {sitio["veces"]} visita(s)',
        icon=folium.Icon(color=color)
    ).add_to(m)

# Guardar el mapa como HTML
m.save("mapa_visitas.html")

