import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Cargar datos de ejemplo
data = pd.read_csv("../data/sample_pulse_data.csv")
X = data[['pulse','spo2']]  # Variables de entrada
y = data['condition']       # Normal / Arritmia

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluación
y_pred = model.predict(X_test)
print("=== Reporte de clasificación ===")
print(classification_report(y_test, y_pred))

# Guardar modelo entrenado
joblib.dump(model, "pulse_model.pkl")
print("Modelo guardado como pulse_model.pkl")
