import os

class Analizer():
    def __init__(self):
        self.__data = None
    
    def analize(self, technique):
        # TODO: implement the data param, could be either the default file or the user's file
        print("Analizing data...")

        # TODO: add a switch case to call the corresponding technique that calls a subroutine for each technique

        # TODO: update the data.csv file with the analyzed_data
        current_directory = os.getcwd() # Get the current working directory
        file_name = "data.csv" # Define the file name
        data_path = os.path.join(current_directory, file_name) # Create the path using the os package

        # Convert numerical values to strings and concatenate with newline character
        csv_content = "analyzed_data\n" # TODO: changed to actual analyzed data

        # Clear the existing content and write the new content to data.csv
        with open(data_path, "w") as csv_file:
            csv_file.write(csv_content)