import pandas as pd
import matplotlib.pyplot as plt

#  Cargar el archivo 
file_path = 'netflix_titles.csv'
netflix_data = pd.read_csv(file_path)

#  Visualizar los primeros 10 registros del conjunto de datos
print("Primeros 10 registros del conjunto de datos:")
print(netflix_data.head(10))

#  Visualizar los últimos 15 registros del conjunto de datos
print("\nÚltimos 15 registros del conjunto de datos:")
print(netflix_data.tail(15))

#  Generar los estadísticos básicos
print("\nEstadísticos básicos:")
print(netflix_data.describe())

# Completar todos los datos vacíos (na) con ceros (0)
netflix_data.fillna(0, inplace=True)

# Filtrar datos desde 2010 hasta 2021
netflix_data['release_year'] = netflix_data['release_year'].astype(int)  
filtered_data = netflix_data[(netflix_data['release_year'] >= 2010) & (netflix_data['release_year'] <= 2021)]

# Contar la cantidad de películas y series por año
counts = filtered_data['type'].value_counts()

# Generar gráfico de barras
counts.plot(kind='bar', color=['blue', 'orange'])
plt.title('Comparación de películas vs series (2010 - 2021)')
plt.xlabel('Tipo')
plt.ylabel('Cantidad')
plt.xticks(rotation=0)  
plt.show()
