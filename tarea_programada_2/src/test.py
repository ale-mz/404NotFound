import os
import numpy as np
import matplotlib.pyplot as plt

# Read data from data.csv
current_directory = os.getcwd()
file_name = "data.csv"
data_path = os.path.join(current_directory, file_name)

with open(data_path, "r") as csv_file:
    # Assuming each line in data.csv contains a numerical value
    data = [float(line.strip()) for line in csv_file]

# Create a histogram
plt.hist(data, bins=30, density=True, alpha=0.7, color='b', edgecolor='black')

# Add a title and labels
plt.title("Distribution of Data")
plt.xlabel("Values")
plt.ylabel("Frequency")

# Show the plot
plt.show()
