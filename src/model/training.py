from collections import Counter

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


def hex_to_feature_vector(hex_data):
    byte_freq = Counter(hex_data[i : i + 2] for i in range(0, len(hex_data), 2))
    feature_vector = [byte_freq.get(f"{i:02x}", 0) for i in range(256)]
    return feature_vector


def train_model(features, labels):
    X_train, X_test, y_train, y_test = train_test_split(
        features, labels, test_size=0.2, random_state=42
    )

    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))
