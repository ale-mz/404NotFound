import tkinter
import tkinter.messagebox
import customtkinter
import os

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
        self.radio_var = tkinter.IntVar(value=0)

        # Create radio buttons
        self.distribution_label = customtkinter.CTkLabel(master=self.population_distribution, text="Choose the population distribution:")
        self.distribution_label.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="w")

        # self.linear_distribution = customtkinter.CTkRadioButton(master=self.population_distribution, variable=self.radio_var, value=0, text="Linear distribution")
        # self.linear_distribution.grid(row=1, column=2, pady=10, padx=20, sticky="w")
        self.normal_distribution = customtkinter.CTkRadioButton(master=self.population_distribution, variable=self.radio_var, value=0, text="Normal distribution")
        self.normal_distribution.grid(row=2, column=2, pady=10, padx=20, sticky="w")
        self.bimodal_distribution = customtkinter.CTkRadioButton(master=self.population_distribution, variable=self.radio_var, value=1, text="Bimodal distribution")
        self.bimodal_distribution.grid(row=3, column=2, pady=10, padx=20, sticky="w")



        # CHOOSING THE POPULATION SIZE SECTION
        # Create the inner frame (self.technique_choice)
        self.population_size = customtkinter.CTkFrame(master=self.right_sidebar_frame)
        self.population_size.grid(row=1, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # Create a variable to hold the selected radio button value
        self.radio_var = tkinter.IntVar(value=0)

        # Create radio buttons
        self.size_label = customtkinter.CTkLabel(master=self.population_size, text="Choose the population size:")
        self.size_label.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="w")

        self.small_population = customtkinter.CTkRadioButton(master=self.population_size, variable=self.radio_var, value=0, text="Small population (100)")
        self.small_population.grid(row=1, column=2, pady=10, padx=20, sticky="w")
        self.medium_population = customtkinter.CTkRadioButton(master=self.population_size, variable=self.radio_var, value=1, text="Medium population (1000)")
        self.medium_population.grid(row=2, column=2, pady=10, padx=20, sticky="w")
        self.large_population = customtkinter.CTkRadioButton(master=self.population_size, variable=self.radio_var, value=2, text="Large population (10000)")
        self.large_population.grid(row=3, column=2, pady=10, padx=20, sticky="w")

        # BUTTON CREATE POPULATION
        self.create_population = customtkinter.CTkButton(master=self.right_sidebar_frame, command=self.execute_technique_event) # TODO: change the function
        self.create_population.grid(row=2, column=2, padx=20, pady=(20, 40))
        self.create_population.configure(state="enabled", text="Create population")

        # CHOOSING SOLVING TECHNIQUE SECTION
        # Create the inner frame (self.technique_choice)
        self.technique_choice = customtkinter.CTkFrame(master=self.right_sidebar_frame)
        self.technique_choice.grid(row=3, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # Create a variable to hold the selected radio button value
        self.radio_var = tkinter.IntVar(value=0)

        # Create radio buttons
        self.technique_label = customtkinter.CTkLabel(master=self.technique_choice, text="Choose the solving technique:")
        self.technique_label.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="w")

        self.brute_force = customtkinter.CTkRadioButton(master=self.technique_choice, variable=self.radio_var, value=0, text="Brute force technique")
        self.brute_force.grid(row=1, column=2, pady=10, padx=20, sticky="w")
        self.heuristic = customtkinter.CTkRadioButton(master=self.technique_choice, variable=self.radio_var, value=1, text="Heuristic technique")
        self.heuristic.grid(row=2, column=2, pady=10, padx=20, sticky="w")
        self.metaheuristic = customtkinter.CTkRadioButton(master=self.technique_choice, variable=self.radio_var, value=2, text="Metaheuristic technique")
        self.metaheuristic.grid(row=3, column=2, pady=10, padx=20, sticky="w")


        self.execute_technique = customtkinter.CTkButton(master=self.right_sidebar_frame, command=self.execute_technique_event) # TODO: change the function
        self.execute_technique.grid(row=4, column=2, padx=20, pady=(20, 40))
        self.execute_technique.configure(state="enabled", text="Execute technique")



    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def execute_technique_event(self):
        print("execute_technique_event")
        # TODO: implement the solving technique
        # TODO: update the csv_preview with the results of the solving technique

    def quit_simulation_event(self):
        self.destroy()
        exit()
