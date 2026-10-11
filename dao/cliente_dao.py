import sqlite3
from dao.database import conectar
from model.cliente import Cliente


class ClienteDAO:
    @staticmethod
    def insertar(cliente):
        conexion = conectar()
        try:
            cursor = conexion.execute("""
                INSERT INTO cliente (rut, nombre, correo, telefono, dias_deuda)
                VALUES (?, ?, ?, ?, ?)
            """, (cliente.rut, cliente.nombre, cliente.correo, cliente.telefono, cliente.diasDeuda))
            conexion.commit()
            cliente.idCliente = cursor.lastrowid
            return cliente.idCliente
        except sqlite3.Error as e:
            conexion.rollback()
            print(f"Error SQLite al insertar cliente: {e}")
            return None
        finally:
            conexion.close()

    @staticmethod
    def obtener_por_rut(rut):
        conexion = conectar()
        try:
            row = conexion.execute("SELECT id_cliente, rut, nombre, correo, telefono, dias_deuda FROM cliente WHERE rut = ?", (rut,)).fetchone()
            return Cliente(row[1], row[2], row[3], row[4], row[0], row[5]) if row else None
        except (sqlite3.Error, ValueError, TypeError) as e:
            print(f"Error SQLite al buscar cliente: {e}")
            return None
        finally:
            conexion.close()

    @staticmethod
    def obtener_todos():
        conexion = conectar()
        try:
            return conexion.execute("SELECT id_cliente, rut, nombre, correo, telefono, dias_deuda FROM cliente").fetchall()
        except sqlite3.Error as e:
            print(f"Error SQLite al leer clientes: {e}")
            return []
        finally:
            conexion.close()

    @staticmethod
    def actualizar(cliente):
        conexion = conectar()
        try:
            conexion.execute("UPDATE cliente SET rut = ?, nombre = ?, correo = ?, telefono = ?, dias_deuda = ? WHERE id_cliente = ?", (cliente.rut, cliente.nombre, cliente.correo, cliente.telefono, cliente.diasDeuda, cliente.idCliente))
            conexion.commit()
        except sqlite3.Error as e:
            conexion.rollback()
            print(f"Error SQLite al actualizar cliente: {e}")
        finally:
            conexion.close()

    @staticmethod
    def eliminar(id_cliente):
        conexion = conectar()
        try:
            conexion.execute("DELETE FROM cliente WHERE id_cliente = ?", (id_cliente,))
            conexion.commit()
        except sqlite3.Error as e:
            conexion.rollback()
            print(f"Error SQLite al eliminar cliente: {e}")
        finally:
            conexion.close()
