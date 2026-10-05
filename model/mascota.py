from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Mascota(ABC):
    def __init__(self, numeroMicrochip: str, fechaUltimaVacuna: datetime):
        self.numeroMicrochip = numeroMicrochip
        self.fechaUltimaVacuna = fechaUltimaVacuna

    @abstractmethod
    def obtenerDuracion(self) -> str:
        pass

    @abstractmethod
    def obtenerTarifa(self) -> int:
        pass

    def estaAptaParaCirugia(self) -> bool:
        limite = datetime.now() - timedelta(days=365)
        return self.fechaUltimaVacuna >= limite
