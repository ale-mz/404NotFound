import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.widgets import Slider
import analyzer

dataframe = []

class datas():
    def __init__(self):

        # Create the main window
        self.root = tk.Tk()
        self.root.title("App with Multiple Buttons")

        # Load the image and resize it to 50x50
        # original_image = tk.PhotoImage(file="image0.png")
        # resized_image = original_image.subsample(1)  # Resize the image using subsample method
        # self.image = resized_image

        # Create a label for the image
        # image_label = tk.Label(self.root, image=self.image)
        # image_label.pack(pady=10)

        # Create buttons for various functionalities
        quit_button = tk.Button(self.root, text="Quit App", command=self.root.quit)

        # Create a frame for the main content
        self.content_frame = tk.Frame(self.root)

        # Create labels to display file and analysis information
        # self.file_label = tk.Label(self.content_frame, text="No file selected")
        # self.result_label = tk.Label(self.content_frame, text="")

        # Pack buttons, labels, and frames
        # choose_file_button.pack(pady=10)
        # analyze_file_button.pack(pady=10)
        quit_button.pack(pady=10)

        self.file_label.pack(pady=10)
        self.result_label.pack(pady=10)

        # Show the main content frame initially
        self.content_frame.pack(fill="both", expand=True)  # Show the content frame

        # Set window dimensions and position
        window_width = 800
        window_height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def run(self):
        self.root.mainloop()



class menu():
    def __init__(self):

        # Create the main window
        self.root = tk.Tk()
        self.root.title("App with Multiple Buttons")

        # Load the image and resize it to 50x50
        # original_image = tk.PhotoImage(file="image0.png")
        # resized_image = original_image.subsample(1)  # Resize the image using subsample method
        # self.image = resized_image

        # Create a label for the image
        # image_label = tk.Label(self.root, image=self.image)
        # image_label.pack(pady=10)

        # Create buttons for various functionalities
        choose_file_button = tk.Button(self.root, text="Choose File", command=self.choose_file)
        analyze_file_button = tk.Button(self.root, text="Analyze File", command=self.analyze_file)
        quit_button = tk.Button(self.root, text="Quit App", command=self.root.quit)

        # Create a frame for the main content
        self.content_frame = tk.Frame(self.root)

        # Create labels to display file and analysis information
        self.file_label = tk.Label(self.content_frame, text="No file selected")
        self.result_label = tk.Label(self.content_frame, text="")

        # Pack buttons, labels, and frames
        choose_file_button.pack(pady=10)
        analyze_file_button.pack(pady=10)
        quit_button.pack(pady=10)

        self.file_label.pack(pady=10)
        self.result_label.pack(pady=10)

        # Show the main content frame initially
        self.content_frame.pack(fill="both", expand=True)  # Show the content frame

        # Set window dimensions and position
        window_width = 800
        window_height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def choose_file(self):
        file_path = filedialog.askopenfilename(title="Choose a File") 
        if file_path:
            self.file_label.config(text="Selected File: " + file_path)
        else:
            self.file_label.config(text="No file selected")

    def analyze_file(self):
        file_path = self.file_label.cget("text")[15:]
        if file_path:
            print("Analyzing file: " + file_path)
            # call function from analyzer.py
            self.result_label.config(text="Analysis complete.")
            analyzed_data = analyzer.analyze(file_path)
            clean_data = clean_tables(analyzed_data)
            # close menu
            self.root.destroy() 
        else:
            self.result_label.config(text="No file selected")


def run(self):
    self.root.mainloop()

def clean_tables(raw_data):
    # Pass all to a new table

    for i in range(len(raw_data)):

        # Look if the user was previously append
        userbool = False
        for j in range(len(dataframe)):
            if (dataframe[j][0] == raw_data[i][0]):
                userbool = True
            
            if userbool == False:
                # IP(s)
                IPs = [raw_data[i][1]]
                # Route(s) list
                RTs = [raw_data[i][2]]

                # Append to the new table all data from the old one
                # User / IP(s) / Route(s) / Conection(s) / #IP(s) / #Route(s)
                input = [raw_data[i][0], IPs, RTs, 0, 1, 1]
                dataframe.append(input)

                for j in range(len(raw_data)):
                    # Same user
                    last = len(dataframe) -1
                    if (dataframe[last][0] == raw_data[j][0]):
                        # New Conection
                        dataframe[last][3] += 1
                        # If the IP associate is new append it in new table
                        conf = False
                        for k in range(len(dataframe[last][1])) :
                            if (dataframe[last][1][k] == raw_data[j][1]):
                                conf = True
                    
                        if conf == False:
                            dataframe[last][1].append(raw_data[j][1])
                            dataframe[last][4] += 1

                        conf = False
                        for k in range(len(dataframe[last][2])) :
                            if (dataframe[last][2][k] == raw_data[j][2]):
                                conf = True
                        
                        if conf == False:
                            dataframe[last][2].append(raw_data[j][2])
                            dataframe[last][5] += 1
    return dataframe

def create_graphs(dataframe):
    # 1. Cuántas conexiones en total se establecieron.
    connections_counter = 0
    for i in range(len(dataframe)):
        connections_counter += dataframe[i][3]
    # 2. Cuántos estudiantes y cuántos profesores usaron el servicio. Tome en cuenta que un mismo usuario podría haberse conectado en ocasiones diferentes.
    students_counter = 0
    teachers_counter = 0

    # 3. Lista de direcciones IP desde las cuáles se conectaron los usuarios.
    # create a list of all the IPs
    ips_list = []
    for i in range(len(dataframe)):
        for j in range(len(dataframe[i][1])):
            ips_list.append(dataframe[i][1][j])

    # 4. Cuántas conexiones por cada ruta se establecieron (mostrar un gráfico).
    # list of pairs (route, counter)
    routes_list = []
    for i in range(len(dataframe)):
        for j in range(len(dataframe[i][2])):
            routes_list.append(dataframe[i][2][j])

    # 5. Los 5 usuarios con más conexiones realizadas (mostrar un gráfico).
    


def main():
    appmenu = menu()
    appmenu.run()
    data = datas()
    data.run()    

if __name__ == '__main__':
    main()