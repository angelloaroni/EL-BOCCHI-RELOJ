import tkinter as tk
from PIL import Image, ImageTk

#no se como cargar el gif en tkinter
class Gif:
    def __init__(self, master, gif_path):
        self.master = master
        
        self.image = Image.open(gif_path)
        self.frames = [ImageTk.PhotoImage(self.image.copy().convert("RGBA")) for _ in range(self.image.n_frames)]
        
        # Configurar el label para mostrar el GIF
        self.label = tk.Label(master)
        self.label.pack()

        self.current_frame = 0
        self.update_gif()

    def update_gif(self):
        #actualizando los frames del gif
        self.label.config(image=self.frames[self.current_frame])
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.master.after(1, self.update_gif)  

    def place(self, x, y):
        # Método para colocar el GIF en una posición específica
        self.label.place(x=x, y=y)
