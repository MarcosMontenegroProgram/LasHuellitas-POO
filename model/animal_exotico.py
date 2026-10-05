from model.mascota import Mascota

class AnimalExotico(Mascota):
    def obtenerDuracion(self) -> str:
        return "30 min"

    def obtenerTarifa(self) -> int:
        return 40000
