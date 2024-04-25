import pandas as pd
import matplotlib.pyplot as plt

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

# Path to your CSV file
file_path = '3.8_non_wp_open.csv'

# Call the function with the path to your file
load_and_plot_data(file_path)
