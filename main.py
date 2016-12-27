#main
from node import *


Nodes = []
for i in range(256):
    Nodes.append(node())

print(Nodes[255].cache,Nodes[25].memory)
