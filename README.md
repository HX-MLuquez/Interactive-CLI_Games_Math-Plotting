# CHALLENGE - PYTHON
###  Desarrollar un programa que permita realizar diferentes operaciones en base a las opciones que el usuario vaya ingresando por línea de comandos:
- Jugar a “piedra, papel, tijera” compitiendo contra la computadora.
- Adivinar un número compitiendo contra la computadora.
- Tirar un dado.
- Graficar una función matemática.

### El programa deberá estructurarse utilizando clases y ser subido a Github

---

## STEPS

### Instalar las bibliotecas matplotlib y numpy de manera local:

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



### Entorno Virtual en Python

Un entorno virtual es una herramienta que permite crear un entorno de desarrollo aislado y 
separado del entorno global de Python en tu sistema. Esto significa que puedes tener múltiples 
entornos virtuales, cada uno con sus propias bibliotecas y versiones de Python, sin que entren 
en conflicto entre sí.

Existen diferentes herramientas para crear y gestionar entornos virtuales en Python. 
Algunas de las más populares son venv y conda.

1. venv: Es un módulo incorporado en Python a partir de la versión 3.3. Puedes crear un entorno 
virtual utilizando el siguiente comando en la terminal:

```
python -m venv nombre_del_entorno
```
Esto creará un nuevo directorio con el nombre especificado (nombre_del_entorno) que contendrá 
el entorno virtual. Para activar el entorno virtual, en la misma terminal, ejecuta el siguiente comando:

En Windows:
```
nombre_del_entorno\Scripts\activate.bat
```

En macOS/Linux:

```
source nombre_del_entorno/bin/activate
```

Una vez activado el entorno virtual, todas las bibliotecas que instales utilizando pip se instalarán 
en ese entorno específico.

2. conda: Es una plataforma y gestor de paquetes que proporciona entornos virtuales y administración 
de paquetes para varios lenguajes de programación, incluido Python. Con conda, puedes crear y 
administrar entornos virtuales con facilidad. Para crear un entorno virtual con conda, puedes 
ejecutar el siguiente comando en la terminal:

```
conda create --name nombre_del_entorno
```
Esto creará un nuevo entorno virtual con el nombre especificado (nombre_del_entorno). 
Para activar el entorno virtual, en la misma terminal, ejecuta el siguiente comando:

```
conda activate nombre_del_entorno
```
Al igual que con venv, todas las bibliotecas que instales utilizando pip o conda dentro de este 
entorno virtual específico se instalarán en ese entorno.

Utilizar un entorno virtual es útil cuando deseas mantener diferentes proyectos o aplicaciones 
separadas, cada una con sus propias dependencias y versiones de bibliotecas. 
Además, también facilita la distribución y reproducción de tu entorno de desarrollo en diferentes sistemas.

