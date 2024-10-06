# Importar las librerías necesarias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configurar el estilo para los gráficos
sns.set_style("whitegrid")

# Cargar el archivo CSV (reemplaza la ruta con la ubicación correcta del archivo)
file_path = 'Admin.csv'
admin_df = pd.read_csv(file_path)

# Renombrar las columnas en español para mayor claridad
admin_df.columns = ['ID', 'Medicamento', 'Fecha_Admin', 'Unidades']

# Convertir la columna 'Fecha_Admin' a formato datetime
admin_df['Fecha_Admin'] = pd.to_datetime(admin_df['Fecha_Admin'], format='%d/%m/%Y')

# Asegurarse de que la columna 'Unidades' sea numérica (eliminar comas si es necesario)
admin_df['Unidades'] = admin_df['Unidades'].replace(',', '', regex=True).astype(float)

# Agrupar los datos por mes y medicamento, sumando las unidades
uso_mensual = admin_df.groupby([admin_df['Fecha_Admin'].dt.to_period('M'), 'Medicamento'])['Unidades'].sum().unstack(fill_value=0)

# Crear el gráfico de barras con los datos procesados
ax = uso_mensual.plot(kind='bar', figsize=(12, 7), color=['#00BFFF', '#FF6347'], edgecolor='black')

# Personalizar el título y las etiquetas
plt.title('Uso Mensual Total de Medicamentos', fontsize=20, weight='bold', color='#4682B4', pad=20)
plt.xlabel('Mes', fontsize=16, weight='bold', color='#2F4F4F')
plt.ylabel('Total de Unidades Administradas', fontsize=16, weight='bold', color='#2F4F4F')

# Ajustes de los ticks y las leyendas
plt.xticks(rotation=45, fontsize=12, color='#696969', weight='bold')
plt.yticks(fontsize=12, color='#696969', weight='bold')
plt.legend(title='Medicamento', fontsize=13, title_fontsize='14', loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Ajustar la distribución de la figura
plt.tight_layout()

# Mostrar el gráfico
plt.show()



