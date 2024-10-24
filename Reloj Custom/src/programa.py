import time
import threading
import tkinter
import winsound
from PIL import Image, ImageTk
from gif import Gif #no usado por ahora
import os


#Clase contador
class Contador:
    def __init__(self):
        # los atributos son el tiempo, y variables para controlar el avance del contador y reproduccion del sonido
        self.contador_activo = False
        self.sonido_reproduciendo = False
        self.segundos = 0
        self.minutos = 0
        self.horas = 0
        self.cancion = "Seishun Complex"

    def crear_contador(self, label):
        # crea el contador y su logica
        while self.contador_activo:
            self.segundos += 1
            time.sleep(1)
            if self.segundos == 60:
                self.segundos = 0
                self.minutos += 1
            if self.minutos == 60:
                self.minutos = 0
                self.horas += 1
            #actualizacion del label
            label.config(text=f"Tiempo transcurrido: {self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}")
            
            # CONFIGURAR MAS PARA QUE NO SEAN 3 SEGUNDOS SINO MAS BIEN UN TIEMPO ELEGIDO POR USUARIO
            if self.segundos == 3 and not self.sonido_reproduciendo:
                self.sonido_reproduciendo = True  # cuando sonido se reproduce, se actualiza a True
                self.reproducirSonido()

    def reproducirSonido(self):
        # SND_ASYNC permite que el sonido se reproduzca de forma sincrona, asi no se interrumpe la ejecucion del resto
        if self.cancion == "Seishun Complex":
            winsound.PlaySound("sounds\\alarmaBTR.wav", winsound.SND_ASYNC | winsound.SND_FILENAME)
        elif self.cancion == "World.execute(me);":
            winsound.PlaySound("sounds\\World.Execute(me).wav", winsound.SND_ASYNC | winsound.SND_FILENAME)
        elif self.cancion == "Rock'n Roll morning light falls on you":
            winsound.PlaySound("sounds\\BestKessokuSong.wav", winsound.SND_ASYNC | winsound.SND_FILENAME)
        elif self.cancion == "Freedom Dive":
            winsound.PlaySound("sounds\\FreedomDive.wav", winsound.SND_ASYNC | winsound.SND_FILENAME)

    def detenerSonido(self):
        self.sonido_reproduciendo = False  # Actualizar el estado
        winsound.PlaySound(None, winsound.SND_ASYNC)  # Detener el sonido

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
        #reinicio del label
        label.config(text=f"Tiempo transcurrido: {self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}")

# Crear la ventana principal
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

#queria poner esto pero la verdad es que el gif no se mueve y no se porque
gif = Gif(root, gif_path) 
gif.place(100, 50)

cancion_var = tkinter.StringVar(value="Seishun Complex")  # canción por defecto
# menú desplegable para seleccionar las canciones
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
imagen_pil = Image.open("imgs\mainIMG.png")
# Se redimensiona la imagen con la librería PIL, se ajusta a 400x420
imagenRedimensionada = imagen_pil.resize((400, 420))
# Se convierte la imagen en tkinter usando .PhotoImage
imagen_tk = ImageTk.PhotoImage(imagenRedimensionada)
# Se asigna la imagen a una variable label
label_imagen = tkinter.Label(root, image=imagen_tk)
# Se coloca el label creado
label_imagen.place(x=100, y=200)

root.mainloop()
