 # GraficarFunction
 ## Explicación línea por línea del code:

```python
class GraficarFuncion:
```
Esta línea define una clase llamada GraficarFuncion. Una clase es una plantilla para crear objetos. En este caso, la clase se utiliza para encapsular la funcionalidad de graficar una función.

```python
    def __init__(self):
        self.x = np.linspace(-10, 10, 100)
```
Aquí se define un método especial llamado __init__, que es el constructor de la clase. El constructor se ejecuta automáticamente cuando se crea un nuevo objeto de la clase. En este caso, el constructor inicializa un atributo x que contiene un arreglo de 100 puntos equidistantes en el rango de -10 a 10. Esto se logra utilizando la función linspace de la biblioteca NumPy (importada como np).

```python
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
```
Aquí se define el método graficar. Este método se encarga de pedir al usuario una función matemática, evaluarla para cada valor de x en el rango predefinido, y luego graficar la función resultante utilizando la biblioteca matplotlib.pyplot (importada como plt).

Dentro del bucle while True, el programa solicita al usuario que ingrese una función matemática en formato de cadena, por ejemplo, "math.sin(x)". Luego, utiliza la función eval para evaluar la expresión ingresada, asignando valores a las variables x y math dentro del entorno de evaluación. El resultado de evaluar la función para cada valor de x se almacena en la lista y.

A continuación, el código utiliza plt.plot para trazar la función en el gráfico, y luego agrega etiquetas de ejes y un título al gráfico utilizando las funciones plt.xlabel, plt.ylabel y plt.title. Finalmente, muestra el gráfico utilizando plt.show.

Si ocurre un error de sintaxis durante la evaluación de la función, se captura la excepción SyntaxError y se imprime un mensaje de error.

Si ocurre cualquier otro error durante el proceso de graficación, se captura cualquier excepción genérica y se imprime un mensaje de error.

```python
            jugar_nuevamente = input("¿Quieres graficar otra función? (s/n): ")
            if jugar_nuevamente.lower() != "s":
                break
```
Después de graficar la función, se le pregunta al usuario si desea graficar otra función. Si la respuesta no es "s" (ignorando mayúsculas y minúsculas), se rompe el bu