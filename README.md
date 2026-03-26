# BioPulse AI

Proyecto de monitoreo de signos vitales con inteligencia artificial.

## Descripción
BioPulse AI es un sistema que lee el pulso y oxigenación de la sangre usando sensores y detecta anomalías mediante un modelo de Machine Learning.

## Archivos
- `hardware/arduino_code.ino` → Código Arduino para leer el pulso
- `src/ml_model.py` → Modelo de ML para clasificar las condiciones
- `src/dashboard.py` → Dashboard interactivo con Streamlit
- `data/sample_pulse_data.csv` → Datos de ejemplo
- `requirements.txt` → Librerías necesarias

## Cómo usar
1. Conecta el sensor de pulso al Arduino y sube `arduino_code.ino`.
2. Instala las librerías de Python:
