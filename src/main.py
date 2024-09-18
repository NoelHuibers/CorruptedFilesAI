from preprocessing.collectingpdfs import collect_pdfs, shorten_filenames
from preprocessing.corrupting import (
    corrupt_object_references,
    randomly_corrupt_pdf,
    remove_pdf_markers,
    truncate_pdf,
)
from preprocessing.generating_dataset import corrupt_pdf_dataset


def main():
    #
    # PREPROCESSING
    #
    # For collecting from an API found on Kaggle
    # collect_pdfs()
    #
    # For shortening the filenames (Windows has a limit of 260 characters for file paths)
    # shorten_filenames()
    #
    # For corrupting the PDFs
    corruption_methods = [
        randomly_corrupt_pdf,
        remove_pdf_markers,
        truncate_pdf,
        corrupt_object_references,
    ]
    corrupt_pdf_dataset("./input/corrupted", corruption_methods)


if __name__ == "__main__":
    main()
