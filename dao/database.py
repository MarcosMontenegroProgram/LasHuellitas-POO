import sqlite3

def conectar():
    return sqlite3.connect("las_huellitas.db")

def crear_tablas():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                id_cliente INTEGER PRIMARY KEY,
                rut TEXT NOT NULL,
                nombre TEXT NOT NULL,
                correo TEXT NOT NULL,
                telefono TEXT,
                dias_deuda INTEGER
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mascota (
                numero_microchip TEXT PRIMARY KEY,
                tipo TEXT NOT NULL,
                fecha_ultima_vacuna TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS atencion (
                id_atencion INTEGER PRIMARY KEY,
                fecha_hora TEXT NOT NULL,
                diagnostico TEXT,
                total REAL,
                rut_cliente TEXT,
                microchip_mascota TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS detalle_atencion (
                id_detalle INTEGER PRIMARY KEY AUTOINCREMENT,
                id_atencion INTEGER,
                descripcion TEXT,
                costo REAL
            )
        """)
        conexion.commit()
    except sqlite3.Error as e:
        print(f"Error al crear tablas: {e}")
    finally:
        if "conexion" in locals() and conexion:
            conexion.close()

