import openrouteservice

# Reemplaza con tu API Key de OpenRouteService
API_KEY = "5b3ce3597851110001cf62482444961d79ee43a1bffff654be6e2e52"

# Diccionario con coordenadas de ciudades
ciudades = {
    "santiago": (-70.6483, -33.4569),
    "valparaiso": (-71.6127, -33.0472),
    "buenos aires": (-58.3816, -34.6037),
    "mendoza": (-68.8458, -32.8895),
    "cordoba": (-64.1888, -31.4201)
}

def main():
    client = openrouteservice.Client(key=API_KEY)
    while True:
        print("\nIngrese 's' para salir.")
        origen = input("Ciudad de Origen (en minúsculas): ")
        if origen.lower() == 's':
            break
        destino = input("Ciudad de Destino (en minúsculas): ")
        if destino.lower() == 's':
            break

        if origen not in ciudades or destino not in ciudades:
            print("❌ Ciudad no encontrada. Intente nuevamente.")
            continue

        print("Seleccione el medio de transporte:")
        print("1 - Automóvil")
        print("2 - Bicicleta")
        print("3 - Caminando")
        modo = input("Opción (1-3): ")

        if modo == '1':
            profile = 'driving-car'
        elif modo == '2':
            profile = 'cycling-regular'
        elif modo == '3':
            profile = 'foot-walking'
        else:
            print("Opción inválida. Intente nuevamente.")
            continue

        coords = [ciudades[origen], ciudades[destino]]

        route = client.directions(coords, profile=profile, format='geojson')
        summary = route['features'][0]['properties']['summary']

        distancia_km = summary['distance'] / 1000
        distancia_millas = distancia_km * 0.621371
        duracion_min = summary['duration'] / 60

        print(f"\nRuta de {origen.title()} a {destino.title()}:")
        print(f"- Distancia: {distancia_km:.2f} km ({distancia_millas:.2f} millas)")
        print(f"- Duración estimada: {duracion_min:.1f} minutos")
        print(f"- Narrativa del viaje: {route['features'][0]['properties']['segments'][0]['steps'][0]['instruction']}")
        print("-" * 50)

if __name__ == "__main__":
    main()