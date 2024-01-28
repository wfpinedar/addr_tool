import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
from joblib import dump

# Cargar los datos
df = pd.read_excel('../out.xlsx')

# Asegurarse de que no hay valores nulos
df.dropna(subset=['DIRECCION', 'direccion_estandarizada'], inplace=True)

# Crear conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(df['DIRECCION'], df['direccion_estandarizada'], test_size=0.3, random_state=42)

# Crear y entrenar el modelo
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

# Evaluar el modelo
y_pred = model.predict(X_test)
report = classification_report(y_test, y_pred)

# Guardar el modelo
dump(model, 'modelo_direccion.joblib')

print(report)
