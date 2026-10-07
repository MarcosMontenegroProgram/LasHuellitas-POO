import sqlite3
from dao.database import conectar

class MascotaDAO:
    @staticmethod
    def insertar(mascota):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            tipo = mascota.__class__.__name__
            cursor.execute("""
                INSERT OR IGNORE INTO mascota (numero_microchip, tipo, fecha_ultima_vacuna)
                VALUES (?, ?, ?)
            """, (mascota.numeroMicrochip, tipo, mascota.fechaUltimaVacuna.isoformat()))
            conexion.commit()
        except sqlite3.Error as e:
            print(f"Error SQLite al insertar mascota: {e}")
        finally:
            if "conexion" in locals() and conexion:
                conexion.close()

    @staticmethod
    def obtener_todos():
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM mascota")
            return cursor.fetchall()
        except sqlite3.Error:
            return []
        finally:
            if "conexion" in locals() and conexion:
                conexion.close()

    @staticmethod
    def actualizar(mascota):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            tipo = mascota.__class__.__name__
            cursor.execute("""
                UPDATE mascota SET tipo = ?, fecha_ultima_vacuna = ?
                WHERE numero_microchip = ?
            """, (tipo, mascota.fechaUltimaVacuna.isoformat(), mascota.numeroMicrochip))
            conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al actualizar mascota: {e}")
        finally:
            if "conexion" in locals() and conexion:
                conexion.close()

    @staticmethod
    def eliminar(numero_microchip):
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM mascota WHERE numero_microchip = ?", (numero_microchip,))
            conexion.commit()
        except sqlite3.Error:
            pass
        finally:
            if "conexion" in locals() and conexion:
                conexion.close()

