import pickle
import struct
import binascii

class Codificador:
    def __init__(self):
        self.k = 16
        self.dic_size = 2**self.k
        self.dic = {}
        self.codigos = []

    def makeCod(self, path):
        for i in range(self.dic_size):
            self.dic[chr(i).encode('utf-8')] = i
        aux = bytes('', encoding = "utf-8")
        for char in path:
            aux_c = b''.join([aux,char])
#            if(self.dic_size >= (pow(2,self.k))): 
#                
#                print("Tam Max |-----------| Ultrapassado")
#                return
#            else:
            if aux_c in self.dic:
                aux = aux_c
            else:
                self.codigos.append(self.dic[aux])
                self.dic[aux_c] = self.dic_size
                self.dic_size = self.dic_size + 1
                aux = char
        if aux:
            self.codigos.append(self.dic[aux])

    def getCodigos(self):
        return self.codigos

    def insereTamanho(self):
        self.codigos.insert(0, self.dic_size)