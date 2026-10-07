import requests
from requests.exceptions import Timeout, ConnectionError, RequestException

def obtener_valor_dolar() -> float:
    url = "https://mindicador.cl/api/dolar"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return float(data["serie"][0]["valor"])
    except Timeout:
        print("⚠️ Timeout API Dólar. Usando referencial 900.0")
        return 900.0
    except ConnectionError:
        print("⚠️ ConnectionError API Dólar. Usando referencial 900.0")
        return 900.0
    except (ValueError, KeyError, RequestException) as e:
        print(f"⚠️ Error API Dólar ({e}). Usando referencial 900.0")
        return 900.0

