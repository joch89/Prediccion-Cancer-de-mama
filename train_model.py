# train_model.py

# 1. Importar librerías
import pandas as pd
import joblib
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 2. Cargar dataset Breast Cancer
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# 3. División en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Entrenamiento
clf = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)
clf.fit(X_train, y_train)

# 5. Evaluación
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nReporte de clasificación:\n")
print(classification_report(y_test, y_pred, target_names=data.target_names))

# Matriz de confusión
cm = confusion_matrix(y_test, y_pred)
print("Matriz de Confusión:")
for i, clase_real in enumerate(data.target_names):
    for j, clase_predicha in enumerate(data.target_names):
        print(f"{clase_real} predicho como {clase_predicha}: {cm[i][j]}")

# 6. Guardar modelo
joblib.dump(clf, "modelo.pkl")
print("\nModelo guardado como 'modelo.pkl'")

# 7. Verificación de carga (opcional)
modelo_cargado = joblib.load("modelo.pkl")
ejemplo = X_test.iloc[0].values.reshape(1, -1)
print("\nPredicción de prueba:", modelo_cargado.predict(ejemplo))
