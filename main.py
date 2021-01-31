# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:57:07 2019

"""

import CaixeiroViajante
import time

#Leitura do arquivo fonte do grafo
fileName = input("Arquivo do grafo:")
file =open(fileName)
str = file.readline()
str = str.split(" ")
numVertices = int(str[0])
numArestas = int(str[1])

#preenchimento das estruturas de dados
listaAdj = [[] for x in range (numVertices)]
matAdj = [[ 0 for x in range (numVertices)] for x in range(numVertices)]
vertices = [x for x in range (numVertices)]
arestas = []

for i in range(numArestas):
    str = file.readline()
    str = str.split(" ")
    origem = int (str[0])
    destino = int(str[1])
    peso = float(str[2])
    listaAdj[origem].append((destino, peso))
    matAdj[origem][destino]=peso
    arestas.append((origem,destino,peso))

S = CaixeiroViajante.NEARESTNEIGHBOR(matAdj)
print("Distancia NN:",CaixeiroViajante.AVALIA(matAdj,S))
print("Rota:", S)

inicio = time.time()
TWOOPT = CaixeiroViajante.TWOOPT(matAdj,S)
fim = time.time()
print("Distancia TWOOPT:",CaixeiroViajante.AVALIA(matAdj,TWOOPT))
print("Rota:", TWOOPT)
print("Tempo: %.3f" %( fim - inicio))

