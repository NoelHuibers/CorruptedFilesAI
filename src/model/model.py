import os

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from model.features import extract_features_with_hex
from model.utils import load_corruption_log


def prepare_dataset(original_folder, corrupted_folder, data_split):
    """
    Prepare the dataset by extracting features from both original and corrupted PDFs,
    and include the corruption type.
    """
    features = []
    labels = []
    corruption_types = []

    # Load the corruption log
    corruption_log = load_corruption_log(corrupted_folder)

    # Create a mapping of original file names to corruption types
    corruption_mapping = {entry["file"]: entry["method"] for entry in corruption_log}

    for original_file, corrupted_file in data_split:
        # Extract features from the original PDF (label 0, non-corrupted)
        original_features = extract_features_with_hex(
            os.path.join(original_folder, original_file)
        )
        features.append(original_features)
        labels.append(0)  # Label 0 for non-corrupted file
        corruption_types.append("original")  # No corruption for the original file

        corrupted_features = extract_features_with_hex(
            os.path.join(corrupted_folder, corrupted_file)
        )
        features.append(corrupted_features)
        labels.append(1)  # Label 1 for corrupted file

        # Add the corruption type from the log
        corruption_type = corruption_mapping.get(
            corrupted_file.replace("corrupted_", ""), "unknown"
        )
        corruption_types.append(corruption_type)

    # Convert to a DataFrame for easier manipulation
    feature_df = pd.DataFrame(features)
    return feature_df, np.array(labels), np.array(corruption_types)


def train_model(X_train, y_train):
    """
    Train a RandomForestClassifier on the training data.
    """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test, corruption_types):
    """
    Evaluate the model on the test data and compute detection rates per corruption type.
    """
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    corruption_stats = {}

    for corruption_type in np.unique(corruption_types):
        indices = corruption_types == corruption_type
        correct_predictions = (y_pred[indices] == y_test[indices]).sum()
        total_predictions = indices.sum()
        corruption_stats[corruption_type] = correct_predictions / total_predictions

    return accuracy, corruption_stats
