import os
import csv
import numpy as np

class Analyzer():
    def __init__(self):
        self.__data = None
    
    def analyze(self, technique):
        # TODO: implement the data param, could be either the default file or the user's file
        print("Analyzing data...")

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
        data_content = self.read_data_from_csv()
        # print(data_content)

    def heuristic(self):
        print("Heuristic technique")
        data_content = self.read_data_from_csv()
        size_data = len(data_content)
        match_counter = 0

        data_content.sort()
        team_1 = []
        team_2 = []

        # store the data in the data.csv file
        current_directory = os.getcwd() # Get the current working directory
        file_name = "data.csv" # Define the file name
        data_path = os.path.join(current_directory, file_name) # Create the path using the os package
        
        with open(data_path, 'w') as file:
            file.write('')

        for i in range(size_data):
            # clean the arrays
                
            counter = i % 10
            is_team_1 = counter == 0 or counter == 3 or counter == 4 or counter == 7 or counter == 8
            is_team_2 = counter == 1 or counter == 2 or counter == 5 or counter == 6 or counter == 9
            if  is_team_1:
                team_1.append(data_content[i])
            else:
                team_2.append(data_content[i])

            if i % 10 == 0 and i != 0:
                
                # print("Team 1: ", team_1)
                # print("Team 2: ", team_2)

                # TODO: add the average value of each team/match ?

                # store the data in the data.csv file
                current_directory = os.getcwd() # Get the current working directory
                file_name = "data.csv" # Define the file name
                data_path = os.path.join(current_directory, file_name) # Create the path using the os package
        
                csv_content = '[' + ', '.join(map(str, team_1)) + ']' + " VS " + '[' + ', '.join(map(str, team_2)) + ']' + "\n"    # write the content of data.csv into the csv_content variable
                # ""    # write the content of data.csv into the csv_content variable
                # data.sort()
                # Convert numerical values to strings and concatenate with newline character
                # csv_content = "\n".join(map(str, data))

                # Clear the existing content and write the new content to data.csv
                with open(data_path, "a") as csv_file:
                    csv_file.write(csv_content)

                team_1.clear()
                team_2.clear()
            

    # TODO: implement the genetic algorithm technique
    def genetic_algorithm(self):
        # create the original population
        data_content = self.read_data_from_csv()
        # population_size must be divided by 10 because each individual has 10 values
        population_size = len(data_content)/10
        # cast the population_size to int
        population_size = int(population_size)
        population = [self.generate_individual(data_content) for _ in range(population_size)]
        new_population = []


        counter = 0
        max_generations = 10
        while counter < max_generations:
            print(f"Generation: {counter}")
            self.calculate_fitness(population)

            population = sorted(population, key=lambda x: x['fitness'], reverse=True)
            # Calculate the index to get the top 5%
            top_5_percent_index = int(len(population) * 0.05)
            # Get the top 5% individuals
            top_5_percent = population[:top_5_percent_index]
            # get the best 5% of the population and copy them to the next generation
            new_population[:top_5_percent_index] = top_5_percent
            population = population[top_5_percent_index:]

            population = sorted(population, key=lambda x: x['greatness'], reverse=True)

            # TODO: apply the crossover operation to the population and store the result in new_population
            for i in range(0, len(population)-1, 2):
                # print(f"Individual {i}")
                self.calculate_fitness(population)
                self.calculate_greatness(population)
                parent1 = population[i]
                parent2 = population[i + 1]

                # Perform crossover between parent1 and parent2
                child1, child2 = self.crossover(parent1, parent2)

                # Add the children to the new population
                new_population.append(child1)
                new_population.append(child2)

            if len(population) % 2 != 0:
                odd_one = population[-1]


            # set the new population as the current population and clear the new population
            population = new_population
            new_population = []
            counter += 1
        
        # store the data in the data.csv file
        #cast the population to str
        # population = str(population)
        matches_string = ""
        for individual in population:
            match = individual['match']
            matches_string += f"{match[0]} VS {match[1]} with fitness of {individual['fitness']}\n"
        self.save_data(matches_string)
        print("Genetic algorithm technique")

    def crossover(self, parent1, parent2):
        # Get the match of each parent
        match1 = parent1['match']
        match2 = parent2['match']

        # Get the teams of each match
        team1_parent1 = match1[0]
        team2_parent1 = match1[1]
        team1_parent2 = match2[0]
        team2_parent2 = match2[1]

        # put all element of the teams in a single array, shuffle it and split it in 4 new teams
        all_teams = team1_parent1 + team2_parent1 + team1_parent2 + team2_parent2
        np.random.shuffle(all_teams)
        team1_child1 = all_teams[:5]
        team2_child1 = all_teams[5:10]
        team1_child2 = all_teams[10:15]
        team2_child2 = all_teams[15:20]
        child1 = {'match': [team1_child1, team2_child1], 'fitness': 0, 'greatness': 0}
        child2 = {'match': [team1_child2, team2_child2], 'fitness': 0, 'greatness': 0}
        return child1, child2

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

    def read_data_from_csv(self):
        data_array = []

        current_directory = os.getcwd() # Get the current working directory
        file_name = "data.csv" # Define the file name
        file_path = os.path.join(current_directory, file_name) # Create the path using the os package

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            # csv_reader = csv.reader(csvfile, delimiter='|', skipinitialspace=True)
            for row in csv_reader:
                # Assuming the numerical value is at the beginning of each line
                # numerical_value = int(row[1])
                numerical_value = int(row[0])

                data_array.append(numerical_value)

        return data_array

    def generate_individual(self, data_content):
        # Generate a random match (two teams of 5 candidates each)
        # np.random.shuffle(data_content)
        sub_data = data_content[:10]
        data_content = data_content[10:]
        match = [sub_data[:5], sub_data[5:]]
        fitness = 0
        greatness = 0
        # with open("data.txt", 'a') as file:
        #     file.write(f"Match: {match}, Fitness: {fitness}\n")
        return {'match': match, 'fitness': fitness, 'greatness': greatness}
    
    def calculate_greatness(self, population):
        for individual in population:
            match = individual['match']
            greatness = sum(match[0]) + sum(match[1])/10
            # greatness is the average value of the match
            individual['greatness'] = greatness

    def calculate_fitness(self, population):
        for individual in population:
            match = individual['match']
            fitness = 0
            team_1 = match[0]
            team_2 = match[1]
            # FIXME: difference msut be the difference between the biggest and the smallest value of the team
            difference_team_1 = abs(sum(team_1) - len(team_1)*np.mean(team_1))
            difference_team_2 = abs(sum(team_2) - len(team_2)*np.mean(team_2))
            difference_match = abs(sum(team_1) - sum(team_2))
            fitness = difference_team_1 + difference_team_2 + difference_match
            individual['fitness'] = fitness