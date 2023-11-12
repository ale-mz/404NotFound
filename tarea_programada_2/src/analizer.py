import os

class Analizer():
    def __init__(self):
        self.__data = None
    
    def analize(self, technique):
        # TODO: implement the data param, could be either the default file or the user's file
        print("Analizing data...")

        # TODO: add a switch case to call the corresponding technique that calls a subroutine for each technique
        switch_values = {
            0: self.brute_force,
            1: self.heuristic,
            2: self.genetic_algorithm
        }

        # Call the corresponding technique
        switch_values.get(technique, self.default_option)()


    # TODO: implement the brute force technique
    def brute_force(self):
        print("Brute force technique")

    # TODO: implement the heuristic technique
    def heuristic(self):
        print("Heuristic technique")

    # TODO: implement the genetic algorithm technique
    def genetic_algorithm(self):
        print("Genetic algorithm technique")

    def default_option(self):
        print("Invalid technique")

    def save_data(self, analyzed_data):
        current_directory = os.getcwd() # Get the current working directory
        file_name = "data.csv" # Define the file name
        data_path = os.path.join(current_directory, file_name) # Create the path using the os package

        # Convert numerical values to strings and concatenate with newline character
        csv_content = analyzed_data

        # Clear the existing content and write the new content to data.csv
        with open(data_path, "w") as csv_file:
            csv_file.write(csv_content)