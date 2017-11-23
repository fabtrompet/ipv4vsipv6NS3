numeroroteadores=(16)
tamanhodopacote=(1000 1500 2000)
numerodeclientes=(1 10)
tempodeenvio=(0.09 0.18)
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
				python trabalhoipv4manhattan.py --numeroclientes=$c --numroteadores=$a --intervalodepacotes=$d --tamanhodepacotes=$b 2> teste1.txt
				cat teste1.txt | grep "client sent" | cut -d' ' -f3 | tr "s" ' ' > /home/meruem/Documentos/TrabalhoDesempenho/manhattan/teste.csv
				cat teste1.txt | grep "server received" | cut -d' ' -f3 | tr "s" ' ' > /home/meruem/Documentos/TrabalhoDesempenho/manhattan/teste2.csv 
				cat teste1.txt | grep "server sent" | cut -d' ' -f3 | tr "s" ' ' > /home/meruem/Documentos/TrabalhoDesempenho/manhattan/teste3.csv
				cat teste1.txt | grep "client received" | cut -d' ' -f3 | tr "s" ' ' > /home/meruem/Documentos/TrabalhoDesempenho/manhattan/teste4.csv 
				python /home/meruem/Documentos/TrabalhoDesempenho/manhattan/calcula.py
				done
			done
		done
	done
done







