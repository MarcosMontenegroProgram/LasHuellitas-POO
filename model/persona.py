from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, rut: str, nombre: str, correo: str, telefono: str):
        self.rut = rut
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        
    @abstractmethod
    def obtenerRol(self) -> str:
        pass
