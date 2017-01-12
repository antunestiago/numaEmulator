import binascii

class EndFisico():

    def __init__(self):
        self.offset = 0
        self.endBloco = 0
        self.no = 0

    def converteToEndFis(self, endBin):
        self.offset = int(endBin[20:27],2)
        self.endBloco = int(endBin[10:20],2)
        self.no = int(endBin[2:9],2)
