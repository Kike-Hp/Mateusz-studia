#!/usr/bin/env python

from __future__ import division             # The Future Division Statement. If from __future__ import division is present in a module, or if -Qnew is used, 
# the / and /= operators are translated to true division opcodes; otherwise they are translated to classic division 
import matplotlib
matplotlib.use('Agg')                       # renderowanie plikow bez GUI
import math
import matplotlib.pyplot as plt
import numpy as np


def plot_color_gradients(gradients, names):
    plt.rc('legend', fontsize = 10) #ustawienie legendy
    column_width_pt = 400         # Show in latex using \the\linewidth
    pt_per_inch = 72
    size = column_width_pt / pt_per_inch #rozmiar okna
    fig, axes = plt.subplots(nrows = len(gradients), sharex = True, figsize = (size, 0.75 * size)) #definiowanie obszaru i wlasciwosci
    fig.subplots_adjust(top = 1.00, bottom= 0.05, left = 0.25, right = 0.95) #padding

    for ax, gradient, name in zip(axes, gradients, names): # Create image with two lines and draw gradient on it
        img = np.zeros((2, 1024, 3))
        for i, v in enumerate(np.linspace(0, 1, 1024)):
            img[:, i] = gradient(v)
        im = ax.imshow(img, aspect = 'auto')
        im.set_extent([0, 1, 0, 1])
        ax.yaxis.set_visible(False)
        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.25
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, name, va = 'center', ha = 'left', fontsize = 10)

    fig.savefig('gradients.pdf')
    

def colorme(v,colv):
    r = 0
    g = 0
    b = 0   
    size = len(colv)-1
    for i in range(1, len(colv)): #i - numer przejscia
        if v < i/size:
            break    
    colorchange = [colv[i][0]-colv[i-1][0], colv[i][1]-colv[i-1][1], colv[i][2]-colv[i-1][2]] #zmiany kolorow - 0 = brak zmian, + = zwieskszanie, - = zmniejszanie
    change = (v-(i-1)/size)*size #zmiana
    
    if colorchange[0] == 0:
        r = colv[i][0]
    elif colorchange[0] > 0:
        r = change
    else:
        r = 1-change 
    
    if colorchange[1] == 0:
        g = colv[i][1]
    elif colorchange[1] > 0:
        g = change
    else:
        g = 1-change
        
    if colorchange[2] == 0:
        b = colv[i][2]
    elif colorchange[2] > 0:
        b = change
    else:
        b = 1-change

    return(r,g,b)


def hsv2rgb(h, s, v):
    r = 0.0
    g = 0.0
    b = 0.0
    if v != 0:
        h /= 60.0
        i = int(h)
        f = h-i
        p = v*(1-s)
        q = v*(1-(s*f))
        t = v*(1-(s*(1-f)))
        
        if i == 0: r,g,b=(v, t, p)
        elif i == 1: r, g, b = (q, v, p)
        elif i == 2: r, g, b = (p, v, t)
        elif i == 3: r, g, b = (p, q, v)
        elif i == 4: r, g, b = (t, p, v)
        elif i == 5: r, g, b = (v, p, q)
    return r, g, b

def gradient_rgb_bw(v):
    return (v, v, v)


def gradient_rgb_gbr(v):
    r = 0
    g = 0
    b = 0
    #[0, 1, 0] [0, 0, 1][1, 0, 0]
    
    if v < 0.5:
        r = 0
        g = 1-2*v
        b = v*2
    else:
        r = 2*v-1 
        g = 0
        b = 2-2*v
        
    r, g, b = colorme(v, [[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    return (r, g, b)


def gradient_rgb_gbr_full(v):
    r, g, b = colorme(v, [[0, 1, 0], [0, 1, 1], [0, 0, 1], [1, 0, 1], [1, 0, 0]])
    return (r, g, b)


def gradient_rgb_wb_custom(v):
    r, g, b = colorme(v, [[1, 1, 1], [0, 1, 1], [1, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 1], [1, 1, 0], [0, 0, 0]])
    return (r, g, b)


def gradient_hsv_bw(v):
    return (hsv2rgb(0, 0, v))


def gradient_hsv_gbr(v):   
    return (hsv2rgb(v*240+120, 1, 1) )

def gradient_hsv_unknown(v):
    r, g, b = hsv2rgb(120-120*v, 0.5, 1)
    return (r, g, b)


def gradient_hsv_custom(v):
    return hsv2rgb((200+3*v*360)%360, ((v*10)%10)/10, 1-((v*10)%10)/37)



def toname(g):
    return g.__name__.replace('gradient_', '').replace('_', '-').upper()

gradients = (gradient_rgb_bw, gradient_rgb_gbr, gradient_rgb_gbr_full, gradient_rgb_wb_custom,
             gradient_hsv_bw, gradient_hsv_gbr, gradient_hsv_unknown, gradient_hsv_custom)

plot_color_gradients(gradients, [toname(g) for g in gradients])