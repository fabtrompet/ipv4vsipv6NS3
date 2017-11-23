import pandas as pd
import os
import datetime

teste = pd.read_csv('/home/meruem/Documentos/TrabalhoDesempenho2/teste.csv', header=None );
teste2 = pd.read_csv('/home/meruem/Documentos/TrabalhoDesempenho2/teste2.csv', header=None );
teste3 = pd.read_csv('/home/meruem/Documentos/TrabalhoDesempenho2/teste3.csv', header=None );
teste4 = pd.read_csv('/home/meruem/Documentos/TrabalhoDesempenho2/teste4.csv', header=None );
teste = teste.apply(lambda x: x - 20)
teste2 = teste2.apply(lambda x: x - 20)
teste3 = teste3.apply(lambda x: x - 20)
teste4 = teste4.apply(lambda x: x - 20)

novo = teste2 - teste
media = float(novo.mean())
minimo = float(novo.min()) 
maximo = float(novo.max()) 
desvio = float(novo.std())

novo2 = teste4 - teste3
media2 = float(novo2.mean())
minimo2 = float(novo2.min()) 
maximo2 = float(novo2.max()) 
desvio2 = float(novo2.std())

cont = open('/home/meruem/Documentos/TrabalhoDesempenho2/cont.txt', 'r')
num=cont.read()
cont.close()

cont = open('/home/meruem/Documentos/TrabalhoDesempenho2/cont.txt', 'w')
cont.write(str(int(num)+1))
cont.close()

cont = open('/home/meruem/Documentos/TrabalhoDesempenho2/cont.txt', 'r')
num=cont.read()
cont.close()

if int(num) == 1:
	date = datetime.datetime.today().strftime('%Y%m%d%H%M%S');	
	data = open('/home/meruem/Documentos/TrabalhoDesempenho2/data.txt', 'w')
	data.write(date)
	data.close()
	os.makedirs("/home/meruem/Documentos/TrabalhoDesempenho2/"+date)
else:
	if int(num) == 31:
		date = datetime.datetime.today().strftime('%Y%m%d%H%M%S');
		data = open('/home/meruem/Documentos/TrabalhoDesempenho2/data.txt', 'w')
		data.write(date)
		data.close()	
		os.makedirs("/home/meruem/Documentos/TrabalhoDesempenho2/"+date)
		cont = open('/home/meruem/Documentos/TrabalhoDesempenho2/cont.txt', 'w')
		cont.write(str(1))
		cont.close()
	else:
		date = open('/home/meruem/Documentos/TrabalhoDesempenho2/data.txt', 'r')
		date=date.read()

arq = open('/home/meruem/Documentos/TrabalhoDesempenho2/'+date+'/cont1.csv', 'a')
arq.write(str(media)+","+str(minimo)+","+str(maximo)+'\n')
arq.close()

arq = open('/home/meruem/Documentos/TrabalhoDesempenho2/'+date+'/cont2.csv', 'a')
arq.write(str(media)+","+str(minimo2)+","+str(maximo2)+'\n')
arq.close()

arq = open('/home/meruem/Documentos/TrabalhoDesempenho2/'+date+'/cont3.csv', 'a')
arq.write(str(media2+media)+'\n')
arq.close()
