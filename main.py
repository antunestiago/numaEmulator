from node import *
import binascii

Nodes = [Node(i) for i in range(256)] #criar 256 nos

f = open('entrada.txt','r') #abre o arquivo com as entradas de programacao
text = f.read() #coloca em uma string
words = text.split() #coloca uma lista, em que cada palavra e uma posicao na lista
hexdecimal = words[1]
print words[1]
binario = bin(int(hexdecimal,16)) #converte hexdeciamal para binario
print binario
print words
print Nodes[1].memory, Nodes[1].cache, Nodes[1].diretorio,Nodes[5].cpu
