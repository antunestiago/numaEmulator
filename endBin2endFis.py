import binascii

class EndFisico():

    def __init__(self):
        self.offset = 0
        self.endBloco = 0
        self.no = 0

    def converteToEndFis(self, endBin):
        self.offset = int(endBin[29:34],2)
        self.endBloco = int(endBin[11:28],2)
        self.no = int(endBin[2:10],2)
        
