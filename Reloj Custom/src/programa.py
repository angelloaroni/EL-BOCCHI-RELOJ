import time
import threading
import tkinter
import pygame  # originalmente winsound xd
from PIL import Image, ImageTk
import os


# Clase contador
class Contador:
    def __init__(self):
        # Inicializa los atributos del contador
        self.contador_activo = False
        self.sonido_reproduciendo = False
        self.segundos = 0
        self.minutos = 0
        self.horas = 0
        self.cancion = "Seishun Complex"
        pygame.mixer.init()  

    def crear_contador(self, label):
        # Crea el contador y su lógica
        while self.contador_activo:
            self.segundos += 1
            time.sleep(1)
            if self.segundos == 60:
                self.segundos = 0
                self.minutos += 1
            if self.minutos == 60:
                self.minutos = 0
                self.horas += 1
            
            # Actualización del label
            label.config(text=f"Tiempo transcurrido: {self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}")
            
            if self.segundos == 3 and not self.sonido_reproduciendo:
                self.sonido_reproduciendo = True  # Cuando el sonido se reproduce, se actualiza a True
                self.reproducirSonido()

    def reproducirSonido(self):
        #dependiendo de lo elegido se reproduce alguna de estas 
        if self.cancion == "Seishun Complex":
            pygame.mixer.music.load("sounds/alarmaBTR.mp3")
        elif self.cancion == "World.execute(me);":
            pygame.mixer.music.load("sounds/World.Execute(me).mp3")
        elif self.cancion == "Rock'n Roll morning light falls on you":
            pygame.mixer.music.load("sounds/BestKessokuSong.mp3")
        elif self.cancion == "Freedom Dive":
            pygame.mixer.music.load("sounds/FreedomDive.mp3")


        pygame.mixer.music.play(-1)  

    def detenerSonido(self):
        self.sonido_reproduciendo = False  # Actualizar el estado
        pygame.mixer.music.stop()  # Detener el sonido

    def iniciarContador(self, label):
        if not self.contador_activo:
            self.contador_activo = True
            hilo1 = threading.Thread(target=self.crear_contador, args=(label,))
            hilo1.start()

    def detenerContador(self):
        self.contador_activo = False
        self.detenerSonido()  # Detener el sonido si se estaba reproduciendo

    def reiniciarContador(self, label):
        self.detenerContador()  # Detener el contador antes de reiniciar
        self.segundos = 0
        self.minutos = 0
        self.horas = 0
        # Reinicio del label
        label.config(text=f"Tiempo transcurrido: {self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}")

# Configuración de la ventana principal de tkinter
root = tkinter.Tk()
root.title("Ventana del contador")
root.config(bg="black")
root.geometry("1920x1080")

contador = Contador()  # Instancia de la clase Contador

lab1 = tkinter.Label(root, text=f"Tiempo transcurrido: {contador.horas:02d}:{contador.minutos:02d}:{contador.segundos:02d}", height=2, width=40, font=("", 20))
lab1.place(x=620, y=560)

# Funciones para controlar el contador
def iniciar_contador():
    # Actualizar la canción seleccionada antes de iniciar el contador
    contador.cancion = cancion_var.get()
    contador.iniciarContador(lab1)

def detener_contador():
    contador.detenerContador()

def reiniciar_contador():
    contador.reiniciarContador(lab1)

# Botones para controlar el contador
btn1 = tkinter.Button(root, text="Iniciar", command=iniciar_contador, height=4, width=40, bg="green")
btn1.place(x=800, y=200)

btn2 = tkinter.Button(root, text="Detener", command=detener_contador, height=4, width=40, bg="red")
btn2.place(x=800, y=320)

btn3 = tkinter.Button(root, text="Reiniciar", command=reiniciar_contador, height=4, width=40, bg="yellow")
btn3.place(x=800, y=440)

gif_path = os.path.join("gifs", "bocchi-the-rock-anime.gif")

# Menú desplegable para seleccionar las canciones
cancion_var = tkinter.StringVar(value="Seishun Complex")  # Canción por defecto
desplegable = tkinter.OptionMenu(root, cancion_var, 
                                  "Seishun Complex", 
                                  "World.execute(me);",
                                  "Rock'n Roll morning light falls on you",
                                  "Freedom Dive",                                  
                                  )
desplegable.config(height=4, width=40, text="Seleccionar Canción")
desplegable.pack()
desplegable.place(x=1200, y=200)

# Cargar y colocar la imagen
imagen_pil = Image.open("imgs/mainIMG.png")  
# Se redimensiona la imagen con la librería PIL, se ajusta a 400x420
imagenRedimensionada = imagen_pil.resize((400, 420))
# Se convierte la imagen en tkinter usando .PhotoImage
imagen_tk = ImageTk.PhotoImage(imagenRedimensionada)
# Se asigna la imagen a una variable label
label_imagen = tkinter.Label(root, image=imagen_tk)
# Se coloca el label creado
label_imagen.place(x=100, y=200)

root.mainloop()
