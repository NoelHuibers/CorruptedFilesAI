import os
import random


def select_training_testing_data(original_folder, corrupted_folder, X):
    """
    Split the data into training and testing sets.
    X represents the amount of data to be used for training.
    """
    # List all files in the original and corrupted folders
    original_files = [f for f in os.listdir(original_folder) if f.endswith(".pdf")]
    corrupted_files = [f for f in os.listdir(corrupted_folder) if f.endswith(".pdf")]

    # Create a random split for training data
    total_files = len(original_files)
    num_train = int(X * total_files)

    # Shuffle and select a 50/50 split
    file_indices = list(range(total_files))
    random.shuffle(file_indices)

    train_indices = file_indices[:num_train]
    test_indices = file_indices[num_train:]

    train_data = [(original_files[i], corrupted_files[i]) for i in train_indices]
    test_data = [(original_files[i], corrupted_files[i]) for i in test_indices]

    return train_data, test_data
