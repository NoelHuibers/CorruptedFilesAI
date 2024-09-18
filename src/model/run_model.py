import os

from model.model import evaluate_model, prepare_dataset, train_model
from model.selecting import select_training_testing_data
from model.utils import plot_results, save_results_to_csv


def run_pipeline(original_folder, corrupted_folder, X):
    """
    Full pipeline for training and testing the model.
    """
    # Step 1: Select training and testing data
    print("Selecting training and testing data...")
    train_data, test_data = select_training_testing_data(
        original_folder, corrupted_folder, X
    )

    # Step 2: Prepare the dataset (extract features and labels)
    print("Preparing the dataset...")
    X_train, y_train, _ = prepare_dataset(original_folder, corrupted_folder, train_data)
    X_test, y_test, corruption_types_test = prepare_dataset(
        original_folder, corrupted_folder, test_data
    )

    # Step 3: Train the model
    print("Training the model...")
    model = train_model(X_train, y_train)

    # Step 4: Evaluate the model
    print("Evaluating the model...")
    overall_accuracy, corruption_stats = evaluate_model(
        model, X_test, y_test, corruption_types_test
    )

    # Print and plot the results
    print(f"Overall Accuracy={overall_accuracy:.2f}%")
    print("Corruption Detection Rates:")
    for corruption_type, rate in corruption_stats.items():
        print(f"  {corruption_type}: {rate:.2f}%")

    # Save the results to CSV
    output_folder = "./output"
    save_results_to_csv(overall_accuracy, corruption_stats, output_folder)

    # Generate the plot from the CSV and save it
    plot_output_folder = os.path.join(output_folder, "plots")
    csv_file = os.path.join(output_folder, "results.csv")
    plot_results(csv_file, plot_output_folder)

    print(f"Results saved to {output_folder}, and plot saved to {plot_output_folder}")

    return overall_accuracy, corruption_stats
