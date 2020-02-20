class Decodificador():
    def __init__(self):
        self.k = 8
        self.dic_size = 2**self.k
        self.dic = {}
        self.codigos = []

    def makeDecod(self, path, dic_tam):
        for i in range(self.dic_size):
            self.dic[i] = chr(i).encode('utf-8', errors='surrogatepass')
        del path[0]
        aux = chr(path.pop(0)).encode("utf-8", errors='surrogatepass')
        self.codigos.append(aux)
        for key in path:
            if(self.dic_size == dic_tam):
                print("tamanho maximo ultrapassado")
                return
            else:
                if key in self.dic:
                    aux_c = self.dic[key]
                elif key == self.dic_size:
                    aux_c = b''.join([aux,chr(aux[0]).encode("utf-8", errors='surrogatepass')])     
                else:
                    print("Deu errado o valor ", key)
                self.codigos.append(aux_c)
            
            self.dic[self.dic_size] = b''.join([aux,chr(aux_c[0]).encode("utf-8", errors='surrogatepass')])
            self.dic_size = self.dic_size + 1
            aux = aux_c

    def getCodigos(self):
        return self.codigos
