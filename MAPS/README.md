# 🌍 Mapa Interactivo de Lugares Visitados

Este proyecto muestra en un mapa interactivo todos los lugares que he visitado, con marcadores de colores según la frecuencia de visitas. Al pasar el ratón por encima, puedes ver cuántas veces he estado en cada lugar.

## 🧰 Tecnologías utilizadas

- Python 3
- [Folium](https://python-visualization.github.io/folium/) — para generar mapas interactivos en HTML
- HTML — salida del mapa

## 🗺️ Funcionalidades

- Mapa centrado en Europa y Canarias.
- Marcadores personalizados por lugar.
- Tooltip con el número de visitas al pasar el cursor.
- Colores de marcadores según número de visitas:
  - 🟩 **Verde**: 5 o más visitas
  - 🟧 **Naranja**: entre 2 y 4 visitas
  - 🔵 **Azul**: 1 visita

## ▶️ Cómo ejecutar

1. Asegúrate de tener Python 3 instalado.
2. Instala Folium:

```bash
pip install folium

python3 map_flights.py
open mapa_visitas.html
