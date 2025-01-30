import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('C:\Analitica/BikePrices.csv')

#Exploración Inicial
data.shape
data.head()
data.describe()
types = data.dtypes.value_counts()

print('Number of Features: %d'%(data.shape[1]))
print('Number of Customers: %d'%(data.shape[0]))
print('Data Types and Frequency in Dataset:')
print(types)

#Gráfica 1
data["Brand"].value_counts().plot(kind="bar", color=["yellow", "green"])

plt.title("Distribución de Marcas")
plt.xlabel("Marca")
plt.ylabel("Cantidad")
plt.show()

#Gráfica 2
data["Seller_Type"].value_counts().plot(kind="pie")
plt.title("Tipo de vendedor")
plt.show()

#Gráfica 3
plt.figure(figsize=(10, 8))
plt.scatter(data["Selling_Price"], data["Brand"], color='blue', alpha=0.7)
plt.title("Precios de venta")
plt.show()
