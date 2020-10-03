#!/usr/bin/env python
'''
Matplotlib [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec
import mplcursors  # [Opcional cursores]


def simple_plot():
    # Dibujar una recta y = 2x
    x = np.linspace(start=0, stop=10, num=11)
    y = 2*x

    plt.figure()
    plt.plot(x, y, color='m', marker='^')
    plt.show()

    # Dibujar una senoidal y = sin(x)
    x = np.linspace(start=0, stop=2*np.pi, num=100)
    y = np.sin(x)

    fig = plt.figure()      # Definir tamaño figura
    ax = fig.add_subplot()  # Definir cuantos gráficos tendrá

    ax.plot(x, y)           # Graficar con plot en mi gráfico "ax"
    ax.set_facecolor('whitesmoke')
    ax.set_title("Mi senoidal")
    ax.set_ylabel("Amplitud")
    ax.set_xlabel("[rad]")
    plt.show()              # Mostrar el gráfico


def multi_plot():
    # Dibujar múltiples líneas en un mismo gráfico
    x = np.linspace(start=0, stop=4*np.pi, num=100)

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(x, np.sin(x), color='b', marker='^', label='y=sin(x)')
    ax.plot(x, 2*np.sin(x), color='c', marker='+', label='y=2*sin(x)')
    ax.plot(x, 3*np.sin(x), color='g', marker='.', label='y=3*sin(x)')
    ax.plot(x, 4*np.sin(x), color='k', label='y=4*sin(x)')
    ax.set_facecolor('whitesmoke')
    ax.set_title("Senoidales")
    ax.set_ylabel("Y[amplitud]")
    ax.set_xlabel("X[rads]")
    ax.set_xlim([0, 4*np.pi])  # Limito el eje "Y" entre 0 y 4*pi
    ax.set_ylim([-4, 4])       # Limito el eje "X" entre -4 y 4
    ax.legend()
    plt.show(block=False)

    # Dibujar 4 gráficos en una misma figura
    fig = plt.figure()
    # Ejemplo de uso --> ax = fig.add_subplot(nrows, ncols, index)
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    ax1.plot(x, np.sin(x), color='b', marker='^', label='y=sin(x)')
    ax1.set_facecolor('whitesmoke')
    ax1.set_title("Senoidal1")
    ax1.set_ylabel("Y[amplitud]")
    ax1.set_xlabel("X[rads]")
    ax1.set_xlim([0, 4*np.pi])
    ax1.set_ylim([-4, 4])
    ax1.legend()

    ax2.plot(x, 2*np.sin(x), color='c', marker='+', label='y=2*sin(x)')
    ax2.set_facecolor('whitesmoke')
    ax2.set_title("Senoidal2")
    ax2.set_ylabel("Y[amplitud]")
    ax2.set_xlabel("X[rads]")
    ax2.set_xlim([0, 4*np.pi])
    ax2.set_ylim([-4, 4])
    ax2.legend()

    ax3.plot(x, 3*np.sin(x), color='g', marker='.', label='y=3*sin(x)')
    ax3.set_facecolor('whitesmoke')
    ax3.set_title("Senoidal3", position=(0.5, 0.85))  # h=center, v=top
    ax3.set_ylabel("Y[amplitud]")
    ax3.set_xlabel("X[rads]")
    ax3.set_xlim([0, 4*np.pi])
    ax3.set_ylim([-4, 4])
    ax3.legend()

    ax4.plot(x, 4*np.sin(x), color='k', label='y=4*sin(x)')
    ax4.set_facecolor('whitesmoke')
    ax4.set_title("Senoidal4", position=(0.5, 0.85))  # h=center, v=top
    ax4.set_ylabel("Y[amplitud]")
    ax4.set_xlabel("X[rads]")
    ax4.set_xlim([0, 4*np.pi])
    ax4.set_ylim([-4, 4])
    ax4.legend()

    # Graficar la figura con los 4 axes
    plt.show()


def marker_color():
    # Veremos para que sirven los "marker"
    # Supongamos que estoy midiendo la velocidad de un auto en diferentes
    # intervalos de tiempo en segundos, supongamos que realicé 4 mediciones
    # a 0seg, 1seg, 2seg y 3seg distintas velocidades en km/h:
    t = [0, 1, 2, 3]
    vel = [0, 10, 40, 40]

    # Realizaremos dos gráficos, uno sin marker y otro con marker
    # Dibujar 2 gráficos en una misma figura
    fig = plt.figure()
    fig.suptitle('Velocidad de un coche', fontsize=16)
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    ax1.plot(t, vel)
    ax1.set_facecolor('whitesmoke')
    ax2.plot(t, vel, marker='^', mec='r', ms=10)
    ax2.set_facecolor('whitesmoke')
    plt.show(block=False)

    # Realizaremos dos gráficos, con distinto tipo de línea y color
    # Dibujar 2 gráficos en una misma figura
    fig = plt.figure()
    fig.suptitle('Velocidad de un coche', fontsize=16)
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    ax1.plot(t, vel, color='r')
    ax1.set_facecolor('whitesmoke')
    ax2.plot(t, vel, c=(0, 0.5, 0.5), ls='--', lw='2')
    ax2.set_facecolor('whitesmoke')
    plt.show()


def grid():
    # Veremos los distintos tipos de grids
    t = range(-10, 10, 1)
    x2 = [x**2 for x in t]

    # Realizaremos dos gráficos, con distinto tipo de línea y color
    # Dibujar 2 gráficos en una misma figura
    fig = plt.figure()
    fig.suptitle('Función cuadrática', fontsize=16)
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    ax1.plot(t, x2, color='darkred')
    ax1.set_facecolor('whitesmoke')
    ax1.grid(ls='dashed')
    ax2.plot(t, x2, c='darkgreen', ls='--')
    ax2.set_facecolor('whitesmoke')
    ax2.grid(ls='dashdot')
    plt.show()


def line_plot():
    # Demostración de uso de line plot con una sola variable
    # Generaremos la función y=X^2 (x al cuadradro)
    # pero solo graficaremos los valores de "Y" indepedientes de "X"
    x = range(-10, 11, 2)
    y = [i**2 for i in x]

    fig = plt.figure()
    fig.suptitle('Graficar "Y" independiente de "X"', fontsize=14)
    ax = fig.add_subplot()

    ax.plot(y, c='darkred', marker='^', ms=10, label='y=x**2')
    ax.legend()
    ax.grid()
    custom_ticks = np.linspace(0, 10, 11, dtype=int)
    ax.set_xticks(custom_ticks)
    ax.set_facecolor('whitesmoke')
    plt.show(block=False)

    # Demostracion de line plot junto con grid layout
    gs = gridspec.GridSpec(2, 2)     # (row, col)
    fig = plt.figure()
    ax1 = fig.add_subplot(gs[0, 0])  # row 0, col 0
    ax2 = fig.add_subplot(gs[0, 1])  # row 0, col 1
    ax3 = fig.add_subplot(gs[1, :])  # row 1, toma todas las col

    x = np.linspace(0, 4*np.pi, 100)

    ax1.plot(x, np.sin(x), color='darkgreen', label='y=sin(x)')
    ax1.set_facecolor('whitesmoke')
    ax1.legend()
    ax1.grid('solid')

    ax2.plot(x, np.sin(2*x), color='darkblue', label='y=sin(2*x)')
    ax2.set_facecolor('whitesmoke')
    ax2.legend()
    ax2.grid('solid')

    ax3.plot(x, np.sin(2*x) + np.sin(x), color='gold',
             label='y=sin(2*x) + sin(x)'
             )
    ax3.set_facecolor('whitesmoke')
    ax3.legend()
    ax3.grid('solid')
    plt.show()


def scatter_plot():
    # Demostración de la utilidad del scatter plot
    # Generaremos una linea y=x con ruido sumando
    # valores aleatorios uniformes en cada punto
    sample_size = 20
    x = np.linspace(0, 10, sample_size)
    y = x + np.random.uniform(-1, 1, sample_size)

    fig = plt.figure()
    fig.suptitle('Line vs Scatter', fontsize=16)
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    ax1.plot(x, y, c='darkcyan')
    ax1.set_facecolor('whitesmoke')
    ax1.grid('solid')
    ax2.scatter(x, y, c='darkcyan')
    ax2.set_facecolor('whitesmoke')
    ax2.grid('solid')
    plt.show(block=False)

    np.random.shuffle(x)
    y = x + np.random.uniform(-1, 1, sample_size)

    fig = plt.figure()
    fig.suptitle('Line vs Scatter', fontsize=16)
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    ax1.plot(x, y, c='darkmagenta')
    ax1.set_facecolor('whitesmoke')
    ax1.grid('solid')
    ax2.scatter(x, y, c='darkmagenta')
    ax2.set_facecolor('whitesmoke')
    ax2.grid('solid')
    plt.show()


def bar_plot():
    # Utilizar el gráfico de barras para comparar el consumo
    # de productos por trimestre
    trimestres = [1, 2, 3, 4]
    trimestres_label = ['En-Mar', 'Abr-Jun', 'Jul-Sep', 'Oct-Dic']
    carne = [20, 23, 30, 26]
    fruta = [25, 23, 16, 21]
    verdura = [22, 18, 15, 20]

    fig = plt.figure()
    fig.suptitle('Gastos Comida', fontsize=16)
    ax1 = fig.add_subplot(3, 1, 1)
    ax2 = fig.add_subplot(3, 1, 2)
    ax3 = fig.add_subplot(3, 1, 3)

    ax1.bar(trimestres, carne, label='carne')
    ax1.set_facecolor('whitesmoke')
    ax1.legend()

    ax2.bar(trimestres, fruta, label='fruta')
    ax2.set_facecolor('whitesmoke')
    ax2.legend()

    ax3.bar(trimestres, verdura, label='verdura')
    ax3.set_facecolor('whitesmoke')
    ax3.legend()
    plt.show(block=False)

    # Bar plot "apilados" (stack)
    fig = plt.figure()
    fig.suptitle('Gastos Comida', fontsize=16)
    ax = fig.add_subplot()

    ax.bar(trimestres_label, carne, label='carne')
    ax.bar(trimestres_label, fruta, bottom=carne, label='fruta')
    ax.bar(trimestres_label, verdura,
           bottom=[sum(x) for x in zip(carne, fruta)], label='verdura'
           )
    ax.set_facecolor('whitesmoke')
    ax.legend()
    plt.show(block=False)

    # Bar plot "agrupados" (grouped)
    trimestres = np.array([1, 2, 3, 4])
    width = 0.2  # Tamaño de la barra
    fig = plt.figure()
    fig.suptitle('Gastos Comida', fontsize=16)
    ax = fig.add_subplot()

    ax.bar(trimestres, carne, width=width, label='carne')
    ax.bar(trimestres + width, fruta, width=width, label='fruta')
    ax.bar(trimestres + 2*width, verdura, width=width, label='verdura')
    ax.set_facecolor('whitesmoke')
    ax.legend()
    ax.set_xticks(trimestres + width / 3)
    ax.set_xticklabels(trimestres_label)
    plt.show()


def pie_plot():
    # Utilizar gráfico de torta para evaluar la distribución
    # Segmetar el consumo en una lista de diccionarios tal como
    # si hubiera venido de un archivo.
    # Ahora los trimestres van del 0 al 3
    consumo = [{'carne': 20, 'fruta': 25, 'verdura': 22},
               {'carne': 23, 'fruta': 23, 'verdura': 18},
               {'carne': 30, 'fruta': 16, 'verdura': 15},
               {'carne': 26, 'fruta': 21, 'verdura': 20},
               ]

    trimestres = {'En-Mar': 0, 'Abr-Jun': 1, 'Jul-Sep': 2, 'Oct-Dic': 3}

    fig = plt.figure()
    fig.suptitle('Gastos Comida de Enero-Marzo', fontsize=16)
    ax = fig.add_subplot()

    index = trimestres['En-Mar']

    ax.pie(consumo[index].values(), labels=consumo[index].keys(),
           autopct='%1.1f%%', shadow=True, startangle=90
           )
    # Igualo la relacion de aspecto para que se vea como un círculo
    ax.axis('equal')
    plt.show(block=False)

    fig = plt.figure()
    fig.suptitle('Gastos Comida de Julio-Septiembre', fontsize=16)
    ax = fig.add_subplot()

    index = trimestres['Jul-Sep']
    explode = (0.1, 0, 0)  # solo resaltar el consumo de carne

    ax.pie(consumo[index].values(), labels=consumo[index].keys(),
           explode=explode, autopct='%1.1f%%', shadow=True, startangle=90
           )
    ax.axis('equal')
    plt.show()


def cursores():
    # Demostración de como funcionan los cursores
    x = np.linspace(0, 4*np.pi, 100)
    y1 = np.sin(x)
    y2 = np.sin(x+np.pi/3)
    y3 = np.sin(x+np.pi*2/3)

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(x, y1, c='b')
    ax.plot(x, y2, c='g')
    ax.plot(x, y3, c='r')
    ax.set_title('Cursores')
    ax.grid()
    mplcursors.cursor(multiple=True)
    plt.show()


def file_plot():
    # Como gráficar datos provenientes de un archivo CSV
    # Supongamos que el archivo tiene dos columnas "X" e "Y"
    # las cuales representan mediciones efectuadas
    # Para poder plotear esa información hacemos
    # la comprension de listas o slicing según como almacenamos
    # los datos de entrada (en una lista de diccionarios o Numpy)

    datos1 = [{'X': 0, 'Y': 0},
              {'X': 1, 'Y': 1},
              {'X': 2, 'Y': 1.414},
              {'X': 3, 'Y': 1.732},
              {'X': 4, 'Y': 2.0},
              {'X': 5, 'Y': 2.236},
              {'X': 6, 'Y': 2.449},
              {'X': 7, 'Y': 2.645},
              ]

    # Debo utilizar comprension de listas para separar
    # las coulmnas "X" e "Y" en lista de datos
    x = [data['X'] for data in datos1]
    y = [data['Y'] for data in datos1]

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(x, y, c='r')
    ax.grid()
    ax.set_facecolor('whitesmoke')
    plt.show(block=False)

    # Veamos ahora la diferencia si el archivo CSV
    # lo hubieramos leido con Numpy y generado
    # una matriz de con 2 columnas (col=0 X, col=1 Y)
    datos2 = np.array([[0, 0],
                       [1, 1],
                       [2, 1.414],
                       [3, 1.732],
                       [4, 2.0],
                       [5, 2.236],
                       [6, 2.449],
                       [7, 2.645],
                       ])

    # Muy facilmente puedo obtener los datos
    # utilizando slicing de Numpy
    x = datos2[:, 0]
    y = datos2[:, 1]

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(x, y, c='b')
    ax.grid()
    ax.set_facecolor('whitesmoke')
    plt.show(block=False)

    # Supongamos ahora que solo deseamos graficar para aquellos
    # valores de X que sean mayor o igual a 2
    # Veamos que sucede en cada caso.

    # En el caso de compresion de listas podemos primero filtrar
    # el dataset por los valores de X o filtrar el dataset
    # mientras estamos generando los datos de "X" e "Y"
    # Para que quede más claro haremos la operacion en dos partes

    # Filtrar el dataset por los valores de X
    filter_dataset = [data for data in datos1 if data['X'] >= 2]

    # Debo utilizar comprension de listas para separar
    # las coulmnas "X" e "Y" en lista de datos
    x1 = [data['X'] for data in filter_dataset]
    y1 = [data['Y'] for data in filter_dataset]

    # En el caso de utilizar Numpy lo más práctico y eficiente
    # es utilizar slicing con máscaras

    # Primero realizaremos una máscara que nos devuelva todas las filas
    # en donde X>=2:
    mask = datos2[:, 0] >= 2

    # Obtenemos nuestro dataset filtrado por la mascara
    filter_dataset2 = datos2[mask, :]

    # Utilizamos slicing de Numpy para seprar X e Y
    x2 = filter_dataset2[:, 0]
    y2 = filter_dataset2[:, 1]

    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    ax1.plot(x1, y1, c='r')
    ax1.grid()
    ax1.set_facecolor('whitesmoke')

    ax2.plot(x2, y2, c='b')
    ax2.grid()
    ax2.set_facecolor('whitesmoke')

    plt.show()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ---- Introducción y personalización de gráficos ---- #
    # simple_plot()
    # multi_plot()
    # marker_color()
    # grid()
    # ---------------- Tipos de gráficos ---------------- #
    line_plot()
    scatter_plot()
    bar_plot()
    pie_plot()
    # --------------------------------------------------- #
    cursores()
    file_plot()
