import os
import pandas as pd
import matplotlib.pyplot as plt
import inquirer

def list_csv_files(directory):
    # List all files in the directory and filter for CSV files
    return [file for file in os.listdir(directory) if file.endswith('.csv')]

def load_and_plot_data(file_path):
    # Load data from the file, skipping the initial non-data rows
    data = pd.read_csv(file_path, skiprows=20)

    # Clean up column names in case there are any leading or trailing whitespaces
    data.columns = data.columns.str.strip()

    # Plotting the data
    plt.figure(figsize=(10, 5))
    plt.plot(data['TIME'], data['CH2'], label='Channel 2', color='blue')
    plt.title('Time Series Data for Channel 2')
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

    # Use inquirer to let the user select a CSV file
    questions = [
        inquirer.List('file',
                      message="Select which CSV file to plot",
                      choices=csv_files,
                      ),
    ]
    answers = inquirer.prompt(questions)

    # Load and plot data from the selected file
    load_and_plot_data(os.path.join(current_directory, answers['file']))

if __name__ == "__main__":
    main()
