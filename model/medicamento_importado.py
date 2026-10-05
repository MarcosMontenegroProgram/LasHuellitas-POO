class MedicamentoImportado:
    def __init__(self, idMedicamento: int, nombre: str, precioUSD: float, margenGanancia: float):
        self.idMedicamento = idMedicamento
        self.nombre = nombre
        self.precioUSD = precioUSD
        self.margenGanancia = margenGanancia

    def calcularPrecioCLP(self, tipoCambioDolar: float) -> float:
        return self.precioUSD * tipoCambioDolar * (1 + self.margenGanancia)
