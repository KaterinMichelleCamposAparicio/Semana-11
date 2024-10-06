# Importar las librerías necesarias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV (ajusta la ruta del archivo si es necesario)
heart_disease_df = pd.read_csv('heart_disease_uci.csv')

# Filtrar las columnas relevantes: Edad (age) y Colesterol (chol)
heart_disease_filtered_df = heart_disease_df[['age', 'chol']].dropna()

# Estilo personalizado
sns.set_style("whitegrid")  # Fondo más claro
plt.figure(figsize=(8, 6))

# Gráfico de líneas con un estilo atractivo
sns.lineplot(x='age', y='chol', data=heart_disease_filtered_df, marker='o', color='#00BFFF', linewidth=3, markersize=10, markerfacecolor='#1E90FF')

# Personalizar el título y etiquetas
plt.title('Niveles de Colesterol según Edad - Enfermedad cardíaca UCI', fontsize=18, weight='bold', color='#4682B4')
plt.xlabel('Edad', fontsize=14, weight='bold', color='#4682B4')
plt.ylabel('Niveles de Colesterol', fontsize=14, weight='bold', color='#4682B4')

# Ajustar el diseño para que sea dinámico
plt.tight_layout()

# Mostrar gráfico
plt.show()


