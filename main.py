from node import *
from endBin2endFis import *
import binascii
import random

Nodes = [Node(i) for i in range(256)] #criar 256 nos

f = open('entrada.txt','r') #abre o arquivo com as entradas de programacao
text = f.read() #coloca em uma string
words = text.split() #coloca uma lista, em que cada palavra e uma posicao na lista

i=0
#le a lista e decide as funcoes
while(i < len(words)):
        if words[i] =="load":
            hexdecimal = words[i+1]
            cpu = random.randint(0,255)
            print cpu
            Nodes[cpu].load(hexdecimal,Nodes)
        elif words[i] =="store":
            hexdecimal = words[i+1]
            cpu = random.randint(0,255)
            print "No:",cpu,"-> store"
            Nodes[cpu].store(hexdecimal,Nodes)
        i = i+2
