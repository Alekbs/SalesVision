from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from skimage import io
import joblib
from skimage.transform import resize
import numpy as np
import pandas as pd
import csv


model = joblib.load('m_shirt.joblib')

data = []


with open('data2.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        print(row)
        data.append({
            "image_path": row['image_path'],
            "name": row['name'],
            "price": int(row['price'])

        })

# Извлечение признаков из изображений
image_features = []
for item in data:
    image = io.imread(item["image_path"])
    resized_image = resize(image, (100, 100))  # Приведем изображения к одному размеру для простоты
    flattened_image = resized_image.flatten()
    image_features.append(flattened_image)

# Извлечение признаков из текстов (названий и описаний товаров)

text_features = []
for item in data:
    text_features.append(item["name"])
# Векторизация текста
vectorizer = TfidfVectorizer()

text_features = vectorizer.fit_transform(text_features).toarray()
# Изменение размерности массива до 36 значений
# Изменение размерности массива до 36 значений
text_features = np.resize(text_features, (1, 97))


# Извлечение признака "price"
price_feature = np.array([item["price"] for item in data])[:, np.newaxis]

# Объединение признаков
print(" Объединение признаков")
new_features = np.concatenate((image_features, text_features, price_feature), axis=1)


predicted_sales = model.predict(new_features)
print(f"Predicted Sales for New Product: {predicted_sales[0]:.2f}")