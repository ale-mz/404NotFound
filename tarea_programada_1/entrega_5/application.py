import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class myApp():
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
            # call function from analyzer.py
            self.result_label.config(text="Analysis complete.")
        else:
            self.result_label.config(text="No file selected")

    def run(self):
        self.root.mainloop()


int main():
    app = myApp()
    app.run()
    return 0

if __name__ == '__main__':
    main()