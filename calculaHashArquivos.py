#importa as lib necessarias para execução do codigo
import os
import hashlib
from datetime import datetime

#PRIMEIRA ETAPA - REALIZA O CALCULO DE HASH DOS ARQUIVOS EXISTENTES NO DIRETORIO INFORMADO
#diretorio informado pelo usuário
diretorio = input('Informe o caminho referente ao diretorio onde estão os arquivos: \n') #'C:/Users/c015945/Desktop/Pentest/arquivos/novavalidacao/novosarquivos'
#pega informação dos arquivos existentes no diretorio
arquivos = os.listdir(diretorio)

#cria arquivo onde será gravado os resultados hash
criatxt = open(diretorio + '/resultadohash.txt', 'w')	
criatxt.write('RESULTADO DOS CALCULOS DE HASH REALIZADO NO DIRETORIO INFORMADO \n')
criatxt.write('REGISTRADO EM: ' + str(datetime.now()) + '\n')
criatxt.write('\n')
criatxt.close()

#realiza laço nos arquivos existentes no diretorio
for a in arquivos:

	#retira os dois novos arquivos criados de dentro do calculo de hash
	if(a == 'resultadohash.txt' or a == 'hash.txt'):
		continue

	#cria apontamento completo do arquivo
	caminho = os.path.join(diretorio,a)

	#verifica a existencia do arquivo
	if(os.path.isfile(caminho)):
		#calcula o tamanho do arquivo em kb
		tamanho = os.path.getsize(caminho)/1024		

	#abre cada arquivo em modo binario para realizar o calculo do hash
	with open(caminho, 'rb', buffering=0) as arquivo:
		#faz a leitura do conteudo
		saida = arquivo.read()
		#calcula em md5
		resultadohashmd5 = hashlib.md5(saida).hexdigest()
		#calcula em sha256
		resultadohashsha = hashlib.sha256(saida).hexdigest()		
	
	#gera as saidas
	gravaresltado = open(diretorio + '/resultadohash.txt', 'a')	
	gravaresltado.write(caminho + '\n')
	gravaresltado.write('Caminho do arquivo: ' + str(diretorio) + '\n')
	gravaresltado.write('Nome do arquivo: ' + str(a) + '\n')	
	gravaresltado.write('Tamanho: ' + str(tamanho) + 'KB \n')
	gravaresltado.write('Hash MD5: ' + str(resultadohashmd5) + '\n')
	gravaresltado.write('Hash SHA256: ' + str(resultadohashsha) + '\n')
	gravaresltado.write('\n')
	gravaresltado.close()
		
#SEGUNDA ETAPA - REALIZAÇÃO DO CALCULO DO HASH EM CIMA DO ARQUIVO CRIADO (RESULTADOSHASH.TXT)
#cria arquivo onde será gravado o hash do arquivo resultadohash.txt
criaconfirmhash = open(diretorio + '/hash.txt', 'w')
criaconfirmhash.close()

#abre o arquivo resultadohash.txt em modo binario para realizar o calculo do hash
with open(diretorio + '/resultadohash.txt', 'rb', buffering=0) as arquivo:
	#faz a leitura do conteudo
	saida = arquivo.read()
	#calcula em md5
	resultadohashmd5 = hashlib.md5(saida).hexdigest()
	#calcula em sha256
	resultadohashsha = hashlib.sha256(saida).hexdigest()

#gera saida da validação
gravaresltado = open(diretorio + '/hash.txt', 'a')	
gravaresltado.write('HASH DE VALIDAÇÃO DO ARQUIVO: resultadohash.txt \n')
gravaresltado.write('REGISTRADO EM: ' + str(datetime.now()) + '\n')
gravaresltado.write('\n')
gravaresltado.write('Hash MD5: ' + str(resultadohashmd5) + '\n')
gravaresltado.write('Hash SHA256: ' + str(resultadohashsha) + '\n')
gravaresltado.close()

print('Script finalizado com sucesso!')