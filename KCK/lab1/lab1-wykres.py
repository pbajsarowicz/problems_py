import matplotlib.pyplot as plt
import numpy as np
from sys import *
from numpy.matlib import rand
from pylab import *

def wczytajDane(file,x):
    data = []
    with open(file, 'r') as f:
        data = f.readlines()
    X = []
    Y = []
    #OX
    for element in range(1, len(data)):
        temp = data[element].split(',')
        X.append(float(temp[1]) / x)
        #OY srednia
    for element in range(1, len(data)):
        temp = data[element].split(',')
        temp = [float(l) for l in temp]
        Y.append(np.mean(temp[2:]))

    return X, Y



def main():
    plt.figure(figsize=(6.7, 5))

    #plt.xticks(np.arange(4),  ('Bill', 'Fred', 'Mary', 'Sue'))
    #Formatowanie wykresu

    ax1 = plt.subplot(1, 2, 1)

    plt.grid(True)
    ax1.xaxis.set_ticks_position("bottom")
    plt.xticks((100, 200, 300, 400, 500),fontsize = 9)#, verticalalignment='bottom')
    #plt.xticks([0, 40, 80, 120, 160, 200],('one','two','three','four','five','six'),rotation='vertical',verticalalignment='bottom')
    plt.yticks((np.arange(0.6, 1.0, 0.05)),fontsize = 9)
    plt.xlabel('Rozegranych gier (x 1000)',fontsize = 9)
    plt.ylabel('Odsetek wygranych gier [%]',fontsize = 9)
    plt.title('Pokolenie',fontsize = 9)

    plt.xticks((100, 200, 300, 400, 500),fontsize = 9)#, verticalalignment='bottom')

    #Ladowanie danych z plikow
    TwoCelX, TwoCelY = wczytajDane('2cel.csv',1000)
    TwoCelRsX, TwoCelRsY = wczytajDane('2cel-rs.csv',1000)
    CelX, CelY = wczytajDane('cel.csv',1000)
    CelRsX, CelRsY = wczytajDane('cel-rs.csv',1000)
    RselX, RselY = wczytajDane('rsel.csv',1000)


    #print file2celY

    #plt.scatter(RselX, RselY, marker='o')
   #plt.scatter._legmarker.set_markevery(5)


    p1A, = plt.plot(RselX, RselY, color='blue',label='1-Evol-RS')
    p1B, = plt.plot(RselX, RselY, 'o', markevery=25, color='blue')

    p2A, = plt.plot(CelRsX, CelRsY, color='green')
    p2B, = plt.plot(CelRsX, CelRsY, 'v', markevery=25, color='green')

    p3A, = plt.plot(TwoCelRsX, TwoCelRsY, color='red')
    p3B, = plt.plot(TwoCelRsX, TwoCelRsY, 'D', markevery=25, color='red')

    p4A, = plt.plot(CelX, CelY, color='black')
    p4B, = plt.plot(CelX, CelY, 's', markevery=25, color='black')

    p5A, = plt.plot(TwoCelX, TwoCelY, color='magenta')
    p5B, = plt.plot(TwoCelX, TwoCelY, 'd', markevery=25, color='magenta')

    plt.legend([(p1A,p1B),(p2A,p2B),(p3A,p3B),(p4A,p4B),(p5A,p5B)],['1-Evol-RS','1-Coev-RS','2-Coev-RS','1-Coev','2-Coev'], loc=4, fontsize = 9)
    #plt.legend(loc=4)

    #plt.legend(('1-Evol-RS','1-Coev-RS','2-Coev-RS','1-Coev','2-Coev'))
    #plt.plot([110000,210000,410000,500000],[0.1,0.2,0.8,0.9])

    ax2 = plt.subplot(1, 2, 2)
    plt.grid(True)


    #Ladowanie danych z plikow
    TwoCelX2, TwoCelY2 = wczytajDane('2cel.csv',1000)
    TwoCelRsX2, TwoCelRsY2 = wczytajDane('2cel-rs.csv',1000)
    CelX2, CelY2 = wczytajDane('cel.csv',1000)
    CelRsX2, CelRsY2 = wczytajDane('cel-rs.csv',1000)
    RselX2, RselY2 = wczytajDane('rsel.csv',1000)






    plt.boxplot((RselY2,CelRsY2,TwoCelY2,CelY2,TwoCelY2),notch=True,bootstrap=100)
    distR = ["a","b","c","d","e"]
    #plt.setp(xticklables = np.repeat(distR,2))
    ax2.yaxis.tick_right()
    plt.yticks(np.arange(0.6, 1.05, 0.05),fontsize = 9)
    plt.xticks(np.arange(1,6),('1-Evol-RS','1-Coev-RS','2-Coev-RS','1-Coev','2-Coev'), rotation = -330, fontsize = 9)


    """p3 = plt.boxplot(CelX, CelY)
    p4 = plt.boxplot(CelRsX, CelRsY)
    p5 = plt.boxplot(RselX, RselY)
    (x, notch=False, sym='+', vert=True, whis=1.5,
        positions=None, widths=None, patch_artist=False,
        bootstrap=None, usermedians=None, conf_intervals=None)


    """

    plt.savefig('myplot.pdf')
    plt.close()


if __name__ == '__main__':
    main()
