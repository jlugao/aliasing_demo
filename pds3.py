# -*- coding: utf-8 -*-
"""
Programa para demonstrar o efeito de aliasing em uma onda senoidal
com frequencia de amostragem fixa e frequência de oscilacao variavel.
Esse programa eh parte de uma serie de applets, desenvolvidas na faculdade
de engenharia de ilha solteira, feitas para demonstrar conceitos de processamento
digital de sinais.

@autor: Joao Ricardo Lhullier Lugao
@laboratorio: LUS - Laboratorio de Ultrassom
@contato: joaolhullier@gmail.com
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from scipy import signal

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar

class mywidget(QWidget):
    def __init__(self,Parent=None):
        super(mywidget,self).__init__(Parent)
        self.figure=plt.figure(figsize=(15,25),facecolor='w',dpi=50)
        self.canvas=FigureCanvas(self.figure)
        self.toolbar=NavigationToolbar(self.canvas,self)
        self.slider=QSlider(Qt.Horizontal,self)
        self.slider.setRange(1, 100)
        self.slider.setValue(5)
        self.slider.valueChanged[int].connect(self.changeValue)
        self.label=QLabel('Taxa de amostragem 50 Hz')
        self.spinbox=QSpinBox()
        self.spinbox.setValue(5)
        self.spinbox.valueChanged.connect(self.sliderchange)
        self.spinbox.setRange(1,100)
        layout=QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.slider)
        layout.addWidget(self.spinbox)
        layout.addWidget(self.label)

        self.slider.valueChanged.connect(self.changeValue)
        self.setLayout(layout)
        self.plot()
        #self.changeValue(5)

    def sliderchange(self,value):
        self.slider.setValue(value)

    def plot(self):
        self.amostrasporseg=15*5 #samples/sec
        frequenciasinal=5 #Hz
        omega= frequenciasinal
        self.z=2*np.pi*np.arange(0,2*np.pi,1/self.amostrasporseg)
        y=np.sin(self.z*omega)
        k=y*signal.hann(len(y))

        ylinha= 20*np.log10(abs(np.fft.fft(k,2048)))
        ylinha=np.tile(ylinha,3)

        zlinha=np.linspace(-2,4,len(ylinha))
        self.figure.subplots_adjust(bottom=.75)
        gs = gridspec.GridSpec(5, 1,height_ratios=[0.2,1,0.25,1,0.2])
        ax =self.figure.add_subplot(gs[1])
        self.plot2,=plt.plot(zlinha,ylinha)
        plt.title('Espectro do sinal')
        plt.xlabel(r'$\omega$')
        plt.ylabel(r'|X($\omega$)|')

        plt.xticks((-2,-1,0,1,2,3,4),[r'$-2\pi$',r'$-\pi$','0',r'$\pi$',r'$2\pi$',r'$3\pi$',r'$4\pi$'])
        #ax.set_xticks([-0.0442,0.0442], minor=True)
        ax.xaxis.grid(True,which='major',linewidth=0.75,color='k',linestyle='--')
        self.beta=self.figure.add_subplot(gs[3])
        self.plot3,=plt.plot(self.z,y,label='Amostragem Correta')
        plt.plot(self.z,y,'o',label='Amostragem Fixa')
        plt.legend(loc='upper right')
        self.beta.set_xlabel(r't')
        self.beta.set_ylabel(r'x(t)')
        self.beta.set_xlim([0,2*np.pi])
        self.figure.tight_layout()

    def changeValue(self,value):
        self.spinbox.setValue(value)
        freq = value
        znovo=np.arange(0,2*np.pi,0.001)
        omega= freq
        omeganovo= freq
        y=np.sin(self.z*omega)
        yf=np.sin(znovo*omeganovo)
        k=y*signal.hann(len(y))
        ylinha=np.fft.fft(k,2048)
        ylinha=np.tile(ylinha,3)
        self.beta.clear()
        self.beta.plot(znovo,yf,label='Amostragem Correta')
        self.beta.plot(self.z,y,'o-',lw=2,label='Amostragem Fixa')
        plt.legend(loc='upper right')
        self.beta.set_xlim([0,2*np.pi])
        self.beta.set_xlabel(r't')
        self.beta.set_ylabel(r'x(t)')
        self.beta.set_title('Sinal com amostragem correta x Sinal com amostragem fixa')
        self.plot2.set_ydata(20*np.log10(abs(ylinha)))
        self.canvas.draw()
        self.canvas.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mywidget()
    ui.show()
    sys.exit(app.exec_())
