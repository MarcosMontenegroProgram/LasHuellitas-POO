from model.procedimiento import Procedimiento
from model.medicamento_importado import MedicamentoImportado
from model.excepciones import MascotaNoAptaCirugiaError, ClienteMorosoError
from datetime import datetime

class Atencion:
    def __init__(self, idAtencion: int, fechaHora: datetime, tipoCambioDolar: float, veterinario, mascota, cliente):
        self.idAtencion = idAtencion
        self.fechaHora = fechaHora
        self.diagnostico = ""
        self.tipoCambioDolar = tipoCambioDolar
        self.veterinario = veterinario
        self.mascota = mascota
        self.cliente = cliente
        self.procedimientos = []
        self.medicamentos = []

    def agregarProcedimiento(self, idProcedimiento: int, nombre: str, esCirugia: bool, costo: float):
        if esCirugia and not self.mascota.estaAptaParaCirugia():
            raise MascotaNoAptaCirugiaError(f"La mascota no está apta para cirugía.")
        procedimiento = Procedimiento(idProcedimiento, nombre, esCirugia, costo)
        self.procedimientos.append(procedimiento)

    def agregarMedicamento(self, idMedicamento: int, nombre: str, precioUSD: float, margenGanancia: float):
        medicamento = MedicamentoImportado(idMedicamento, nombre, precioUSD, margenGanancia)
        self.medicamentos.append(medicamento)

    def procesarAtencion(self):
        if self.cliente.estaMoroso():
            raise ClienteMorosoError(f"El cliente {self.cliente.nombre} presenta morosidad.")
        print("=== DESGLOSE DE LA ATENCIÓN ===")
        print(f"ID Atención: {self.idAtencion} | Fecha: {self.fechaHora}")
        print(f"Veterinario: {self.veterinario.nombre} | Cliente: {self.cliente.nombre}")
        print(f"Mascota Microchip: {self.mascota.numeroMicrochip}")
        print(f"Diagnóstico: {self.diagnostico}")
        total = self.mascota.obtenerTarifa()
        print(f"Tarifa base por consulta: ${total}")
        if self.procedimientos:
            print("Procedimientos:")
            for proc in self.procedimientos:
                print(f" - {proc.nombre} (Cirugía: {'Sí' if proc.esCirugia else 'No'}): ${proc.costo}")
                total += proc.costo
        if self.medicamentos:
            print("Medicamentos prescritos:")
            for med in self.medicamentos:
                precio_clp = med.calcularPrecioCLP(self.tipoCambioDolar)
                print(f" - {med.nombre}: ${precio_clp:.2f}")
                total += precio_clp
        print(f"TOTAL A PAGAR: ${total:.2f}")
        print("===============================\n")
