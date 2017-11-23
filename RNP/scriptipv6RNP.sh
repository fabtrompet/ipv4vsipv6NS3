numeroroteadores=(28)
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
				python trabalhoipv6RNP.py --numeroclientes=$c --numroteadores=$a --intervalodepacotes=$d --tamanhodepacotes=$b 2> teste3.txt
				cat teste3.txt | grep "client sent" | cut -d' ' -f3 | tr "s" ' ' > /home/meruem/Documentos/TrabalhoDesempenho/rnp/teste5.csv
				cat teste3.txt | grep "server received" | cut -d' ' -f3 | tr "s" ' ' > /home/meruem/Documentos/TrabalhoDesempenho/rnp/teste6.csv 
				cat teste3.txt | grep "server sent" | cut -d' ' -f3 | tr "s" ' ' > /home/meruem/Documentos/TrabalhoDesempenho/rnp/teste7.csv
				cat teste3.txt | grep "client received" | cut -d' ' -f3 | tr "s" ' ' > /home/meruem/Documentos/TrabalhoDesempenho/rnp/teste8.csv 
				python /home/meruem/Documentos/TrabalhoDesempenho/rnp/calcula2.py
				done
			done
		done
	done
done







