import binascii

class EndFisico():

    def __init__(self):
        self.offset = 0
        self.endBloco = 0
        self.no = 0

    def converteToEndFis(self, endBin):
        self.offset = int(endBin[27:32],2)
        self.bloco = int(endBin[9:26],2)
        self.no = int(endBin[0:8],2)
