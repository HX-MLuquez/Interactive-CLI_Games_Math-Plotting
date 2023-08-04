import random
import matplotlib.pyplot as plt
import numpy as np
import math

class PiedraPapelTijera:
    def __init__(self):
        self.opciones = ["piedra", "papel", "tijera"]
        
    def jugar(self):
        print("¡Bienvenido a Piedra, Papel, Tijera!")
        while True:
            opcion_usuario = input("Ingresa tu opción (piedra, papel o tijera): ")
            opcion_usuario = opcion_usuario.lower()
            opcion_computadora = random.choice(self.opciones)
            
            if opcion_usuario not in self.opciones:
                print("Opción inválida. Inténtalo nuevamente.")
                continue
            
            print("Tú elegiste:", opcion_usuario)
            print("La computadora eligió:", opcion_computadora)
            
            if opcion_usuario == opcion_computadora:
                print("Es un empate.")
            elif (
                (opcion_usuario == "piedra" and opcion_computadora == "tijera") or
                (opcion_usuario == "papel" and opcion_computadora == "piedra") or
                (opcion_usuario == "tijera" and opcion_computadora == "papel")
            ):
                print("¡Ganaste!")
            else:
                print("La computadora gana.")
                
            jugar_nuevamente = input("¿Quieres jugar nuevamente? (s/n): ")
            if jugar_nuevamente.lower() != "s":
                break

class AdivinarNumero:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        
    def jugar(self):
        print("¡Bienvenido a Adivinar el Número!")
        intentos = 0
        while True:
            intentos += 1
            numero_usuario = int(input("Ingresa tu número: "))
            
            if numero_usuario == self.numero_secreto:
                print("¡Felicitaciones! Adivinaste el número en", intentos, "intentos.")
                break
            elif numero_usuario < self.numero_secreto:
                print("El número secreto es mayor. Intenta nuevamente.")
            else:
                print("El número secreto es menor. Intenta nuevamente.")

class TirarDado:
    def __init__(self):
        self.lados = [1, 2, 3, 4, 5, 6]
        
    def tirar(self):
        print("¡Bienvenido a Tirar el Dado!")
        while True:
            input("Presiona Enter para tirar el dado...")
            resultado = random.choice(self.lados)
            print("El dado ha mostrado:", resultado)
            jugar_nuevamente = input("¿Quieres tirar el dado nuevamente? (s/n): ")
            if jugar_nuevamente.lower() != "s":
                break

class GraficarFuncion:
    def __init__(self):
        self.x = np.linspace(-10, 10, 100)
    def graficar(self):
        print("¡Bienvenido a Graficar una Función!")
        while True:
            print("Ingresa una función matemática (por ejemplo, 'math.sin(x)'): ")
            try:
                funcion = input()
                y = [eval(funcion, {"x": xi, "math": math}) for xi in self.x]
                plt.plot(self.x, y)
                plt.xlabel("x")
                plt.ylabel("y")
                plt.title("Gráfico de la función: " + funcion)
                plt.show()
            except SyntaxError:
                print("Error de sintaxis en la expresión matemática. Inténtalo nuevamente.")
            except:
                print("Ha ocurrido un error al graficar la función.")
            
            jugar_nuevamente = input("¿Quieres graficar otra función? (s/n): ")
            if jugar_nuevamente.lower() != "s":
                break

def elegir_juego():
    print("¡Bienvenido!")
    
    opciones = {
        "1": PiedraPapelTijera,
        "2": AdivinarNumero,
        "3": TirarDado,
        "4": GraficarFuncion,
        "0": None
    }
    
    while True:
        print("Elige un juego:")
        print("1. Piedra, Papel, Tijera")
        print("2. Adivinar el Número")
        print("3. Tirar el Dado")
        print("4. Graficar una Función")
        print("0. Salir")

        opcion = input("Ingresa el número de la opción que deseas jugar: ")

        if opcion in opciones:
            juego_clase = opciones[opcion]
            if juego_clase is None:
                break

            juego = juego_clase()
            if opcion == "3":
                juego.tirar()
            else:
                # juego.jugar() if hasattr(juego, 'jugar') else juego.graficar()
                if hasattr(juego, 'jugar'):
                    juego.jugar()
                else: juego.graficar()
        else:
            print("Opción inválida. Inténtalo nuevamente.")

# Llamamos a la función para iniciar el programa
elegir_juego()

# Ejemplo de uso
# juego = PiedraPapelTijera()
# juego.jugar()


"""
Instalar las bibliotecas matplotlib y numpy de manera local:

1. Puedes verificar versión comando: python --version. 

2. Abre una ventana de comandos (terminal) en tu computadora.

3. Para instalar matplotlib, ejecuta el siguiente comando:
pip install matplotlib

4. Para instalar numpy, ejecuta el siguiente comando:
pip install numpy

Una vez que hayas completado estos pasos, podrás importar matplotlib.pyplot y numpy en tu entorno 
de desarrollo local sin problemas.

Recuerda que si estás utilizando un entorno virtual (por ejemplo, venv o conda), 
debes asegurarte de activar el entorno antes de ejecutar los comandos de instalación. 
Esto garantiza que las bibliotecas se instalen en el entorno correcto.

Espero que esto te sea útil. ¡Si tienes alguna otra pregunta, no dudes en preguntar!
"""


"""
Un entorno virtual es una herramienta que permite crear un entorno de desarrollo aislado y 
separado del entorno global de Python en tu sistema. Esto significa que puedes tener múltiples 
entornos virtuales, cada uno con sus propias bibliotecas y versiones de Python, sin que entren 
en conflicto entre sí.

Existen diferentes herramientas para crear y gestionar entornos virtuales en Python. 
Algunas de las más populares son venv y conda.

venv: Es un módulo incorporado en Python a partir de la versión 3.3. Puedes crear un entorno 
virtual utilizando el siguiente comando en la terminal:

Copy code
python -m venv nombre_del_entorno
Esto creará un nuevo directorio con el nombre especificado (nombre_del_entorno) que contendrá 
el entorno virtual. Para activar el entorno virtual, en la misma terminal, ejecuta el siguiente comando:

En Windows:

Copy code
nombre_del_entorno\Scripts\activate.bat
En macOS/Linux:

bash
Copy code
source nombre_del_entorno/bin/activate
Una vez activado el entorno virtual, todas las bibliotecas que instales utilizando pip se instalarán 
en ese entorno específico.

conda: Es una plataforma y gestor de paquetes que proporciona entornos virtuales y administración 
de paquetes para varios lenguajes de programación, incluido Python. Con conda, puedes crear y 
administrar entornos virtuales con facilidad. Para crear un entorno virtual con conda, puedes 
ejecutar el siguiente comando en la terminal:

lua
Copy code
conda create --name nombre_del_entorno
Esto creará un nuevo entorno virtual con el nombre especificado (nombre_del_entorno). 
Para activar el entorno virtual, en la misma terminal, ejecuta el siguiente comando:

Copy code
conda activate nombre_del_entorno
Al igual que con venv, todas las bibliotecas que instales utilizando pip o conda dentro de este 
entorno virtual específico se instalarán en ese entorno.

Utilizar un entorno virtual es útil cuando deseas mantener diferentes proyectos o aplicaciones 
separadas, cada una con sus propias dependencias y versiones de bibliotecas. 
Además, también facilita la distribución y reproducción de tu entorno de desarrollo en diferentes sistemas.

Espero que esto aclare tus dudas. Si tienes más preguntas, no dudes en preguntar.
"""