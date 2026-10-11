# Clínica Veterinaria Las Huellitas (POO) — Evaluación Sumativa N°3

## 1. Integrantes y negocio

**Negocio:** Clínica Veterinaria Huellitas
**Integrante 1:** Marcos Montenegro Soto
**Integrante 2:** Matias Sebastian Marin

Hay una discrepancia pendiente de confirmación por el equipo: la rúbrica señala la sección **114-2B-F1**, mientras la guía de pruebas señala **114-2A-F2**. Además, el README anterior lista a Marcos Montenegro Soto y Matias Sebastian Marin, pero la guía menciona a Sergio Marguirott Hernández. Se conservaron los integrantes que ya estaban en este README; el equipo debe confirmar la sección y la nómina definitiva.

## 2. Instalación y ejecución paso a paso

Se requiere Python **3.10 o posterior** y conexión a Internet para consultar el dólar actual. SQLite viene incluido con Python.

1. Instale Python desde [python.org](https://www.python.org/downloads/) y habilite Python en PATH.
2. Abra una terminal y clone el repositorio:

   ```bash
   git clone https://github.com/MarcosMontenegroProgram/LasHuellitas-POO.git
   cd LasHuellitas-POO
   ```

3. Instale las dependencias:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Inicie la aplicación:

   ```bash
   python main.py
   ```

La base `las_huellitas.db` se crea en el directorio de ejecución. Al iniciar, el programa intenta consultar el dólar en `https://mindicador.cl/api/dolar`; si la consulta falla, informa que usará el respaldo de $900 y que ese valor no es el valor actual. Para salir, use la opción `0`.

Para ejecutar el guion de verificación automatizado incluido en el repositorio:

```bash
python tests/run_acceptance.py
```

Las pruebas usan una base temporal y reemplazan la respuesta de red por respuestas controladas; no leen ni modifican la base local del usuario.

## 3. Decisiones de seguridad

- **Prevención de inyección SQL:** los datos ingresados se envían mediante parámetros `?` de `sqlite3`. No se concatenan valores de usuario en las consultas. El alta de atención y todas sus líneas de detalle se escriben dentro de una transacción; ante un error se ejecuta `rollback`.
- **Validación de entradas:** el setter de microchip acepta exactamente 15 dígitos ASCII. El modelo valida también nombre, costos y precios; la interfaz vuelve a pedir entradas numéricas inválidas y captura errores para continuar activa.
- **Reglas de negocio:** la cirugía se valida contra la fecha de última vacuna y se vuelve a comprobar al guardar. Una deuda de más de 30 días impide iniciar y guardar la atención. La validación de morosidad ocurre antes de insertar la cabecera.
- **Persistencia y migración:** SQLite conserva los datos entre ejecuciones. Cuando existe una base previa, se agrega `nombre` a `mascota` con el valor `Mascota`, sin borrar registros.
- **Servicio externo:** `service/indicador_api.py` contiene la llamada `requests` con timeout de cinco segundos y valida la respuesta. Si falla, el flujo informa el uso del respaldo y marca su origen en el desglose.

## 4. Uso de Inteligencia Artificial (IA)

Se usó un asistente de IA para revisar el flujo de escritura de `AtencionDAO.insertar`. La propuesta se modificó para preparar las líneas de procedimientos y medicamentos y escribirlas con `executemany` en la misma transacción que la cabecera. La decisión técnica fue asegurar atomicidad: si SQLite rechaza una línea de detalle, no queda una atención incompleta. También se conservó la regla de negocio en el modelo y se añadió una segunda validación al guardar para que no dependa únicamente de la interfaz.
