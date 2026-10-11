import math
import requests

URL_DOLAR = "https://mindicador.cl/api/dolar"
VALOR_RESPALDO = 900.0


def obtener_valor_dolar_info() -> tuple[float, bool]:
    """Devuelve (valor, es_respaldo); el respaldo nunca se presenta como dato actual."""
    try:
        response = requests.get(URL_DOLAR, timeout=5)
        response.raise_for_status()
        valor = float(response.json()["serie"][0]["valor"])
        if not math.isfinite(valor) or valor <= 0:
            raise ValueError("La API entregó un valor de dólar inválido.")
        return valor, False
    except (requests.RequestException, ValueError, KeyError, TypeError, IndexError) as e:
        print(f"No se pudo obtener el dólar actual ({e}). Se usará el valor de respaldo ${VALOR_RESPALDO:.1f}; no corresponde al valor actual.")
        return VALOR_RESPALDO, True


def obtener_valor_dolar() -> float:
    """Compatibilidad con código que solo necesita el importe."""
    return obtener_valor_dolar_info()[0]
