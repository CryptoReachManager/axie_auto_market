import requests
import json

# Endpoint de GraphQL
url = "https://api-gateway.skymavis.com/graphql/marketplace"

# Clave API (Reemplaza esto con tu clave real)
api_key = "" #Escribir aqui la key 

# La petición que quieres hacer
query = """
query MyQuery {
  axies(
    auctionType: Sale
    sort: PriceAsc
    criteria: {breedCount: 4, classes: Reptile, ppBug: 6, ppReptile: 5}
  ) {
    results {
      id
      class
      breedCount
      axpInfo {
        level
        xpToLevelUp
        xp
      }
      order {
        endedPrice
        duration
        currentPriceUsd
        currentPrice
      }
      parts {
        class
      }
    }
  }
}
"""

# Headers para la solicitud, incluyendo la clave API
headers = {
    "Content-Type": "application/json",
    "X-API-Key": api_key,
}

# Realizando la solicitud
response = requests.post(url, json={'query': query}, headers=headers)

# Verificando que la solicitud fue exitosa
if response.status_code == 200:
    # Convirtiendo la respuesta a JSON
    response_json = response.json()
    # Imprimiendo la respuesta
    print(json.dumps(response_json, indent=2))
else:
    print("Error en la solicitud:", response.status_code)
