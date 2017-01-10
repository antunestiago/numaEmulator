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

    
