# Clínica Veterinaria Las Huellitas (POO) - Evaluación Sumativa N°3

## 📅 Fechas del Proyecto
* **Fecha de Inicio:** Martes 6 de octubre de 2026
* **Fecha de Término (Entrega):** Martes 13 de octubre de 2026

## 🎯 ¿Para qué sirve este proyecto?
Este proyecto es un **Sistema de Gestión de Software Orientado a Objetos** diseñado para la Clínica Veterinaria "Las Huellitas". Su objetivo principal es automatizar y digitalizar la administración del negocio, permitiendo:
1. Registrar clientes y llevar un control de sus estados de morosidad.
2. Ingresar mascotas separadas por sus tipos específicos (Perros, Gatos, Exóticos), manejando información crítica como su fecha de última vacuna y su número de microchip.
3. Registrar atenciones médicas (consultas, cirugías y venta de medicamentos), calculando automáticamente las tarifas y convirtiendo valores de medicamentos extranjeros de USD a Pesos Chilenos (CLP) usando el valor real del dólar del día.

---

## 1. Integrantes y Negocio
**Negocio asignado:** Clínica Veterinaria Huellitas  
**Integrante 1:** Sergio Marguirott Hernández  
*(Si hay más integrantes en tu equipo original, asegúrate de añadirlos aquí en el futuro)*

## 2. Instrucciones de Instalación y Ejecución
Para instalar y ejecutar el programa desde un computador que solo tiene Python, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/MarcosMontenegroProgram/LasHuellitas-POO.git
   cd LasHuellitas-POO
   ```

2. **Crear y activar un entorno virtual (Recomendado):**
   - En Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación:**
   ```bash
   python main.py
   ```
   *Al iniciar, la base de datos `las_huellitas.db` se creará automáticamente si no existe.*

---

## ⚙️ Explicación Detallada: ¿Cómo funciona cada aspecto del código?

### El Modelo de Datos (Paradigma Orientado a Objetos) - Carpeta `model/`
El corazón del sistema es la POO. Todo es un objeto.
* **Herencia y Polimorfismo (`mascota.py`, `perro.py`, `gato.py`, `animal_exotico.py`):** Existe una clase "Padre" o abstracta llamada `Mascota`. De ella heredan `Perro`, `Gato` y `AnimalExotico`. Cada una sobrescribe (polimorfismo) los métodos `obtenerTarifa()` y `obtenerDuracion()` para que cobren valores distintos y tomen tiempos distintos según el tipo de animal.
* **Encapsulamiento y Validaciones (Setters):** Las clases como `Mascota` o `Persona` no permiten guardar cualquier dato. Mediante decoradores como `@property` y `@rut.setter` o `@numeroMicrochip.setter`, el código intercepta la información antes de guardarla.
* **Reglas de Negocio (`atencion.py` y `excepciones.py`):** El sistema crea sus propios errores lógicos. Si un cliente debe dinero por más de 30 días, lanza un `ClienteMorosoError`. Si agendamos cirugía a una mascota con vacunas vencidas (más de 1 año), lanza `MascotaNoAptaCirugiaError`.

### Capa de Persistencia (Base de Datos SQLite) - Carpeta `dao/`
El sistema no borra sus datos al cerrarse, los guarda permanentemente usando el patrón DAO (Data Access Object).
* **`database.py`:** Se encarga de conectarse a un archivo local llamado `las_huellitas.db`. Si las tablas no existen, las crea automáticamente (`CREATE TABLE IF NOT EXISTS`).
* **Operaciones CRUD:** Clases como `ClienteDAO` y `MascotaDAO` inyectan los objetos del programa en la base de datos de manera segura usando consultas parametrizadas.
* **Transacciones (`atencion_dao.py`):** Para guardar una Atención médica, se utiliza el comando `BEGIN TRANSACTION`. Esto permite que se guarde la cabecera (la atención general) y luego múltiples detalles (los procedimientos y medicamentos). Si falla, la transacción completa se cancela (`rollback`).

### Consumo de Servicios Externos (API) - Carpeta `service/`
* **`indicador_api.py`:** Utiliza la librería oficial `requests` para conectarse a la URL pública `https://mindicador.cl/api/dolar`. Obtiene el precio del dólar del día actual. Si el internet falla, o la página tarda más de 5 segundos en responder, el sistema atrapa el error (`Timeout` o `ConnectionError`) y utiliza un valor referencial (ej: 900.0) para evitar que el programa colapse.

### La Interfaz de Usuario (El Controlador) - Archivo `main.py`
* Actúa como el puente entre el usuario y la lógica. Despliega un menú interactivo (`while True`) que permite al usuario probar todas las funcionalidades (P01 al P19 de la rúbrica). 
* Maneja los bloques `try...except`, de modo que si el modelo de datos arroja un error (como un RUT mal escrito o una deuda inválida), `main.py` atrapa ese error y lo muestra amigablemente sin que la aplicación se caiga.

---

## 3. Decisiones de Seguridad
- **Prevención de Inyección SQL:** Se han parametrizado **todas** las consultas a la base de datos (utilizando el marcador `?` proporcionado por la librería `sqlite3`). En ninguna consulta de `ClienteDAO`, `MascotaDAO` o `AtencionDAO` se concatena texto que escribe el usuario de forma directa con `f-strings` o el operador `+`, lo que previene que atacantes inyecten sentencias maliciosas.
- **Validación de Entradas (Setter):** Se ha asegurado la consistencia de los datos directamente en el modelo de la clase `Mascota`. Específicamente, mediante el uso de los decoradores `@property` y `@numeroMicrochip.setter`, se valida estrictamente que el número de microchip sea de **exactamente 15 dígitos numéricos**. Si un usuario intenta ingresar un formato inválido (como letras o menos caracteres), la aplicación rechaza la asignación con un `ValueError` descriptivo y el flujo principal atrapa la excepción sin cerrar el programa abruptamente.

## 4. Uso de Inteligencia Artificial (IA)
En el desarrollo de este entregable, se hizo uso de asistentes de Inteligencia Artificial (Google Gemini) para fortalecer y complementar el sistema de la siguiente manera:
- **Código Adoptado (DAO Transaccional):** Se adoptó la sugerencia de la IA para manejar la persistencia de la entidad `Atencion` y `Detalle_Atencion` en un mismo método transaccional utilizando `BEGIN TRANSACTION` y `.commit()` a través de SQLite en Python (`dao/atencion_dao.py`). 
  - *Razón Técnica:* Era crucial asegurar que si la inserción de los procedimientos o medicamentos de una consulta fallaba, la cabecera (atención) no quedara insertada en la base de datos de manera huérfana. Al usar la transacción sugerida por la IA, se garantiza el principio de Atomicidad en la base de datos, lo que estabiliza el sistema de persistencia.
- **Código Adoptado (Refactorización del Setter):** Se modificó el encapsulamiento en Python utilizando `@property` para las validaciones del microchip guiados por el asistente, logrando rechazar datos inválidos de una manera pitónica sin romper el encapsulamiento del POO.
