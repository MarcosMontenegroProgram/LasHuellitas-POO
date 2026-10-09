# Clínica Veterinaria Huellitas - Evaluación Sumativa N°3

## 1. Integrantes y Negocio
**Negocio asignado:** Clínica Veterinaria Huellitas  
**Integrante 1:** Sergio Marguirott Hernández

## 2. Instrucciones de Instalación y Ejecución
Para instalar y ejecutar el programa desde un computador que solo tiene Python, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/marcosems007-collab/LasHuellitas-POO.git
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

## 3. Decisiones de Seguridad
- **Prevención de Inyección SQL:** Se han parametrizado **todas** las consultas a la base de datos (utilizando el marcador `?` proporcionado por la librería `sqlite3`). En ninguna consulta de `ClienteDAO`, `MascotaDAO` o `AtencionDAO` se concatena texto que escribe el usuario de forma directa con `f-strings` o el operador `+`, lo que previene que atacantes inyecten sentencias maliciosas.
- **Validación de Entradas (Setter):** Se ha asegurado la consistencia de los datos directamente en el modelo de la clase `Mascota`. Específicamente, mediante el uso de los decoradores `@property` y `@numeroMicrochip.setter`, se valida estrictamente que el número de microchip sea de **exactamente 15 dígitos numéricos**. Si un usuario intenta ingresar un formato inválido (como letras o menos caracteres), la aplicación rechaza la asignación con un `ValueError` descriptivo y el flujo principal atrapa la excepción sin cerrar el programa abruptamente.

## 4. Uso de Inteligencia Artificial (IA)
En el desarrollo de este entregable, se hizo uso de asistentes de Inteligencia Artificial (Google Gemini) para fortalecer y complementar el sistema de la siguiente manera:
- **Código Adoptado (DAO Transaccional):** Se adoptó la sugerencia de la IA para manejar la persistencia de la entidad `Atencion` y `Detalle_Atencion` en un mismo método transaccional utilizando `BEGIN TRANSACTION` y `.commit()` a través de SQLite en Python (`dao/atencion_dao.py`). 
  - *Razón Técnica:* Era crucial asegurar que si la inserción de los procedimientos o medicamentos de una consulta fallaba, la cabecera (atención) no quedara insertada en la base de datos de manera huérfana. Al usar la transacción sugerida por la IA, se garantiza el principio de Atomicidad en la base de datos, lo que estabiliza el sistema de persistencia.
- **Código Adoptado (Refactorización del Setter):** Se modificó el encapsulamiento en Python utilizando `@property` para las validaciones del microchip guiados por el asistente, logrando rechazar datos inválidos de una manera pitónica sin romper el encapsulamiento del POO.
