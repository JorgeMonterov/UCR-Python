import pandas as pd
import matplotlib.pyplot as plt

# 1-Cargar el archivo CSV como DataFrame
data_frame = pd.read_csv('ventas.csv')

#2- Calcular la ganancia y agregarla como una nueva columna llamada "Ganancia"
data_frame['Ganancia'] = data_frame['Ventas'] - data_frame['Gastos']

# Mostrar el DataFrame con la columna "Ganancia" agregada y el index=False es para no mostrar el index
print(data_frame.to_string(index=False))

#3- Graficar la evolución mensual de las ventas y los gastos
#leyendas para ventas y gastos
plt.plot(data_frame['Mes'], data_frame['Ventas'], label='Ventas', )
plt.plot(data_frame['Mes'], data_frame['Gastos'], label='Gastos', )

#4-Eje 'X' y 'Y'
plt.xlabel('Mes')
plt.ylabel('Cantidad')


plt.title('Evolución mensual de Ventas y Gastos')
plt.legend()

plt.show()
