import csv
import joblib
import numpy as np
from skimage import io
from skimage.transform import resize
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

cat_list = [
    "беспроводные наушники",
    "женская футболка",
    "женские кроссовки",
    "светодиодная лента",
    "чехол на телефон",
]


def read_image(id: int):
    """
    Загрузка и привидение изображений к одному размеру
    """
    image = io.imread(f"categories\{category}\images\image_{id}.jpg")
    return resize(image, (100, 100)).flatten()


for category in cat_list:
    data = []

    with open(
        f"categories/{category}/data.csv", newline="", encoding="utf-8"
    ) as csvfile:
        for row in csv.DictReader(csvfile, delimiter=";"):
            data.append(
                {
                    "id": row["id"],
                    "name": row["name"],
                    "sold": int(row["sold"]),
                    "price": int(row["price"]),
                    "tags": (row["tags"]),
                }
            )

    data = data[-30:]
    image_features = []
    text_features = []

    for item in data:
        image_features.append(read_image(int(item["id"])))
        text_features.append(item["name"] + " " + item["tags"])

    vectorizer = TfidfVectorizer()

    text_features = np.array(vectorizer.fit_transform(text_features).toarray())
    price_feature = np.array([item["price"] for item in data])[:, np.newaxis]

    # Объединение признаков
    X = np.concatenate((image_features, text_features, price_feature), axis=1)
    y = np.array([item["sold"] for item in data])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_jobs=-1, verbose=5, min_samples_leaf=2, n_estimators=30, max_depth=6
    )

    model.fit(X_train, y_train)

    joblib.dump(model, f"{category}.joblib")
    print("сохранение")
