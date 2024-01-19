import pandas as pd

df = pd.read_csv('мужская футболка/data.csv', delimiter=";")
print(df.head())


import matplotlib.pyplot as plt
import seaborn as sns

# Создание графика распределения цен
plt.figure(figsize=(10, 6))
sns.histplot(df['sold'], bins=20, kde=True, color='skyblue')
plt.title('Распределение Цен')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.show()
