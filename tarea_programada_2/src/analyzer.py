import os
import csv
from itertools import combinations
import numpy as np
from itertools import permutations

class Team():
    players = [0,0,0,0,0]
    mean = 0
    var = 0

class Match():
    def __init__(self):
        self.team1 = Team()  # Initialize team1 as an instance of the Team class
        self.team2 = Team()  # Initialize team2 as an instance of the Team class
        self.diff = 0

def team_fix(input_team: Team):
        # First, get mean of team
        ref_mean = 0
        for player in range(5):
            ref_mean += input_team.players[player]
        ref_mean /= 5
        input_team.mean = ref_mean

        # Second, get var
        ref_var = 0
        for player in range(5):
            ref_var += (ref_mean - input_team.players[player]) * (ref_mean - input_team.players[player])
        ref_var /= 5
        input_team.var = ref_var

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
        size_data = len(data_content)
        
        # best_solution = []
        
        # itertools makes an iterable object that keep making new combinations
        # at the time the code is iterating over it
        combinations_table = permutations(data_content, size_data)
        
        for iteration, permutation in enumerate(combinations_table):
            print(f"Solucion #{iteration}: {permutation}")
            
            # make the fitness 
            
            # compare 
            
            # store the best one
            # if (actual > best_solution)
                # best_solutiob = list(permutation)
            
        
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
                
                print("Team 1: ", team_1)
                print("Team 2: ", team_2)

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
        # create array with match
        matchmaking = [Match() for i in range(population_size)]

        # Load matchmaking
        generations = 0
        fitness = 5
        mean_ac = 0
        for match in range(population_size):
            # First Team
            matchmaking[match].team1.players = data_content[match*10:match*10 + 5]
            team_fix(matchmaking[match].team1)
            # Second Team
            matchmaking[match].team2.players = data_content[match*10 + 5:(match + 1)*10]
            team_fix(matchmaking[match].team2)
            # Add diff
            diff = matchmaking[match].team1.mean - matchmaking[match].team2.mean
            if (diff < 0):
                diff *= -1
            matchmaking[match].diff = diff
            mean_ac += diff
        fitness  = mean_ac / population_size
        print("fitness: ", fitness)

        while (fitness > 1) :
            # Cross-Over Teams
            print("Crossover Teams\n")
            for match in range(population_size):
                target = Match()
                target = matchmaking[match]
                # Load both teams in one array
                load = target.team1.players + target.team2.players
                # Sort array, lowest gone to first array, highest to second one
                load.sort()
                matchmaking[match].team1.players = load[:5]
                matchmaking[match].team2.players = load[5:]
                team_fix(matchmaking[match].team1)
                team_fix(matchmaking[match].team2)

                fitness -= matchmaking[match].diff / population_size

                diff = matchmaking[match].team1.mean - matchmaking[match].team2.mean
                if (diff < 0):
                    diff *= -1
                matchmaking[match].diff = diff
                fitness += matchmaking[match].diff / population_size

            # Mutation
            for match in range(population_size-1):
                target = matchmaking[match]
                # Look for a better team
                for index in range(match + 1, population_size):
                    candidate = matchmaking[index]
                    df = target.team1.mean - candidate.team1.mean
                    # Reverse it if df is negative
                    if (df < 0):
                        df *= -1
                    if (df < 1):

                        # Change matchmaking parameters
                        fitness -= matchmaking[match].diff / population_size
                        fitness -= matchmaking[index].diff / population_size

                        # Lower team
                        higher = matchmaking[match].team2
                        matchmaking[match].team2 = matchmaking[index].team1
                        matchmaking[index].team1 = higher
                        
                        # Change match parameters
                        difference1 = matchmaking[match].team1.mean - matchmaking[match].team2.mean
                        if (difference1 < 0):
                            difference1 *= -1
                        matchmaking[match].diff = difference1

                        difference2 = matchmaking[index].team1.mean - matchmaking[index].team2.mean
                        if (difference2 < 0):
                            difference2 *= -1
                        matchmaking[index].diff = difference2

                        # Update matchmaking parameters
                        fitness += matchmaking[match].diff / population_size
                        fitness += matchmaking[index].diff / population_size
                        break

            generations += 1
            print("Fitness: ", fitness)

        # store the data in the data.csv file
        current_directory = os.getcwd() # Get the current working directory
        file_name = "data.csv" # Define the file name
        data_path = os.path.join(current_directory, file_name) # Create the path using the os package
        
        with open(data_path, 'w') as file:
            file.write('')

        retry_matching = 0
        for match in range(population_size):
            print(matchmaking[match].team1.players)
            csv_content = str(matchmaking[match].team1.players)
            print(" vs ")
            csv_content += " VS "
            print(matchmaking[match].team2.players)
            csv_content += str(matchmaking[match].team2.players)
            print("\n")
            csv_content += "\n"
            if (matchmaking[match].diff > 3):
                retry_matching +=1
            with open(data_path, "a") as csv_file:
                csv_file.write(csv_content)

        print("Generations: ", generations)
        print("Retrying Match: ", retry_matching)
        print("Porcentage: ", retry_matching / population_size, "%")

        accumulative = 0
        for match in range(population_size):
            team_fix(matchmaking[match].team1)
            team_fix(matchmaking[match].team2)
            diff = matchmaking[match].team1.mean - matchmaking[match].team2.mean
            if (diff < 0):
                diff *= -1
            accumulative += diff
        print("Fitness: ", accumulative / population_size)

        # store the data in the data.csv file
        # self.save_data(population)
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
        # create array with match
        matchmaking = [Match() for i in range(len(population))]
        # Load matchmaking
        fitness = 5
        mean_ac = 0
        for match in range(len(population)):
            # First Team
            matchmaking[match].team1.players = population[match*10:match*10 + 5]
            team_fix(matchmaking[match].team1)
            # Second Team
            matchmaking[match].team2.players = population[match*10 + 5:(match + 1)*10]
            team_fix(matchmaking[match].team2)
            # Add diff
            diff = matchmaking[match].team1.mean - matchmaking[match].team2.mean
            if (diff < 0):
                diff *= -1
            matchmaking[match].diff = diff
            mean_ac += diff
        fitness  = mean_ac / len(population)
        return fitness