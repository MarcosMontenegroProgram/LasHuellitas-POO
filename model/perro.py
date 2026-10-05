from model.mascota import Mascota

class Perro(Mascota):
    def obtenerDuracion(self) -> str:
        return "20 min"

    def obtenerTarifa(self) -> int:
        return 25000
