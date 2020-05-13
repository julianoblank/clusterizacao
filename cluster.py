import math
import numpy as np
import matplotlib.pyplot


def verificaMenorCaminho(listaDistanciaC1Calculada,listaDistanciaC2Calculada):
  menorDistancia = []
  for num, listaC1 in enumerate(listaDistanciaC1Calculada):
    for num2, listaC2 in enumerate(listaDistanciaC2Calculada):
      if(num == num2):
        if(listaC1 < listaC2):
          menorDistancia.append("C1")
        else:
          menorDistancia.append("C2")
  return menorDistancia            


def calcularDistanciaC1(mediaDisciplinas, faltas, distanciasC1):
  resultadoC1 = []
  for num, media in enumerate(mediaDisciplinas):
    for num2, falta in enumerate(faltas):
      if(num == num2):
        soma = ((media-distanciasC1[0]) ** 2)+((falta-distanciasC1[1]) ** 2)
        resultadoC1.append(math.sqrt(soma))
  return resultadoC1


def calcularDistanciaC2(mediaDisciplinas, faltas, distanciasC2):
  resultadoC2 = []
  for num, media in enumerate(mediaDisciplinas):
    for num2, falta in enumerate(faltas):
      if(num == num2):
        soma = ((media-distanciasC2[0]) ** 2)+((falta-distanciasC2[1]) ** 2)
        resultadoC2.append(math.sqrt(soma))
  return resultadoC2

def novaMedia(listaMenorCaminho):
    somaMediaC1 = 0
    somaFaltasC1 = 0
    somaMediaC2 = 0
    somaFaltasC2 = 0
    totalC1 = 0
    totalC2 = 0
    mediaMediasC1 = 0
    mediaFaltasC1 = 0
    mediaMediasC2 = 0
    mediaFaltasC2 = 0
    C1 = False
    C2 = False
    faltasC1 = []
    faltasC2 = []
    mediasC1 = []
    mediasC2 = []
    for num, caminho in enumerate(listaMenorCaminho):
        for num2, media in enumerate(mediaDisciplinas):
            for num3, falta in enumerate(faltas):
                if(caminho == "C1"):
                    if(num == num2 == num3):
                        totalC1 += 1
                        somaMediaC1 += media
                        somaFaltasC1 += falta
                        C1 = True
                        faltasC1.append(falta)
                        mediasC1.append(media)
                else:
                    if(num == num2 == num3):
                        totalC2 += 1
                        somaMediaC2 += media
                        somaFaltasC2 += falta
                        C2 = True
                        faltasC2.append(falta)
                        mediasC2.append(media)
                if(num2 == len(listaMenorCaminho)-1 and C1 == True and C2 == True):
                    mediaMediasC1 = (somaMediaC1/totalC1)
                    mediaFaltasC1 = (somaFaltasC1/totalC1)
                    mediaMediasC2 = (somaMediaC2/totalC2)
                    mediaFaltasC2 = (somaFaltasC2/totalC2)
    return mediaMediasC1, mediaFaltasC1, mediaMediasC2, mediaFaltasC2, faltasC1, faltasC2, mediasC1, mediasC2  


def unirFaltas(faltasC1, faltasC2):
  faltasTotal = []
  for faltaC1 in faltasC1:
    faltasTotal.append(faltaC1)
  for faltaC2 in faltasC2:
    faltasTotal.append(faltaC2)  
  return faltasTotal

def unirMedias(mediasC1, mediasC2):
  mediasTotal = []
  for mediaC1 in mediasC1:
    mediasTotal.append(mediaC1)
  for mediaC2 in mediasC2:
    mediasTotal.append(mediaC2)  
  return mediasTotal  

mediaDisciplinas = [1,5,4,4,2,1,5,1,0,1,4,3,2,0,4,1,5,3,10,7,10,9,10,7,8,10,6,6,9,9,8,6,9,7,8,8,9,10,9]
faltas = [55,57,45,59,49,42,42,40,60,18,31,5,1,30,9,12,13,7,51,51,44,37,58,50,44,45,58,6,29,28,6,15,25,22,25,26,12,36,32]
distanciaC1Inicial = [5,60]
distanciaC2Inicial = [8,16]

listaDistanciaC1Calculada = calcularDistanciaC1(mediaDisciplinas, faltas, distanciaC1Inicial)
listaDistanciaC2Calculada = calcularDistanciaC2(mediaDisciplinas, faltas, distanciaC2Inicial)
listaMenorCaminho = verificaMenorCaminho(listaDistanciaC1Calculada,listaDistanciaC2Calculada)
medias = novaMedia(listaMenorCaminho)
mediaC1 = []
mediaC2 =[]
mediaC1 = (medias[0:2])
mediaC2 = (medias[2:4])


listaDistanciaC1Calculada.clear()
listaDistanciaC2Calculada.clear()

listaDistanciaC1Calculada = calcularDistanciaC1(mediaDisciplinas, faltas, mediaC1)
listaDistanciaC2Calculada = calcularDistanciaC2(mediaDisciplinas, faltas, mediaC2)

listaMenorCaminhoNova = verificaMenorCaminho(listaDistanciaC1Calculada,listaDistanciaC2Calculada)

a = np.array(listaMenorCaminho)
b = np.array(listaMenorCaminhoNova)

if(all(a==b)):
  parar=True
else:
  parar=False

contador = 0

while(parar==False):
  del medias
  medias = novaMedia(listaMenorCaminhoNova)
  mediaC1 = (medias[0:2])
  mediaC2 = (medias[2:4])
  faltasC1 = (medias[4])
  faltasC2 = (medias[5])
  mediasC1 = (medias[6])
  mediasC2 = (medias[7])
 
  break
  if(all(a==b)):
    parar=True
  else:
    parar=False
  
  contador += 1
  listaMenorCaminho.clear()
  listaMenorCaminho = listaMenorCaminhoNova.copy()

totalFaltas = unirFaltas(faltasC1, faltasC2)
totalMedias = unirMedias(mediasC1, mediasC2)

matplotlib.pyplot.scatter(faltasC2, mediasC2)
matplotlib.pyplot.title('Gráfico de possível evasão de alunos')
matplotlib.pyplot.xlabel('Faltas')
matplotlib.pyplot.ylabel('Média Disciplinas')
matplotlib.pyplot.show()