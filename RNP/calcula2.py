import pandas as pd
import os
import datetime
teste = pd.read_csv('/home/meruem/Documentos/TrabalhoDesempenho/rnp/teste5.csv', header=None );
teste2 = pd.read_csv('/home/meruem/Documentos/TrabalhoDesempenho/rnp/teste6.csv', header=None );
teste3 = pd.read_csv('/home/meruem/Documentos/TrabalhoDesempenho/rnp/teste7.csv', header=None );
teste4 = pd.read_csv('/home/meruem/Documentos/TrabalhoDesempenho/rnp/teste8.csv', header=None );


novo = teste2 - teste
media = float(novo.mean())
minimo = float(novo.min()) 
maximo = float(novo.max()) 

novo2 = teste4 - teste3
media2 = float(novo2.mean())
minimo2 = float(novo2.min()) 
maximo2 = float(novo2.max()) 


cont = open('/home/meruem/Documentos/TrabalhoDesempenho/rnp/cont2.txt', 'r')
num=cont.read()
cont.close()

cont = open('/home/meruem/Documentos/TrabalhoDesempenho/rnp/cont2.txt', 'w')
cont.write(str(int(num)+1))
cont.close()

cont = open('/home/meruem/Documentos/TrabalhoDesempenho/rnp/cont2.txt', 'r')
num=cont.read()
cont.close()

if int(num) == 1:
	date = datetime.datetime.today().strftime('%Y%m%d%H%M%S');	
	data = open('/home/meruem/Documentos/TrabalhoDesempenho/rnp/data2.txt', 'w')
	data.write(date)
	data.close()
	os.makedirs("/home/meruem/Documentos/TrabalhoDesempenho/rnp/ipv6/"+date)
else:
	if int(num) == 31:
		date = datetime.datetime.today().strftime('%Y%m%d%H%M%S');
		data = open('/home/meruem/Documentos/TrabalhoDesempenho/rnp/data2.txt', 'w')
		data.write(date)
		data.close()	
		os.makedirs("/home/meruem/Documentos/TrabalhoDesempenho/rnp/ipv6/"+date)
		cont = open('/home/meruem/Documentos/TrabalhoDesempenho/rnp/cont2.txt', 'w')
		cont.write(str(1))
		cont.close()
	else:
		date = open('/home/meruem/Documentos/TrabalhoDesempenho/rnp/data2.txt', 'r')
		date=date.read()

arq = open('/home/meruem/Documentos/TrabalhoDesempenho/rnp/ipv6/'+date+'/cont1.csv', 'a')
arq.write(str(media)+","+str(minimo)+","+str(maximo)+'\n')
arq.close()

arq = open('/home/meruem/Documentos/TrabalhoDesempenho/rnp/ipv6/'+date+'/cont2.csv', 'a')
arq.write(str(media)+","+str(minimo2)+","+str(maximo2)+'\n')
arq.close()

arq = open('/home/meruem/Documentos/TrabalhoDesempenho/rnp/ipv6/'+date+'/cont3.csv', 'a')
arq.write(str(media2+media)+'\n')
arq.close()
