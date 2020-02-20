# -*- coding: utf-8 -*-
from codificadorLZW import Codificador
from decodificadorLZW import  Decodificador
from Arquivo import Arquivo


#Recebe o nome do arquivo também por parametro no CMD
#nomeComExtensao = 'corpus16MB.txt'
#nomeComExtensao = 'lorem.txt'
nomeComExtensao = 'mapa.mp4'


#Separamos a extensão do arquivo de seu nome
nome,extensao = Arquivo.nomeExt(nomeComExtensao)

#Recebe como parametro do CMD se é compressão ou descompressão
		
#Transforma em bytes o que foi lido do arquivo
byte = Arquivo.leEmBytes(nomeComExtensao)
leu = byte
#Instanciação do objeto cod
cod = Codificador()
#Executa o LZW
cod.makeCod(byte)

var = cod.dic
rav = cod.codigos

#Insere o tamanho
cod.insereTamanho()
#Escreve o .LZW
Arquivo.escreveLzw(nome,str(len(cod.getCodigos())),cod.getCodigos())

###########################DECODIFICADOR
x = []
#Carrega as variáveis byte e path com o arquivo
byte,path = Arquivo.leLzw(nome,str(len(cod.getCodigos())))
decod = Decodificador()
#Separa os itens
for i in path:
	x.extend(i)
#Faz a decodificação
decod.makeDecod(x, x[0])


Arquivo.escreveTxt(nome,extensao,decod.getCodigos())
	

