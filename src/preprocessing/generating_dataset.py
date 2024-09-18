import json
import os
import random

from preprocessing.corrupting import (
    corrupt_object_references,
    randomly_corrupt_pdf,
    remove_pdf_markers,
    truncate_pdf,
)

input_folder = "./input/pdfs"


def corrupt_pdf_dataset(output_folder, corruption_methods):
    """Apply corruption to all PDFs in the dataset."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    log = []

    for pdf_file in os.listdir(os.path.join(os.getcwd(), input_folder)):
        if pdf_file.endswith(".pdf"):
            input_path = os.path.join(input_folder, pdf_file)
            output_path = os.path.join(output_folder, f"corrupted_{pdf_file}")
            # Apply a corruption method from the list
            method = random.choice(corruption_methods)
            method(input_path, output_path)
            print(f"Corrupted {pdf_file} and saved to {output_path}.")
            log.append({"file": pdf_file, "method": method.__name__})

    # Save the log to a JSON file
    log_path = os.path.join(output_folder, "corruption_log.json")
    with open(log_path, "w") as log_file:
        json.dump(log, log_file, indent=2)
    print(f"Corruption log saved to {log_path}.")
