from datetime import datetime, timedelta
from model.excepciones import ClienteMorosoError, MascotaNoAptaCirugiaError
from model.veterinario import Veterinario
from model.asistente import Asistente
from model.cliente import Cliente
from model.perro import Perro
from model.gato import Gato
from model.animal_exotico import AnimalExotico
from model.atencion import Atencion

def main():
    print("Iniciando Sistema Las Huellitas...\n")

    print("=== Bloque 1: Polimorfismo ===")
    fecha_reciente = datetime.now() - timedelta(days=30)
    fecha_antigua = datetime.now() - timedelta(days=400)
    mascotas = [
        Perro("CHIP-PERRO-001", fecha_reciente),
        Gato("CHIP-GATO-002", fecha_reciente),
        AnimalExotico("CHIP-EXOTICO-003", fecha_antigua)
    ]
    for m in mascotas:
        tipo = m.__class__.__name__
        print(f"{tipo} - Microchip: {m.numeroMicrochip} | Duración: {m.obtenerDuracion()} | Tarifa: ${m.obtenerTarifa()}")
    print("\n")

    print("=== Bloque 2: Encapsulamiento en Cliente ===")
    try:
        cliente_invalido = Cliente("11111111-1", "Juan Perez", "juan@correo.com", "987654321", 1, -5)
    except ValueError as e:
        print(f"Excepción capturada correctamente (Creación con deuda negativa): {e}")

    cliente_valido = Cliente("22222222-2", "Maria Lopez", "maria@correo.com", "912345678", 2, 0)
    try:
        cliente_valido.diasDeuda = -10
    except ValueError as e:
        print(f"Excepción capturada correctamente (Setter con deuda negativa): {e}")
    print("\n")

    print("=== Bloque 3: Creación de Atención fluida (Agregación y Composición) ===")
    veterinario = Veterinario("99999999-9", "Dr. Vet", "vet@clinica.com", "999999999", 101, "drvet", "pass123")
    perrito = Perro("CHIP-PERRO-001", datetime.now() - timedelta(days=60))
    atencion1 = Atencion(1001, datetime.now(), 950.0, veterinario, perrito, cliente_valido)
    veterinario.registrarDiagnostico(atencion1, "Infección leve y revisión dental")
    atencion1.agregarProcedimiento(1, "Limpieza Dental", False, 35000.0)
    veterinario.prescribirMedicamento(atencion1, 10, "Antibiótico", 15.0, 0.2)
    atencion1.procesarAtencion()

    print("=== Bloque 4: Provocación de ClienteMorosoError ===")
    cliente_moroso = Cliente("33333333-3", "Pedro Moroso", "pedro@correo.com", "933333333", 3, 45)
    gato = Gato("CHIP-GATO-002", datetime.now() - timedelta(days=10))
    atencion2 = Atencion(1002, datetime.now(), 950.0, veterinario, gato, cliente_moroso)
    veterinario.registrarDiagnostico(atencion2, "Revisión general")
    try:
        atencion2.procesarAtencion()
    except ClienteMorosoError as e:
        print(f"Excepción ClienteMorosoError capturada: {e}")
    print("\n")

    print("=== Bloque 5: Provocación de MascotaNoAptaCirugiaError ===")
    animal_exotico = AnimalExotico("CHIP-EXOTICO-003", datetime.now() - timedelta(days=400))
    atencion3 = Atencion(1003, datetime.now(), 950.0, veterinario, animal_exotico, cliente_valido)
    veterinario.registrarDiagnostico(atencion3, "Problema grave, requiere cirugía")
    try:
        atencion3.agregarProcedimiento(2, "Cirugía de emergencia", True, 150000.0)
    except MascotaNoAptaCirugiaError as e:
        print(f"Excepción MascotaNoAptaCirugiaError capturada: {e}")
    print("\n")

    print("Ejecución del script principal completada sin errores inesperados.")

if __name__ == '__main__':
    main()
