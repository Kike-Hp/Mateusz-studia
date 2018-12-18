#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy
import os
# plit.%matplotlib inline #sets the backend of matplotlib to the "inline" backend

file_path ="/home/antoni/Downloads/Mati"
data = []


def load(file_name):
    file = open(file_name)
    file_lines = file.readlines() #wczytuje  pliki i tworze liste jeden element = jedna lina
    file_lines = [line[0:(len(line)-2)].split(',') for line in file_lines] #tworze liste elementow  - biore po kolei kazda linie, wywalam z konca znaki /r/n oraz rodzielam kazdy element jako element listy
    file.close() #zamykam plik
    file_data = [] #pusta lista
    for x in file_lines[1:]: #petla po elementach listy z pominieciem pierwszego  - nazwy tabeli
        suma=sum([float(cell) for cell in x[2:]]) #przejscie po elemencie tablicy file_lines, z pominieciem kolumny "generation"
        # oraz "effort". Zamiana na liczby zmienno przecinkowe - bo miay wczejsniej kropki oraz przypisanie ich sumy
        mean = suma/(len(x)-2) # wyliczenie sredniej arytmetycnej
        tmp=x[:2] #przypisanie do zmiennej wartosci "generation" oraz "effort" z danego wiersza
        tmp.append(mean) #dodanie do slownika powstalej sredniej
        file_data.append(tmp) # dodanie do slownika wartosci [generation, effort, srednia]
    return file_data 

data.append(load(file_path + '/rsel.csv')) #wywolanie funkcji, zwracajacej liste data  - przypisanie do zmiennnej
data.append(load(file_path + '/cel.csv'))
data.append(load(file_path + '/cel-rs.csv'))
data.append(load(file_path + '/2cel.csv'))
data.append(load(file_path + '/2cel-rs.csv'))

def plot(data):
    plt.plot([data_1[2] for data_1 in data[0]], label="rsel") #rysowanie krzywej na wykresie ( srednia jest wartoscia)
    plt.plot([data_2[2] for data_2 in data[1]], label="cel")
    plt.plot([data_3[2] for data_3 in data[2]], label="cel-rs")
    plt.plot([data_4[2] for data_4 in data[3]], label="2cel")
    plt.plot([data_5[2] for data_5 in data[4]], label="2cel-rs")
    plt.legend(loc = 'best', fontsize=24, framealpha = 1) #definicja legendy
    plt.xlabel('Pokolenie', fontsize = 20) #Podpisy osi
    plt.ylabel('Odsetek wygranych', fontsize = 20)
    plt.ylim(ymin = 0.6, ymax = 1) #wartosci osi
    plt.xlim(xmin = 0, xmax = 200)

#### NA 3

plt.figure(figsize = (14, 14)) #rozmiar figury
plot(data)
plt.show() #pokaz wykres
plt.close()

### NA 5

plt.figure(figsize = (14, 14)) #rozmiar figury
plt.subplot(121) #podzial okna na dwa
plot(data)

plt.subplot(122) #druga czesc okna
plt.boxplot([data_1[2] for data_1 in data[0]], notch = True, positions = [1], showmeans = True, meanline = True) #wykres pudelkowy, notch = If True, will produce a notched box plot. Otherwise, a rectangular boxplot is produced.
plt.boxplot([data_2[2] for data_2 in data[1]], notch = True, positions = [2], showmeans = True, meanline = True) #positions = Sets the positions of the boxes. The ticks and limits are automatically set to match the positions. Defaults to range(1, N+1) where N is the number of boxes to be drawn.
plt.boxplot([data_3[2] for data_3 in data[2]], notch = True, positions = [3], showmeans = True, meanline = True) #showmeans = Show the arithmetic means.
plt.boxplot([data_4[2] for data_4 in data[3]], notch = True, positions = [4], showmeans = True, meanline = True) #meanline = If True (and showmeans is True), will try to render the mean as a line spanning the full width of the box according to meanprops (see below). Not recommended if shownotches is also True. Otherwise, means will be shown as points.
plt.boxplot([data_5[2] for data_5 in data[4]], notch = True, positions = [5], showmeans = True, meanline = True)
plt.xlim(0,6)
plt.xticks([1, 2, 3, 4, 5], ["rsel", "cel", "cel-rs","2cel","2cel-rs"])
plt.ylim(ymin = 0.6, ymax = 1)
plt.ylabel('Odsetek wygranych', fontsize=10)
# 
plt.show()
plt.close()

