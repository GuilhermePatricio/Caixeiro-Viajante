# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 22:36:10 2019

@author: 10226802698
"""
import random
import time


def NEARESTNEIGHBOR(MatrizAdj):
    
    naoVisitados = [x for x in range(len(MatrizAdj))] #vetor com todas as posiçoes da matriz
    u = 0 #vertice inicial
    S = [] #lista que contem a sequencia de vertices
    S.append(u) #adiciona o vertice inicial a lista de vertices
    naoVisitados.remove(u) #remove o vertice visitado
    infinito = 999999
    
    while (len(naoVisitados) != 0):
        menorDistancia = infinito
        for i in naoVisitados:
            if MatrizAdj[u][i] < menorDistancia: #compara se o peso da matriz na posição (u,i) é menor que a menor distancia
                v = i #v recebe o vertice de desitino com a menor distancia
                menorDistancia = MatrizAdj[u][i] #a menor distancia é atualizada
        S.append(v) #adiciona o vertice na lista que contem a rota
        naoVisitados.remove(v)#remove o vertice visitado
        u = v #atualiza o proximo vertice que sera verificado
    S.append(S[0]) #adiciona o vertice inicial ao fim da fila
    return S
    
def AVALIA(MatrizAdj,S):
    custo = 0
    for i in range(len(S)-1):
        u = S[i] #vertice de origem 
        v = S[i+1] #vertice de destino
        w = MatrizAdj[u][v] #peso da matriz na posição (u,v)
        custo = custo + w #atualiza o custo
    return custo
    
def TWOOPT(MatrizAdj,S):
    inicio = time.time() #pega o tempo de quando a função é iniciada
    fim = 0
    
    while (fim - inicio <= 60): #roda por 60 segundos
        
        i1 = random.randint(1,(len(S)-2)) #indice aleatorio de S exeto o primeiro e o ultimo
        i2 = random.randint(1,(len(S)-2)) #indice aleatorio de S exeto o primeiro e o ultimo
        
       
        if i1 != i2:
            S1 = [x for x in S] #S1 = S
            
            #aux1 recebe o valor de S1 na posição i1 e aux2 recebe o valor de S1 na posição i2
            aux1= S1[i1]
            aux2= S1[i2]
            #troca S1[i1] com s1[i2]
            S1[i1] = aux2
            S1[i2] = aux1

            if AVALIA(MatrizAdj,S1) < AVALIA(MatrizAdj,S): #se S1 é melhor que S atualiza S 
                S = S1
        fim = time.time() #pega o tempo de quando a função chega no final
    return S
           
            