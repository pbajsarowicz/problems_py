#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division             # Division in Python 2.7
import matplotlib
matplotlib.use('Agg')                       # So that we can render files without GUI
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

from matplotlib import colors
import colorsys

def wczytajDane(file):
    data = []
    with open(file, 'r') as f:
        data = f.readlines()
    X = {}
    width = 0
    height = 0
    distance = 0
    #OX
    #width, height, distance = data[0].split(' ')

    print data[0], data[1], data[2]
    for element in range(0, len(data)):
        temp = data[element].split(' ')
        X[element] = temp
    print X[0], X[1], X[2]
    (width, height, distance) = X[0]
    return width, height, distance, X

def plot_color_gradients(gradients, names, width, height, distance, data):
    # For pretty latex fonts (commented out, because it does not work on some machines)
    #rc('text', usetex=True) 
    #rc('font', family='serif', serif=['Times'], size=10)
    rc('legend', fontsize=10)

    column_width_pt = width         # Show in latex using \the\linewidth
    pt_per_inch = distance
    size = column_width_pt / pt_per_inch

    fig, axes = plt.subplots(nrows=len(gradients), sharex=True, figsize=(size, 0.75 * size))
    fig.subplots_adjust(top=1.00, bottom=0.05, left=0.25, right=0.95)


    for ax, gradient, name in zip(axes, gradients, names):
        # Create image with two lines and draw gradient on it
        img = np.zeros((2, height, 3))
        for i, v in enumerate(np.linspace(0, 1, 1024)):
            img[:, i] = gradient(v)

        im = ax.imshow(img, aspect='auto')
        im.set_extent([0, 1, 0, 1])
        ax.yaxis.set_visible(False)

        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.25
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, name, va='center', ha='left', fontsize=10)

    fig.savefig('my-gradients.pdf')

def gradient_rgb_bw(v):
    return (1*v, 1*v, 1*v)


def gradient_rgb_gbr(v):
    if v < 0.5:
        return (0,1-v*2,v*2)
    else:
        v -= 0.5
        return (v*2,0,1-v*2)

def gradient_rgb_gbr_full(v):
    if v <= 0.25:
        return (0,1,v*4-1)
    elif v <= 0.5:
        v -= 0.25
        return (0,1-4*v,1)
    elif v <= 0.75:
        v -= 0.5
        return (v*4,0,1)
    else:
        v -= 0.75
        return (1,0,1-v*4)


def gradient_rgb_wb_custom(v):
    n = 1/7
    x = 7
    if v <= n*1:
        return (1, 1-x*v, 1)
    elif v <= n*2:
        v -= n*1
        return (1-x*v,0,1)
    elif v <= n*3:
        v -= n*2
        return (0,x*v,1)
    elif v <= n*4:
        v -= n*3
        return (0,1,1-x*v)
    elif v <= n*5:
        v -= n*4
        return (v*x,1,0)
    elif v <= n*6:
        v -= n*5
        return (1,1-x*v,0)
    else: # v< n*7:
        v -= n*6
        return (1-x*v,0,0)

#odcien nasycenie jaskrawosc
def gradient_hsv_bw(v):
    return colorsys.hsv_to_rgb(0, 0, v)


def gradient_hsv_gbr(v):
    v += 0.4
    return colorsys.hsv_to_rgb(v*0.73, 1, 1)

def gradient_hsv_unknown(v):
    v = 1-v
    return colorsys.hsv_to_rgb(v*0.3, 0.5, 1)
    #<0.3; 0>

def gradient_hsv_custom(v):
    return colorsys.hsv_to_rgb(v, 1-v, 1)


if __name__ == '__main__':
    """def toname(g):
        return g.__name__.replace('gradient_', '').replace('_', '-').upper()

    gradients = (gradient_rgb_bw, gradient_rgb_gbr, gradient_rgb_gbr_full, gradient_rgb_wb_custom,
                 gradient_hsv_bw, gradient_hsv_gbr, gradient_hsv_unknown, gradient_hsv_custom)

    plot_color_gradients(gradients, [toname(g) for g in gradients])"""
    data = {}
    (w,h,d,data) = wczytajDane('big.dem.txt')
    print w, h, d
    plt.figure(figsize=(int(w), int(h)))

    for x in data:
        img = np.zeros((int(w), int(h), 3))
        for i, v in enumerate(np.linspace(0, int(w), 1)):
            img[:, i] = gradient_rgb_gbr_full(v)

    plt.savefig('mymap.pdf')
    plt.close()
