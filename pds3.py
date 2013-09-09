# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:58:02 2013

@author: John
"""

from __future__ import division
import numpy as np
import pylab
from matplotlib.widgets import Slider
import matplotlib.gridspec as gridspec


amostrasporseg=3*5 #samples/sec
frequenciasinal=1*5 #Hz
amostrasnoperiodo=np.round(amostrasporseg/frequenciasinal,decimals=0)

omega= 2*np.pi*frequenciasinal/amostrasporseg
z=np.arange(-2*np.pi,2*np.pi,1/amostrasporseg)



zfft=np.arange(-1,1,2/len(z))
print len(z)
print len(zfft)
y=np.sin(z*omega)
ylinha= np.fft.fft(y)
#zlinha= np.fft.fftfreq(len(z))
zlinha=zfft

figura=pylab.figure(figsize=(8, 6))
figura.subplots_adjust(bottom=.75)
gs = gridspec.GridSpec(3, 1,height_ratios=[1,2,0.25])
figura.add_subplot(gs[0])
#plot1,=pylab.plot(z,y,'-')
#pylab.title('Sinal Com amostragem fixa')
#pylab.xlim([-4,4])
#figura.add_subplot(gs[0])
plot2,=pylab.plot(zlinha,abs(ylinha))
pylab.title('Espectro do sinal')
pylab.xlabel(r'$\omega$/$\pi$')
pylab.ylabel(r'|X($\omega$)|')
beta=figura.add_subplot(gs[1])
plot3,=pylab.plot(z,y,)
pylab.plot(z,y,'o')
beta.set_title('Sinal com amostragem correta x Sinal com amostragem fixa')
beta.set_xlabel(r't')
beta.set_ylabel(r'x(t)')
beta.set_xlim([-4,4])
axfreq = pylab.axes([0.25, 0.1, 0.65, 0.03])
sfreq = Slider(axfreq, 'Freq', 0, 300.0, valinit=amostrasporseg)
figura.tight_layout()

def update(val):
    freq = sfreq.val
    znovo=np.arange(-2*np.pi,2*np.pi,1/freq)
    amostragemreal= 3* sfreq.val
    omega= 2*np.pi*freq/amostrasporseg
    omega2= 2*np.pi*freq/amostrasporseg
    y=np.sin(z*omega)
    yf=np.sin(znovo*omega)
    ylinha=np.fft.fft(y)#/amostrasporseg
    #plot1.set_ydata(y)
    beta.clear()
    beta.plot(znovo,yf)
    beta.plot(z,y,'o-',lw=2)
    beta.set_xlim([-4,4])
    beta.set_xlabel(r't')
    beta.set_ylabel(r'x(t)')
    beta.set_title('Sinal com amostragem correta x Sinal com amostragem fixa')
    plot2.set_ydata(abs(ylinha))
    pylab.draw()
sfreq.on_changed(update)

pylab.show()