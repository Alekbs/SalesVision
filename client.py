import joblib
import numpy as np
from skimage import io
from skimage.transform import resize
from sklearn.feature_extraction.text import TfidfVectorizer


def read_image(image_path: str):
    """
    Загрузка и привидение изображений к одному размеру
    """
    image = io.imread(image_path)
    return resize(image, (100, 100)).flatten()


def predict(name_model, image_path, name, price, size):
    """
    Предсказание для нового товара
    """
    model = joblib.load(name_model)
    model.verbose = 0

    image_features = [read_image(image_path)]
    text_features = [name]
    prices = [[int(price)]]

    # Векторизация текста
    vectorizer = TfidfVectorizer()
    text_features = vectorizer.fit_transform(text_features).toarray()
    text_features = np.resize(text_features, (1, size))

    X = np.concatenate((image_features, text_features, prices), axis=1)
    predicted_sales = model.predict(X)

    return int(predicted_sales)
