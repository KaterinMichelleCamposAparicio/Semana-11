import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
file_path = 'student mental.csv'
student_mental_health_df = pd.read_csv(file_path)

# Crear una nueva columna que identifique si un estudiante tiene problemas de salud mental o no
student_mental_health_df['mental_health_issue'] = student_mental_health_df[['depression', 'anxiety', 'isolation']].max(axis=1) > 2

# Contar los estudiantes en cada categoría: Ansiedad, Depresión, Estrés (aislamiento), Sin problemas
health_issue_counts = {
    "Ansiedad": (student_mental_health_df['anxiety'] > 2).sum(),
    "Depresión": (student_mental_health_df['depression'] > 2).sum(),
    "Estrés": (student_mental_health_df['isolation'] > 2).sum(),
    "Sin problemas de salud mental": (~student_mental_health_df['mental_health_issue']).sum()
}

# Crear un DataFrame a partir de los conteos
mental_health_summary_df = pd.DataFrame(list(health_issue_counts.items()), columns=["Issue", "Contar"])

# Gráfico circular con colores en tonos celeste y pastel
plt.figure(figsize=(8, 6))
plt.pie(mental_health_summary_df['Contar'], labels=mental_health_summary_df['Issue'], 
        autopct='%1.1f%%', startangle=90, 
        colors=['#87CEFA', '#00BFFF', '#1E90FF', '#4682B4'],  # Tonos celeste
        shadow=True, explode=(0.05, 0.05, 0.05, 0), 
        wedgeprops={'edgecolor': 'gray'})  # Bordes más definidos

# Personalización del título
plt.title('Distribución de Problemas de Salud Mental en Estudiantes', fontsize=18, weight='bold', color='#4682B4')

# Mejorar el diseño ajustando el espaciado
plt.tight_layout()

# Mostrar gráfico
plt.show()


