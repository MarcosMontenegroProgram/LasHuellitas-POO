import sqlite3
from dao.database import conectar

class AtencionDAO:
    @staticmethod
    def insertar(atencion):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            
            # Iniciar transacción para cabecera y detalles
            cursor.execute("BEGIN TRANSACTION;")
            
            cursor.execute("""
                INSERT INTO atencion (fecha_hora, diagnostico, total, rut_cliente, microchip_mascota)
                VALUES (?, ?, ?, ?, ?)
            """, (str(atencion.fechaHora), atencion.diagnostico, atencion.total, atencion.cliente.rut, atencion.mascota.numeroMicrochip))
            
            id_atencion = cursor.lastrowid
            
            # Insertar líneas de detalle (Procedimientos)
            for proc in atencion.procedimientos:
                cursor.execute("""
                    INSERT INTO detalle_atencion (id_atencion, descripcion, costo)
                    VALUES (?, ?, ?)
                """, (id_atencion, f"Procedimiento: {proc.nombre}", proc.costo))

            # Insertar líneas de detalle (Medicamentos)
            for med in atencion.medicamentos:
                costo_clp = med.calcularPrecioCLP(atencion.tipoCambioDolar)
                cursor.execute("""
                    INSERT INTO detalle_atencion (id_atencion, descripcion, costo)
                    VALUES (?, ?, ?)
                """, (id_atencion, f"Medicamento: {med.nombre}", costo_clp))
                
            conexion.commit()
            return id_atencion
        except sqlite3.Error as e:
            if "conexion" in locals() and conexion:
                conexion.rollback()
            print(f"Error SQLite al insertar atención (Transacción cancelada): {e}")
            return None
        finally:
            if "conexion" in locals() and conexion:
                conexion.close()

    @staticmethod
    def obtener_atencion_con_detalles(id_atencion):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT id_atencion, fecha_hora, diagnostico, total, rut_cliente, microchip_mascota
                FROM atencion WHERE id_atencion = ?
            """, (id_atencion,))
            
            cabecera = cursor.fetchone()
            if not cabecera:
                return None
                
            cursor.execute("""
                SELECT id_detalle, descripcion, costo
                FROM detalle_atencion WHERE id_atencion = ?
            """, (id_atencion,))
            
            detalles = cursor.fetchall()
            
            return {
                "cabecera": cabecera,
                "detalles": detalles
            }
        except sqlite3.Error as e:
            print(f"Error SQLite al obtener atención: {e}")
            return None
        finally:
            if "conexion" in locals() and conexion:
                conexion.close()
