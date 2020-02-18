#!/usr/bin/python3.6
from codificadorLZW import Codificador
from decodificadorLZW import  Decodificador
from Arquivo import leArquivo
import sys

#Recebe o nome do arquivo também por parametro no CMD
nomeComExtensao = sys.argv[1]
opcao = sys.argv[2].lower()


#Separamos a extensão do arquivo de seu nome
nome,extensao = leArquivo.nomeExt(nomeComExtensao)
while(opcao):
	#Recebe como parametro do CMD se é compressão ou descompressão
	if(opcao.lower() == 'c' ):
		
		#Transforma em bytes o que foi lido do arquivo
		byte = leArquivo.leEmBytes(nomeComExtensao)
		#Instanciação do objeto cod
		cod = Codificador()
		#Executa o LZW
		cod.makeCod(byte)
		#Insere o tamanho
		cod.insereTamanho()
		#Escreve o .LZW
		leArquivo.escreveLzw(nome,str(len(cod.getCodigos())),cod.getCodigos())

		print(str(len(cod.getCodigos())))

	elif(opcao.lower() == 'd'):
		x = []
		#Carrega as variáveis byte e path com o arquivo
		byte,path = leArquivo.leLzw(nome,str(len(cod.getCodigos())))
		decod = Decodificador()
		#Separa os itens
		for i in path:
			x.extend(i)
		#Faz a decodificação
		print(x)
		decod.makeDecod(x, x[0])


		leArquivo.escreveTxt(nome,extensao,decod.getCodigos())
	
	opcao = input("REFAZER - Escolha C ou D - \nENCERRAR - Ctrl+c \n ------> ")

