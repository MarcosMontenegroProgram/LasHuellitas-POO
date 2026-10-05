from model.empleado import Empleado

class Asistente(Empleado):
    def obtenerRol(self) -> str:
        return "Asistente"
        
    def agendarHora(self, cliente, fechaHora):
        print(f"Hora agendada para el cliente {cliente.nombre} en {fechaHora}")
        
    def registrarPago(self, cliente, monto: float):
        print(f"Pago de ${monto} registrado para el cliente {cliente.nombre}")
