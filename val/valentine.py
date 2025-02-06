import tkinter as tk
import random
from PIL import Image, ImageTk

class ValentineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Be My Valentine?")
        self.root.geometry("600x400")
        
        # Load and set background image
        #self.bg_image = Image.open("background.jpg")  # Ensure you have this file
        self.bg_image = Image.open(r"C:\Users\hp\Desktop\VS\Python\.venv\val\background.jpg ")
        self.bg_image = self.bg_image.resize((600, 400), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        
        # Create a label with the question
        self.label = tk.Label(root, text="Will you be my Valentine?", font=("Arial", 20, "bold"), bg="pink", fg="red")
        self.label.place(x=252, y=50)
        
        # Create the Yes button
        self.yes_button = tk.Button(root, text="Yes", font=("Arial", 14, "bold"), bg="red", fg="white", command=self.yes_clicked)
        self.yes_button.place(x=290, y=170)
        
        # Create the No button
        self.no_button = tk.Button(root, text="No", font=("Arial", 14, "bold"), bg="white", fg="red", command=self.move_no_button)
        self.no_button.place(x=490, y=200)
        
        # Initialize previous position
        self.old_x = None
        self.old_y = None
        self.yes_buttons = []  # Track dynamically created Yes buttons
    
    def yes_clicked(self):
        # Remove all Yes buttons before displaying the message
        for button in self.yes_buttons:
            button.destroy()
        self.yes_buttons.clear()
        
        # Remove No button
        if self.no_button.winfo_ismapped():
            self.no_button.destroy()
        
        self.label.config(text="I love you, Baby ❤️", fg="white", bg="red")
        self.yes_button.destroy()
    
    def move_no_button(self):
        # Save the old position
        if self.no_button.winfo_ismapped():
            self.old_x = self.no_button.winfo_x()
            self.old_y = self.no_button.winfo_y()
        
        new_x = random.randint(50, 500)
        new_y = random.randint(100, 300)
        
        # Remove the current No button
        self.no_button.destroy()
        
        # Create a new No button in a random position
        self.no_button = tk.Button(self.root, text="No", font=("Arial", 14, "bold"), bg="white", fg="red", command=self.move_no_button)
        self.no_button.place(x=new_x, y=new_y)
        
        # Create a new Yes button in its previous place
        if self.old_x is not None and self.old_y is not None:
            new_yes_button = tk.Button(self.root, text="Yes", font=("Arial", 14, "bold"), bg="red", fg="white", command=self.yes_clicked)
            new_yes_button.place(x=self.old_x, y=self.old_y)
            self.yes_buttons.append(new_yes_button)  # Track the new Yes button
        
        # Update the UI
        self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = ValentineApp(root)
    root.mainloop()
