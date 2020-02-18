import pathlib
from struct import pack
import struct

class leArquivo: 
    @staticmethod #Para utilizar sem instanciar
    def nomeExt(nome):
        return nome.split('.')

    @staticmethod
    def leEmBytes(nome):
        path = []
        for byte in pathlib.Path(nome).read_bytes(): 
            byte = chr(byte).encode('utf8') #CHAR em UTF8
            path.append(byte)
        return path

    @staticmethod
    def escreveLzw(outFile,codigos,vetor):
        with open(outFile + ".LZW", "wb") as file:
            file.write(struct.pack(codigos+'i', *vetor))

    @staticmethod
    def leLzw(outFile):
        with open(outFile + ".LZW", "rb") as file:
            content = file.read()
            print(content)
            # byte = struct.unpack(codigos+'i', content)
            # path.append(byte)
            # print(path)
            # return byte,path
        