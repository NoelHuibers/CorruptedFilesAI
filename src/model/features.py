from collections import Counter


def hex_to_feature_vector(hex_data):
    byte_freq = Counter(hex_data[i : i + 2] for i in range(0, len(hex_data), 2))
    feature_vector = [byte_freq.get(f"{i:02x}", 0) for i in range(256)]
    return feature_vector


def extract_features_with_hex(file_path):
    with open(file_path, "rb") as file:
        data = file.read()
    return hex_to_feature_vector(data.hex())
