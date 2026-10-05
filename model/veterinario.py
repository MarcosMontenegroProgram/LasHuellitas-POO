from model.empleado import Empleado

class Veterinario(Empleado):
    def obtenerRol(self) -> str:
        return "Veterinario"
        
    def registrarDiagnostico(self, atencion, diagnostico: str):
        atencion.diagnostico = diagnostico
        
    def prescribirMedicamento(self, atencion, idMedicamento: int, nombre: str, precioUSD: float, margenGanancia: float):
        atencion.agregarMedicamento(idMedicamento, nombre, precioUSD, margenGanancia)
