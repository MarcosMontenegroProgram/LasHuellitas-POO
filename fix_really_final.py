import os
content = """from model.veterinario import Veterinario
from model.cliente import Cliente
from model.perro import Perro
from model.gato import Gato
from model.animal_exotico import AnimalExotico
from model.atencion import Atencion
from model.excepciones import ClienteMorosoError, MascotaNoAptaCirugiaError
from datetime import datetime, timedelta

from dao.database import crear_tablas
from dao.cliente_dao import ClienteDAO
from dao.mascota_dao import MascotaDAO
from service.indicador_api import obtener_valor_dolar
import sqlite3

def main():
    print("=== Inicializando Sistema ===")
    crear_tablas()
    
    try:
        dolar_actual = obtener_valor_dolar()
        print(f"Valor del Dólar obtenido de la API: ${dolar_actual}\\n")
        
        veterinario = Veterinario("11223344-5", "Dr. Juan Pérez", "juan.perez@huellitas.cl", "987654321", 101, "jperez", "pass123")
        cliente_valido = Cliente("15555666-7", "María Gómez", "maria@gmail.com", "911223344", 201, 10)
        
        print("=== DEMOSTRACIÓN REAL DE CRUD (CLIENTE) ===")
        cliente_crud = Cliente("11111111-1", "Usuario CRUD", "crud@mail.com", "12345678", 999, 0)
        ClienteDAO.insertar(cliente_crud)
        print("1. CREATE: Cliente insertado.")
        
        clientes_db = ClienteDAO.obtener_todos()
        print(f"2. READ: Total clientes actuales en SQLite: {len(clientes_db)}")
        
        cliente_crud.nombre = "Usuario CRUD Actualizado"
        ClienteDAO.actualizar(cliente_crud)
        print("3. UPDATE: Cliente actualizado en BD.")
        
        clientes_db = ClienteDAO.obtener_todos()
        print(f"4. READ: Validando cambios. Total: {len(clientes_db)}")
        
        ClienteDAO.eliminar(999)
        print("5. DELETE: Cliente eliminado de prueba.")
        
        clientes_db = ClienteDAO.obtener_todos()
        print(f"6. READ FINAL: Total clientes tras borrar: {len(clientes_db)}\\n")
        
        print("Ejecución de prueba completada con éxito.")
        
    except sqlite3.Error as e:
        print(f"Error de base de datos: {e}")
    except Exception as e:
        print(f"Error general: {e}")

if __name__ == '__main__':
    main()"""
with open('main.py', 'w', encoding='utf-8') as f:
    f.write(content)
