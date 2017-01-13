from endBin2endFis import *
import random

class Node:

    def __init__(self,cpuIndex):
        """ a estrutura de um no possui uma lista de diretorios
        lista representando a cache e outra representando a memoria local
        """
        self.cache = ['none'] * 1000
        self.diretorio = ['none'] * 262144
        self.memoria = ['none'] * 10000
        self.cpu = cpuIndex

    def insereCache(self, indiceC, conteudoC):
        self.cache.insert(indice,conteudo)

    def insereMemoria(self,indiceM,conteudoM):
        self.memory.insert(indice,conteudo)

    def insereDiretorio(self,indiceD,conteudoD):
        self.memory.insert(indice,conteudo)

    def load(self,hexadecimal, No):
        end_fisico = EndFisico() #classe que contem metodo para endereco fisico
        binario = bin(int(hexadecimal,16)) #converte hexdeciamal para binario
        end_fisico.converteToEndFis(binario) #metodo que converte o endereco binario para o fisico
        print "No:",self.cpu,"-> load"
        print "\t  byte:",end_fisico.offset
        print "\t  bloco",end_fisico.bloco
        print "\t  no",end_fisico.no
        if (self.cache.count(end_fisico)<1): #verifica se o valor nao ta na cache
                print "Valor nao se encontra na cache"
                if(No[end_fisico.no].diretorio[end_fisico.bloco]=='none'):#verifica se o bloco nao esta sendo usado por outro no
                    No[end_fisico.no].diretorio[end_fisico.bloco] = self.cpu
                    self.cache[random.randint(0,1000)] = No[end_fisico.no].cpu
                    print "Atualiza diretorio[%d] do No[%d] com No[%d]" % (end_fisico.bloco, end_fisico.no, No[end_fisico.no].diretorio[end_fisico.bloco])



                else:
                    NoConflito = No[end_fisico.no].diretorio[end_fisico.bloco] #no que houve conlito
                    print "Conflito detectado com [%d]", NoConflito
                    for indice,valor in enumerate(No[NoConflito].cache):
                        if(valor==end_fisico.no):
                            print "cache antes:", No[NoConflito].cache[indice]
                            No[NoConflito].cache[indice] = 'none'
                            print "cache depois:", No[NoConflito].cache[indice]
                            self.store(hexadecimal,No)
                            No[end_fisico.no].diretorio[end_fisico.bloco] = self.cpu
                            self.cache[random.randint(0,1000)] = No[end_fisico.no].cpu
                            print "Atualiza diretorio[%d] do No[%d] com No[%d]" % (end_fisico.bloco, end_fisico.no, No[end_fisico.no].diretorio[end_fisico.bloco])


        else: print "valor esta na cache"

    def store(self,hexadecimal,No):
        end_fisico = EndFisico() #classe que contem metodo para endereco fisico
        binario = bin(int(hexadecimal,16)) #converte hexdeciamal para binario
        end_fisico.converteToEndFis(binario) #metodo que converte o endereco binario para o fisico
        No[end_fisico.no].memoria[(end_fisico.bloco-1*6)+end_fisico.offset] = 'data'
        print "Escrito na Memoria[%d] do No[%d]" % (((end_fisico.bloco-1)*4)+end_fisico.offset, end_fisico.no)
