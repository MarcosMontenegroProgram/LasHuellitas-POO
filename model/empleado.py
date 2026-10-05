from model.persona import Persona
from abc import ABC

class Empleado(Persona, ABC):
    def __init__(self, rut: str, nombre: str, correo: str, telefono: str, idEmpleado: int, usuario: str, contrasena: str):
        super().__init__(rut, nombre, correo, telefono)
        self.idEmpleado = idEmpleado
        self.usuario = usuario
        self.contrasena = contrasena
