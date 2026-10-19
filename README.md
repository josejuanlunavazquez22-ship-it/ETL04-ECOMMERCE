# ETL04-ECOMMERCE: Pipeline de Análisis de Ventas

Este proyecto implementa un pipeline ETL modular en Python para procesar datos de ordenes de venta, validar calidad de datos (descarte de anomalías) y generar reportes analíticos.

## 🛠️ Tecnologías
* Python 3.x
* Pandas

## 🚀 Reglas de Negocio y Transformaciones
1. **Filtrado:** Solo registros con estado `COMPLETED`.
2. **Calidad de Datos:** Remover simbolos de moneda, sufijos y espacios sobrantes.
3. **Métrica:** Cálculo de `subtotal bruto` y `total neto`.
4. **Almacenamiento:** Carga de  data final en un reporte CSV.

## 📂 Estructura del Proyecto
- `src/`: Módulos de extracción, transformación y carga.
- `main.py`: Orquestador principal del pipeline.
- `data/`: Directorios de entrada y salida procesada.

## 🏃 Ejecución
```bash
python main.py