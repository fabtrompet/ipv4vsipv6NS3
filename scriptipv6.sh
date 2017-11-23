numeroroteadores=(5)
tamanhodopacote=(2000)
numerodeclientes=(10)
tempodeenvio=(0.09)
for a in "${numeroroteadores[@]}";
do
	for b in "${tamanhodopacote[@]}";
	do
		for c in "${numerodeclientes[@]}";
		do
			for d in "${tempodeenvio[@]}";
			do
				for i in `seq 30`
				do
				echo $a,$b,$c,$d
				python trabalhoipv6.py --numeroclientes=$c --numroteadores=$a --intervalodepacotes=$d --tamanhodepacotes=$b 2> teste.txt
				mv teste.txt backup1/
				cat backup1/teste.txt | grep "client sent" | cut -d' ' -f3 | tr "s" ' ' > /home/meruem/Documentos/TrabalhoDesempenho2/teste.csv
				cat backup1/teste.txt | grep "server received" | cut -d' ' -f3 | tr "s" ' ' > /home/meruem/Documentos/TrabalhoDesempenho2/teste2.csv 
				cat backup1/teste.txt | grep "server sent" | cut -d' ' -f3 | tr "s" ' ' > /home/meruem/Documentos/TrabalhoDesempenho2/teste3.csv
				cat backup1/teste.txt | grep "client received" | cut -d' ' -f3 | tr "s" ' ' > /home/meruem/Documentos/TrabalhoDesempenho2/teste4.csv 
				if [ "$c" == 10 ];then
					python /home/meruem/Documentos/TrabalhoDesempenho2/calculacom10.py
				else
					python /home/meruem/Documentos/TrabalhoDesempenho2/calcula.py
				fi
				done
			done
		done
	done
done