# Crea tu propia app para gestión de tiempo con Python
# Interfaces gráficas con Python: crea tu app Platzidoro
# Crea tu propia app de escritorio para impulsar tu concentración: Platzidoro

Seguramente ya conoces la técnica Pomodoro, sí, esa con la 
que activas tus superpoderes para enfocarte mientras estudias, consta 
de concentrase en ciclos de 25 minutos estudiando y 5 minutos de descanso.

¿No sería genial crear tu propia app que te marque el tiempo de estudio?

Al terminar este tutorial lograrás crear una aplicación de escritorio
utilizando Python y una de las librerías que incluye este lenguaje de
programación: TKinter. 

Si aún no conoces esta librería, te comparto que es una de las más populares
para crear interfaces gráficas de usuario (GUI), y que tiene soporte para
diversos lenguajes, así que podrás replicar este tutorial en: Ruby, Go, JS

Lo mejor será que podrás modificarla a tu gusto
para que se adapte a tu forma de estudio.

## Manos a la obra
___

Nota: En este tutorial nos vamos a enfocar en la parte práctica por lo que contar
con conocimientos previos de Python te ayudará muchísimo, aunque no es necesario
que lo domines todavía. También estaré utilizando comandos de entorno Unix.

Una buena práctica para iniciar un proyecto en Python
es generar un [entorno virtual,](https://platzi.com/clases/2255-python-intermedio/36458-que-es-un-entorno-virtual/)
lo cual hacemos con:

```Python
python3 -m venv venv
```
A continuación activamos nuestro entorno virtual:
```python
source venv/bin/activate
```
Ahora procedemos a generar desde la terminal, nuestro archivo de Python donde escribiremos el código
para generar nuestra aplicación de escritorio:
```
touch main.py
```
A partir de aquí puedes trabajar el proyecto en VSCode o tu editor de texto
preferido. Yo estaré utilizando PyCharm para este proyecto.

Dentro del archivo ``main.py`` estarás contruyendo la aplicación utilizando la librería
de TKinter que viene pre cargada en Python, así que solo hay que importarla al inicio:
```
from tkinter import *
```
## ¿Cómo funciona TKinter?

