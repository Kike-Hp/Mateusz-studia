#!/usr/bin/env python

from __future__ import division
import skimage as ski
import skimage.io as si
import skimage.filters as filters
import skimage.morphology as mp
import matplotlib as mat
import pylab
from skimage import img_as_float, img_as_ubyte


def obrysuj(bw):
    MIN = 100 / 256
    MAX = 125 / 256
    bw = (bw - MIN) / (MAX - MIN)
    print bw
    bw[bw > 1] = 1
    bw[bw < 0] = 0
    bw = filters.sobel(bw)
    bw = mp.dilation(mp.erosion(bw))
    bw = mp.erosion(mp.dilation(bw))
    return bw

mat.pylab.figure(figsize = (40, 30)) # rozmiar obszaru
mat.pylab.tight_layout() #zapobiega wychodzieniu etykiety lub tytulu poza obszar ysunku
mat.pylab.subplots_adjust(wspace = 0, hspace = 0) #dostrajanie ukladu
j = 1 #zmienna j

for i in [1, 2, 3, 8, 13, 14, 16, 18]: #nr obrazkow
    if(i < 10): #tworze zmeinne t  bedaca liczba dwucyfrowa
        t = '0' + str(i) #tworzy zmienna t np 01, 02 ...
    else:
        t = str(i)
    imagine = si.imread("samolot" + t + ".jpg", as_grey = True) #zaladuj obraz z pliku, as_grey - konwertuje kolorowe obrazy na skale szarosci 
    imagine = obrysuj(imagine) # wywolanie funkcji
    mat.pylab.subplot(3, 3, j)
    si.imshow(imagine, cmap = 'gray')

    mat.pylab.axis("off")
    j += 1
mat.pyplot.show()
    
    