import requests as requests

def listar_nombre_paises(url):

    paises = requests.get(url)
    paises = paises.json()

    for pais in paises:

          #print(f"Nombre Comun: {pais['name']['common']}")
          #print(f"Nombre Oficial: {pais['name']['official']}")
          #print(f"Nombre Oficial: {pais['official']}")

          print(f"Nombre Oficial en Español: {pais['translations']['spa']['official']}")
          print(f"Su capital es: {pais['capital'][0]}")
          print(f"Su moneda es: {pais['currencies']}")
          print(f"Su Codigo telefonico: {pais['idd']['root'] + pais['idd']['suffixes'][0]}")
          #print(pais)

url = 'https://restcountries.com/v3.1/independent?=status=true&fields=translations,capital,idd,currencies'
listar_nombre_paises(url)