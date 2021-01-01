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


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ---- Introducción y personalización de gráficos ---- #
    simple_plot()
    multi_plot()
    marker_color()
    grid()
