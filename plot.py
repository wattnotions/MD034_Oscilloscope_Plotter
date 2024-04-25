import os
import pandas as pd
import matplotlib.pyplot as plt
import inquirer

def list_csv_files(directory):
    # List all files in the directory and filter for CSV files
    return [file for file in os.listdir(directory) if file.endswith('.csv')]

def load_and_plot_data(files):
    plt.figure(figsize=(10, 5))

    # Loop through the list of file paths
    for file_path in files:
        # Load data from the file, skipping the initial non-data rows
        data = pd.read_csv(file_path, skiprows=20)
        # Clean up column names in case there are any leading or trailing whitespaces
        data.columns = data.columns.str.strip()

        # Plotting the data
        plt.plot(data['TIME'], data['CH2'], label=os.path.basename(file_path))

    plt.title('Time Series Data for Selected Files')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    # Get the current directory of the script
    current_directory = os.getcwd()

    # List CSV files in the current directory
    csv_files = list_csv_files(current_directory)

    # If no CSV files are found, print a message and exit
    if not csv_files:
        print("No CSV files found in the directory.")
        return

    # Use inquirer to let the user select multiple CSV files
    questions = [
        inquirer.Checkbox('files',
                          message="Select up to 5 CSV files to plot (use space to select, enter to finalize)",
                          choices=csv_files,
                          validate=lambda _, x: len(x) <= 5,
                          ),
    ]
    answers = inquirer.prompt(questions)

    # Generate full paths for the selected files
    selected_files = [os.path.join(current_directory, file) for file in answers['files']]

    # Load and plot data from the selected files
    load_and_plot_data(selected_files)

if __name__ == "__main__":
    main()
