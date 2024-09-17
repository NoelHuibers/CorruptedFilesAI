def extract_hex_from_pdf(file_path):
    with open(file_path, "rb") as file:
        hex_data = file.read().hex()
    return hex_data
