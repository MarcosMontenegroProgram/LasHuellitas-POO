from model.mascota import Mascota

class Gato(Mascota):
    def obtenerDuracion(self) -> str:
        return "15 min"

    def obtenerTarifa(self) -> int:
        return 20000
