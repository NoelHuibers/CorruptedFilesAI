import random
import re


def randomly_corrupt_pdf(file_path, output_path, corruption_rate=0.01):
    """Randomly corrupts a percentage of the bytes in a PDF."""
    with open(file_path, "rb") as file:
        data = bytearray(file.read())

    num_bytes_to_corrupt = int(len(data) * corruption_rate)
    for _ in range(num_bytes_to_corrupt):
        rand_index = random.randint(0, len(data) - 1)
        rand_byte = random.randint(0, 255)
        data[rand_index] = rand_byte

    with open(output_path, "wb") as out_file:
        out_file.write(data)
    print(f"Corrupted {num_bytes_to_corrupt} bytes and saved to {output_path}.")


def remove_pdf_markers(file_path, output_path, markers=["%PDF", "%%EOF"]):
    """Remove key markers like %PDF and %%EOF from the file."""
    with open(file_path, "rb") as file:
        data = file.read().decode(errors="ignore")

    for marker in markers:
        data = data.replace(marker, "")

    with open(output_path, "wb") as out_file:
        out_file.write(data.encode())
    print(f"Removed markers {markers} and saved to {output_path}.")


def truncate_pdf(file_path, output_path, percentage=0.9):
    """Truncate the PDF file to a certain percentage of its original size."""
    with open(file_path, "rb") as file:
        data = file.read()

    truncated_data = data[: int(len(data) * percentage)]

    with open(output_path, "wb") as out_file:
        out_file.write(truncated_data)
    print(
        f"Truncated file to {percentage*100}% of its original size and saved to {output_path}."
    )


def corrupt_object_references(file_path, output_path):
    """Tamper with object references in the PDF file."""
    with open(file_path, "rb") as file:
        data = file.read().decode(errors="ignore")

    corrupted_data = re.sub(r"\d+ \d+ obj", "9999 9999 obj", data)

    with open(output_path, "wb") as out_file:
        out_file.write(corrupted_data.encode())
    print(f"Corrupted object references and saved to {output_path}.")


def corrupt_pdf_combined(file_path, output_path):
    """Combine multiple corruption techniques on the PDF."""
    randomly_corrupt_pdf(file_path, "temp_random_corrupted.pdf")
    remove_pdf_markers("temp_random_corrupted.pdf", "temp_marker_removed.pdf")
    truncate_pdf("temp_marker_removed.pdf", output_path, percentage=0.8)
    print(f"Applied combined corruption and saved to {output_path}.")
