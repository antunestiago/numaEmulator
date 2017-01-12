from node import *
from endBin2endFis import *
import binascii

Nodes = [Node(i) for i in range(256)] #criar 256 nos

f = open('entrada.txt','r') #abre o arquivo com as entradas de programacao
text = f.read() #coloca em uma string
words = text.split() #coloca uma lista, em que cada palavra e uma posicao na lista
hexdecimal = words[1]
print words[1] #teste
binario = bin(int(hexdecimal,16)) #converte hexdeciamal para binario
print binario #teste
end_fisico = EndFisico() #classe que contem metodo para endereco fisico
end_fisico.converteToEndFis(binario) #metodo que converte o endereco binario para o fisico
print end_fisico.no #teste

#le a lista e decide as funcoes
for x in words:
    print x
    if x =="load":
        print 1
    elif x =="store":
        print 2
    else: print "que porra e essa"

print words#teste
print Nodes[1].memory, Nodes[1].cache, Nodes[1].diretorio,Nodes[5].cpu
