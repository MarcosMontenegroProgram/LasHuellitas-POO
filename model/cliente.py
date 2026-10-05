from model.persona import Persona

class Cliente(Persona):
    def __init__(self, rut: str, nombre: str, correo: str, telefono: str, idCliente: int, diasDeuda: int):
        super().__init__(rut, nombre, correo, telefono)
        self.idCliente = idCliente
        self.diasDeuda = diasDeuda

    def obtenerRol(self) -> str:
        return "Cliente"

    @property
    def diasDeuda(self) -> int:
        return self._diasDeuda

    @diasDeuda.setter
    def diasDeuda(self, valor: int):
        if valor < 0:
            raise ValueError("Los días de deuda no pueden ser negativos.")
        self._diasDeuda = valor

    def estaMoroso(self) -> bool:
        return self._diasDeuda > 30
