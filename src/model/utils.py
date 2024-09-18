import csv
import json
import os

from matplotlib import pyplot as plt


def extract_hex_from_pdf(file_path):
    with open(file_path, "rb") as file:
        hex_data = file.read().hex()
    return hex_data


def hex_to_numeric(hex_str):
    """
    Convert a hex string to a numerical feature by summing the ASCII values of the characters.
    """
    return sum(ord(c) for c in hex_str)


def load_corruption_log(corrupted_folder):
    """
    Load the corruption log from the corrupted folder.
    """
    corruption_log_path = os.path.join(corrupted_folder, "corruption_log.json")
    with open(corruption_log_path, "r") as f:
        corruption_log = json.load(f)
    return corruption_log


def save_results_to_csv(overall_accuracy, corruption_stats, output_folder):
    """
    Save overall accuracy and corruption detection rates to a CSV file in the /output folder.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    output_file = os.path.join(output_folder, "results.csv")

    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Metric", "Value"])
        writer.writerow(["Overall Accuracy", f"{overall_accuracy:.2f}"])
        writer.writerow([])
        writer.writerow(["Corruption Type", "Detection Rate"])
        for corruption_type, rate in corruption_stats.items():
            writer.writerow([corruption_type, f"{rate:.2f}"])


def plot_results(csv_file, plot_output_folder):
    """
    Generate a plot from the CSV file and save it as an image in the /output/plots folder.
    """
    if not os.path.exists(plot_output_folder):
        os.makedirs(plot_output_folder)

    corruption_types = []
    detection_rates = []
    overall_accuracy = 0.0

    with open(csv_file, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        overall_accuracy = float(next(reader)[1])

        for row in reader:
            if row and row[0] == "Corruption Type":
                break

        for row in reader:
            if row:
                corruption_types.append(row[0])
                detection_rates.append(float(row[1]))

    plt.figure(figsize=(10, 6))
    plt.bar(["Overall Accuracy"], [overall_accuracy], color="skyblue")

    plt.bar(corruption_types, detection_rates, color="lightcoral")

    plt.ylabel("Accuracy")
    plt.title("Model Accuracy and Corruption Type Detection Rates")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plot_file = os.path.join(plot_output_folder, "corruption_detection_rates.png")
    plt.savefig(plot_file)

    plt.close()
