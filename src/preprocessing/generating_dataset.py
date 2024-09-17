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

    for pdf_file in os.listdir(os.path.join(os.getcwd(), input_folder)):
        if pdf_file.endswith(".pdf"):
            input_path = os.path.join(input_folder, pdf_file)
            output_path = os.path.join(output_folder, f"corrupted_{pdf_file}")
            # Apply a corruption method from the list
            random.choice(corruption_methods)(input_path, output_path)
            print(f"Corrupted {pdf_file} and saved to {output_path}.")
