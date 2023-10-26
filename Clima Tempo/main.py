import requests
from bs4 import BeautifulSoup


def get_temperature(cidade_id):
  url = f"https://www.climatempo.com.br/previsao-do-tempo/cidade/{cidade_id}/"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  min_temp = soup.find("span", id="min-temp-1")
  max_temp = soup.find("span", id="max-temp-1")

  print(
      f"[-] A TEMPERATURA MÁXIMA EM {nome_cidade.upper()} - {estado} É DE {max_temp.text}, COM MÍNIMA DE {min_temp.text}"
  )


def get_city_id(city_name):
  global cidade_id, nome_cidade, estado
  url = "https://www.climatempo.com.br/json/busca-por-nome"
  payload = {"name": city_name}
  response = requests.post(url, data=payload)
  data = response.json()
  if data[0]["response"]["success"]:
    cidade_id = data[0]["response"]["data"][0]["idcity"]
    nome_cidade = data[0]["response"]["data"][0]["city"]
    estado = data[0]["response"]["data"][0]["uf"]
    get_temperature(cidade_id)
  else:
    print("[-] CIDADE NÃO ENCONTRADA!")


city_name = input("[-] NOME DA CIDADE: ").strip()
get_city_id(city_name)
