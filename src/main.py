from preprocessing.collectingpdfs import collect_pdfs
from preprocessing.corrupting import (
    corrupt_object_references,
    randomly_corrupt_pdf,
    remove_pdf_markers,
    truncate_pdf,
)
from preprocessing.generating_dataset import corrupt_pdf_dataset


def main():
    # collect_pdfs() For collecting from an API found on Kaggle
    corruption_methods = [
        randomly_corrupt_pdf,
        remove_pdf_markers,
        truncate_pdf,
        corrupt_object_references,
    ]
    corrupt_pdf_dataset("./input/corrputedpdfs", corruption_methods)


if __name__ == "__main__":
    main()
