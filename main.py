#!/usr/bin/python3.6
from codificadorLZW import Codificador
from decodificadorLZW import  Decodificador
from Arquivo import leArquivo
import sys

#Recebe o nome do arquivo também por parametro no CMD
nomeComExtensao = sys.argv[1]
option_redo = nomeComExtensao
#Separamos a extensão do arquivo de seu nome
nome,extensao = leArquivo.nomeExt(nomeComExtensao)
while(option_redo):
	#Recebe como parametro do CMD se é compressão ou descompressão
	if(sys.argv[2].lower() == 'c' || option_redo.lower() == 'c'):
		
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

	elif(sys.argv[2].lower() == 'd' || option_redo.lower() == 'c'):

		#Carrega as variáveis byte e path com o arquivo
		#byte,path = 
		leArquivo.leLzw(nome)#,str(len(Codificador.getCodigos())))
		decod = Decodificador()
		#decod.makeDecod()
	
	option_redo	= input("REFAZER - Escolha C ou D - \nENCERRAR - 0 \n ------> ")

