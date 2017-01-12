from endBin2endFis import *

class Node:

    def __init__(self,cpuIndex):
        """ a estrutura de um no possui uma lista de diretorios
        lista representando a cache e outra representando a memoria local
        """
        self.cache = []
        self.memory = []
        self.diretorio = []
        self.cpu = cpuIndex

    def insereCache(self, indiceC, conteudoC):
        self.cache.insert(indice,conteudo)

    def insereMemoria(self,indiceM,conteudoM):
        self.memory.insert(indice,conteudo)

    def insereDiretorio(self,indiceD,conteudoD):
        self.memory.insert(indice,conteudo)

    def load(self,hexadecimal):
        end_fisico = EndFisico() #classe que contem metodo para endereco fisico
        binario = bin(int(hexadecimal,16)) #converte hexdeciamal para binario
        end_fisico.converteToEndFis(binario) #metodo que converte o endereco binario para o fisico
        print "valor em load:"
        print end_fisico.offset

    def store(self,hexadecimal):
        end_fisico = EndFisico() #classe que contem metodo para endereco fisico
        binario = bin(int(hexadecimal,16)) #converte hexdeciamal para binario
        end_fisico.converteToEndFis(binario) #metodo que converte o endereco binario para o fisico
        print "valor em store:"
        print end_fisico.offset
