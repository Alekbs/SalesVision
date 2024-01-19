from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction.text import TfidfVectorizer
from skimage import io
import joblib
from skimage.transform import resize
import numpy as np
import csv
import pandas as pd


data = pd.read_csv('data3.csv', delimiter=';
                   ')
"""with open('data3.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append({
            "id": row['id'],
            "name": row['name'],
            "price": row['price'],
            "rate": row['rate'],
            "sold": row['sold'],
            "tags": row['tags']
        })"""

print(data)

