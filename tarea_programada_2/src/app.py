import tkinter
import tkinter.messagebox
import customtkinter
import os
import numpy as np
import matplotlib.pyplot as plt
from analizer import Analizer

np.set_printoptions(precision=8, suppress=True, threshold=np.inf)
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# custom_theme_path = "C:/Users/archi/Documents/GitHub/tareas-programadas-404-not-found/tarea_programada_2/src/custom_theme.json"

# TODO: Add our own custom theme instead of using the default one
# current_directory = os.getcwd() # Get the current working directory
# file_name = "custom_theme.json" # Define the file name
# custom_theme_path = os.path.join(current_directory, file_name) # Create the path using the os package
# customtkinter.set_default_color_theme(custom_theme_path)  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Match making system")
        self.geometry(f"{1480}x{720}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        # self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # left side bar section

        # create and configure the sidebar frame
        self.left_sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.left_sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.left_sidebar_frame.grid_rowconfigure(5, weight=1)

        # create and configure the logo label
        self.logo_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="Match making system", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))   # set the logo at the top of the left column

        # create and configure the appearance option menu and label
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.left_sidebar_frame, values=["Light", "Dark", "System"],
                                                                    command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=2, column=0, padx=20, pady=(0, 10))  # Removed padding at the bottom
        self.appearance_mode_optionemenu.set("Dark")
        self.appearance_mode_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="Appearance Mode: ", anchor="w")
        self.appearance_mode_label.grid(row=1, column=0, padx=20, pady=(0, 10))

        # create and configure the scaling option menu and label
        self.scaling_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=3, column=0, padx=20, pady=(10, 5))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.left_sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                            command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=4, column=0, padx=20, pady=(5, 10))  # Removed padding at the bottom
        self.scaling_optionemenu.set("100%")

        # created and configure the quit button
        self.quit_button = customtkinter.CTkButton(self.left_sidebar_frame, command=self.quit_simulation_event)
        self.quit_button.grid(row=6, column=0, padx=20, pady=(10, 40))
        self.quit_button.configure(state="enabled", text="Quit simulation")





        # DATA PREVIEW SECTIONS
        # create csv content preview
        self.csv_preview = customtkinter.CTkTextbox(self, width=250)
        self.csv_preview.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        csv_content = ""    # write the content of data.csv into the csv_content variable
        current_directory = os.getcwd() # Get the current working directory
        file_name = "data.csv" # Define the file name
        data_path = os.path.join(current_directory, file_name) # Create the path using the os package

        with open(data_path, "r") as csv_file:
            csv_content = csv_file.read()
        
        # print(csv_content)
        # TODO: implement a prettify function for the csv content

        # self.csv_preview.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consektetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        self.csv_preview.insert("0.0", csv_content)

        # Create the outer frame (self.right_sidebar_frame)
        self.right_sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        self.right_sidebar_frame.grid_rowconfigure(5, weight=1)


        # CHOOSING THE POPULATION DISTRIBUTION SECTION
        self.population_distribution = customtkinter.CTkFrame(master=self.right_sidebar_frame)
        self.population_distribution.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # Create a variable to hold the selected radio button value
        self.population_distribution_value = tkinter.IntVar(value=0)

        # Create radio buttons
        self.distribution_label = customtkinter.CTkLabel(master=self.population_distribution, text="Choose the population distribution:")
        self.distribution_label.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="w")

        # self.linear_distribution = customtkinter.CTkRadioButton(master=self.population_distribution, variable=self.radio_var, value=0, text="Linear distribution")
        # self.linear_distribution.grid(row=1, column=2, pady=10, padx=20, sticky="w")
        self.normal_distribution = customtkinter.CTkRadioButton(master=self.population_distribution, variable=self.population_distribution_value, value=0, text="Normal distribution")
        self.normal_distribution.grid(row=2, column=2, pady=10, padx=20, sticky="w")
        self.bimodal_distribution = customtkinter.CTkRadioButton(master=self.population_distribution, variable=self.population_distribution_value, value=1, text="Bimodal distribution")
        self.bimodal_distribution.grid(row=3, column=2, pady=10, padx=20, sticky="w")



        # CHOOSING THE POPULATION SIZE SECTION
        self.population_size = customtkinter.CTkFrame(master=self.right_sidebar_frame)
        self.population_size.grid(row=1, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # Create a variable to hold the selected radio button value
        self.population_size_value = tkinter.IntVar(value=0)

        # Create radio buttons
        self.size_label = customtkinter.CTkLabel(master=self.population_size, text="Choose the population size:")
        self.size_label.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="w")

        self.small_population = customtkinter.CTkRadioButton(master=self.population_size, variable=self.population_size_value, value=0, text="Small population (10000)")
        self.small_population.grid(row=1, column=2, pady=10, padx=20, sticky="w")
        self.medium_population = customtkinter.CTkRadioButton(master=self.population_size, variable=self.population_size_value, value=1, text="Medium population (100000)")
        self.medium_population.grid(row=2, column=2, pady=10, padx=20, sticky="w")
        self.large_population = customtkinter.CTkRadioButton(master=self.population_size, variable=self.population_size_value, value=2, text="Large population (1000000)")
        self.large_population.grid(row=3, column=2, pady=10, padx=20, sticky="w")

        # BUTTON CREATE POPULATION
        self.create_population = customtkinter.CTkButton(master=self.right_sidebar_frame, command=self.create_population_event) # TODO: change the function
        self.create_population.grid(row=2, column=2, padx=20, pady=(20, 40))
        self.create_population.configure(state="enabled", text="Create population")

        # CHOOSING SOLVING TECHNIQUE SECTION
        # Create the inner frame (self.technique_choice)
        self.technique_choice = customtkinter.CTkFrame(master=self.right_sidebar_frame)
        self.technique_choice.grid(row=3, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # Create a variable to hold the selected radio button value
        self.technique_used = tkinter.IntVar(value=0)

        # Create radio buttons
        self.technique_label = customtkinter.CTkLabel(master=self.technique_choice, text="Choose the solving technique:")
        self.technique_label.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="w")

        self.brute_force = customtkinter.CTkRadioButton(master=self.technique_choice, variable=self.technique_used, value=0, text="Brute force technique")
        self.brute_force.grid(row=1, column=2, pady=10, padx=20, sticky="w")
        self.heuristic = customtkinter.CTkRadioButton(master=self.technique_choice, variable=self.technique_used, value=1, text="Heuristic technique")
        self.heuristic.grid(row=2, column=2, pady=10, padx=20, sticky="w")
        self.metaheuristic = customtkinter.CTkRadioButton(master=self.technique_choice, variable=self.technique_used, value=2, text="Metaheuristic technique")
        self.metaheuristic.grid(row=3, column=2, pady=10, padx=20, sticky="w")


        self.execute_technique = customtkinter.CTkButton(master=self.right_sidebar_frame, command=self.execute_technique_event) # TODO: change the function
        self.execute_technique.grid(row=4, column=2, padx=20, pady=(20, 40))
        self.execute_technique.configure(state="enabled", text="Execute technique")

    def create_population_event(self):
        # store in variables the values of the radio buttons
        distribution = self.population_distribution_value.get()
        size = self.population_size_value.get()

        if(distribution == 0):
            distribution = "Normal"
        else:
            distribution = "Bimodal"
        
        if(size == 0):
            size = 10000
        elif(size == 1):
            size = 100000
        else:
            size = 1000000
        
        data = []

        if(distribution == "Normal"):
            # Set parameters for Gaussian distribution
            mean, std = 100, 50
            # Generate Gaussian data
            data = self.generate_gaussian_data(size, mean, std)
            data = list(map(lambda x: abs(int(x)), data))
        else:
            # Set parameters for bimodal distribution
            mean1, std1 = 50, 10
            mean2, std2 = 100, 20
            weight1 = 0.7
            # Generate bimodal data
            data = self.generate_bimodal_data(size, mean1, std1, mean2, std2, weight1)
            data = list(map(lambda x: abs(int(x)), data))

        # store the data in the data.csv file
        csv_content = ""    # write the content of data.csv into the csv_content variable
        current_directory = os.getcwd() # Get the current working directory
        file_name = "data.csv" # Define the file name
        data_path = os.path.join(current_directory, file_name) # Create the path using the os package

        # Convert numerical values to strings and concatenate with newline character
        csv_content = "\n".join(map(str, data))

        # Clear the existing content and write the new content to data.csv
        with open(data_path, "w") as csv_file:
            csv_file.write(csv_content)
        

        # with open(data_path, "w") as csv_file:
        #     # csv_content = csv_file.read()
        #     csv_file.write(str(data))

        self.csv_preview.delete("0.0", "end")  # delete all text        
        self.csv_preview.insert("0.0", str(csv_content))
        # print(csv_content)
        # TODO: implement a prettify function for the csv content

        # self.csv_preview.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consektetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)

        # print("data:", data)
        
    def generate_bimodal_data(self, n, mean1, std1, mean2, std2, weight1=0.5):
        data1 = np.random.normal(mean1, std1, int(n * weight1))
        data2 = np.random.normal(mean2, std2, int(n * (1 - weight1)))
        return np.concatenate([data1, data2])

    def generate_gaussian_data(self, n, mean, std):
        return np.random.normal(mean, std, n)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def execute_technique_event(self):
        # create and object analizer
        analizer = Analizer()
        # store the value of the chosen technique
        technique = self.technique_used.get()

        if(technique == 0):
            technique = "Brute force"
        elif(technique == 1):
            technique = "Heuristic"
        else:
            technique = "Metaheuristic"

        print("technique:", technique)
        analizer.analize(technique)

        # TODO: update the csv_preview with the new data
        csv_content = ""    # write the content of data.csv into the csv_content variable
        current_directory = os.getcwd() # Get the current working directory
        file_name = "data.csv" # Define the file name
        data_path = os.path.join(current_directory, file_name) # Create the path using the os package

        with open(data_path, "r") as csv_file:
            csv_content = csv_file.read()
        
        self.csv_preview.delete("0.0", "end")
        self.csv_preview.insert("0.0", csv_content)

    def quit_simulation_event(self):
        self.destroy()
        exit()
