import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt
import analyzer

class menu():
    def __init__(self):

        # Create the main window
        self.root = tk.Tk()
        self.root.title("App with Multiple Buttons")
        self.has_file = False

        # Create a info window
        self.info_window = None
        
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
            # print("Analyzing file: " + file_path)
            # call function from analyzer.py
            self.result_label.config(text="Analysis complete.")

            analyze(file_path,self)
            self.has_file = True


            # analyzed_data = analyzer.analyze(file_path)
            # clean_data = clean_tables(analyzed_data)
            # close menu

            # print("analyzed completed")
            # self.root.destroy() 
        else:
            self.result_label.config(text="No file selected")

    def run(self):
        self.root.mainloop()

def analyze(file_path, self):
    
    output = []
    output = analyzer.analyze(file_path)

    vpns = []
    vpns = analyzer.vpn_table()

    conn = []
    conn = analyzer.vpn_con()

    # ------------------ Make a function -----------
    dataframe = []
    print("\n")

    # Pass all to a new table
    for i in range(len(output)):

        # Look if the user was previously append
        userbool = False
        for j in range(len(dataframe)):
            if (dataframe[j][1] == output[i][1]):
                userbool = True
            
        if userbool == False:
            # IP(s)
            IPs = [output[i][2]]
            # Route(s) list
            RTs = [output[i][3]]

            # Append to the new table all data from the old one
            # Bool / User / IP(s) / Route(s) / Conection(s) / #IP(s) / #Route(s)
            input = [output[i][0], output[i][1], IPs, RTs, 0, 1, 1]
            dataframe.append(input)

            for j in range(len(output)):
                # Same user
                last = len(dataframe) -1
                if (dataframe[last][1] == output[j][1]):
                    # New Conection
                    dataframe[last][4] += 1
                    # If the IP associate is new append it in new table
                    conf = False
                    for k in range(len(dataframe[last][2])) :
                        if (dataframe[last][2][k] == output[j][2]):
                            conf = True
                    
                    if conf == False:
                        dataframe[last][2].append(output[j][2])
                        dataframe[last][5] += 1

                    conf = False
                    for k in range(len(dataframe[last][3])) :
                        if (dataframe[last][3][k] == output[j][3]):
                            conf = True
                    
                    if conf == False:
                        dataframe[last][3].append(output[j][3])
                        dataframe[last][6] += 1

    # (1,2). Calculate the total amount of connections fro teachers and students
    # And  Students & Teachers connections for each one
    students_counter = 0
    teachers_counter = 0
    for i in range(len(dataframe)):
        if dataframe[i][0] == True:
            students_counter += dataframe[i][4]
        else:
            teachers_counter += dataframe[i][4]
    total_connections = students_counter + teachers_counter 
    
    # 3. User's IP List
    iplist = []
    for i in range(len(dataframe)):
        for j in range(len(dataframe[i][2])):
            iplist.append(dataframe[i][2][j])
    init_info_window(self,students_counter,teachers_counter,total_connections,iplist)
    # 4. Cuántas conexiones por cada ruta se establecieron (mostrar un gráfico).
        # list of pairs (route, counter)
    analyzer_conn = []
    analyzer_conn = analyzer.vpn_con()
    analyzer_vpns = []
    analyzer_vpns = analyzer.vpn_table()
    vpns = analyzer_vpns = [line[1] for line in analyzer_vpns]
    connection_list = []
    
    for item in vpns:
        new_vpn = item.replace("[","").replace("]","") # get rid of the [] simbols of the vpns
        input = [item, 0]
        connection_list.append(input)
        
    
    for connection in connection_list:
        benchmark = connection
        counter = 0
        for line in analyzer_conn:
            for vpn in line:
                if benchmark[0] == vpn:
                    counter +=1
        benchmark[1] = counter

    # print (connection_list)
    connection_vpns = [line[0] for line in connection_list]
    vpn_amount = [line[1] for line in connection_list]

    plt.figure(1,figsize=(10,8))
    plt.bar(connection_vpns,vpn_amount)# ,Poner colores)
    plt.title("Chart of usage of VPNs")
    plt.xlabel("VPN Used")
    plt.ylabel("Times")
    plt.grid(True,axis = 'y', color = 'g')
    plt.savefig('VPNs.png')
    
    # 5. Los 5 usuarios con más conexiones realizadas (mostrar un gráfico).
    # vector with the names
    names = [line[1] for line in dataframe]
    # vector with the connections( treated as ints)
    conections = [int(conection[4]) for conection in dataframe]
    # sort the names and conections 
    all_sort = sorted(list(zip(names,conections)), key=lambda x: x[1], reverse=True)
    nombres_ordenados , cantidades = zip(*all_sort)
    
    # reduce the amount to the best 5
    name_top5 = nombres_ordenados[:5]
    amount_top5 = cantidades[:5]

    # Colors
    # Obtain from: https://www.webucator.com/article/python-color-constants-module/
    bars_colors = ['#FFD700', '#C0C0C0', '#CD7F32', '#00FFFF', '#800080']
    # create the chart
    plt.figure(2,figsize=(8,6))
    plt.bar(name_top5, amount_top5, color = bars_colors)
    plt.title("Chart of users with more conections")
    plt.xlabel("Users")
    plt.ylabel("Connections per users")
    plt.grid(True,axis = 'y', color = 'b')
    plt.savefig('Connections_per_user.png')

    plt.show()

def init_info_window(self,students_counter,teachers_counter,total_connections,iplist):
    if self.info_window is None:
        self.info_window = tk.Toplevel(self.root) # Create a Secondary window linked to root
        self.info_window.geometry("400x300") 
        self.info_window.title("Data")
        to_print_text  = "Students Connections: [" + str(students_counter) + "]"
        to_print_text += "\nTeachers Connections: [" + str(teachers_counter) + "]"
        to_print_text += "\nTotal Connections: [" + str(total_connections) + "]"
        
        info = tk.Label(self.info_window, text= to_print_text)
        info.pack(padx=20, pady=20)
        # create the ip Scroll box
        scrollbox = tk.Listbox(self.info_window)
        for ip in iplist:
            scrollbox.insert(tk.END, ip)
        
        # Create the IP scroll bar for the scroll box
        scrollbar = tk.Scrollbar(self.info_window, orient=tk.VERTICAL)
        scrollbar.config(command = scrollbox.yview)
        scrollbox.config(yscrollcommand = scrollbar.set)
        scrollbox.pack(fill = tk.Y)


def main():
    appmenu = menu()
    appmenu.run()

if __name__ == '__main__':
    main()
