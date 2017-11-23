
# coding: utf-8

# In[1]:

from glob import glob
import pandas as pd
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


# In[2]:

arquivos = glob("ipv4/*/")
arquivos2 = glob("ipv6/*/")


# In[3]:

arquivos.sort()
arquivos2.sort()


# In[4]:

arquivos


# In[4]:

def calc(df):
    mean = df[0].mean()
    std = df[0].std()
    margemdeerro = 1.96 * (std / np.sqrt(len(df[0]))) 
    return mean, margemdeerro


# In[ ]:


    


# In[22]:

def gera_graficos(n1,n2,n3):
    cont=1
    for caminho in arquivos:
        arquivos3 = glob(caminho+"*/"+"*")
        arquivos4 = glob(arquivos2[0]+"*/"+"*")
        arquivos3.sort()
        arquivos4.sort()
        lista = []
        lista.append(pd.read_csv(arquivos3[n1], header=None))
        lista.append(pd.read_csv(arquivos4[n1], header=None))
        lista.append(pd.read_csv(arquivos3[n2], header=None))
        lista.append(pd.read_csv(arquivos4[n2], header=None))
        lista.append(pd.read_csv(arquivos3[n3], header=None))
        lista.append(pd.read_csv(arquivos4[n3], header=None))

        lista2 = []
        for i in lista:
            lista2.append(calc(i))
        #x = np.arange(6)
        x = [0,11,21]
        cliente = caminho.split("/")[1].split("-")[0]
        roteador = caminho.split("/")[1].split("-")[1]
        intervalo = float(caminho.split("/")[1].split("-")[2])/100
        labels=['1000 Bytes','1500 Bytes', '2000 Bytes']
        plt.errorbar(0,lista2[0][0], yerr=lista2[1][1], linestyle='', capsize=6,elinewidth="1", marker='o',fmt='o', label="IPv4", color='k' )
        plt.errorbar(0.9,lista2[1][0], yerr=lista2[1][1], linestyle='',capsize=6,elinewidth="1",marker='o', fmt='o', label="IPv6", color='r')
        plt.errorbar(11,lista2[2][0], yerr=lista2[2][1], linestyle='',capsize=6,elinewidth="1",marker='o', fmt='o',color='k')
        plt.errorbar(11.9,lista2[3][0], yerr=lista2[3][1], linestyle='',capsize=6,elinewidth="1",marker='o', fmt='o',color='r')
        plt.errorbar(21,lista2[4][0], yerr=lista2[4][1], linestyle='',capsize=6,elinewidth="1",marker='o', fmt='o',color='k')
        plt.errorbar(21.9,lista2[5][0], yerr=lista2[5][1], linestyle='',capsize=6,elinewidth="1",marker='o', fmt='o',color='r')
        plt.xticks(x,labels)
        plt.legend()

        #plt.plot(x, lista, marker="o")
        #plt.plot(x, teste2[0])
        if roteador == "05":
    #        print ('oi')
            if n1 == 0:
                plt.title("Gráfico "+str(cont)+" - Ida de pacotes UDP\n com "+cliente+" cliente(s) e intervalo de "+str(intervalo)+"s")
                plt.savefig("Graficos Ida/Gráfico "+str(cont)+" - Envio de pacotes UDP com "+cliente+" cliente(s) e intervalo de "+str(intervalo)+"s.png")
            elif n1 == 1:
                plt.title("Gráfico "+str(cont)+" - Volta de pacotes UDP\n com "+cliente+" cliente(s) e intervalo de "+str(intervalo)+"s")
                plt.savefig("Graficos Volta/Gráfico "+str(cont)+" - Envio de pacotes UDP com "+cliente+" cliente(s) e intervalo de "+str(intervalo)+"s.png")
            elif n1 == 2:
                plt.title("Gráfico "+str(cont)+" - Ida e Volta de pacotes UDP\n com "+cliente+" cliente(s) e intervalo de "+str(intervalo)+"s") 
                plt.savefig("Graficos IdaeVolta/Gráfico "+str(cont)+" - Envio de pacotes UDP com "+cliente+" cliente(s) e intervalo de "+str(intervalo)+"s.png")
            cont+=1
        plt.show()
        


# In[23]:

gera_graficos(0,3,6)


# In[25]:

gera_graficos(1,4,7)


# In[24]:

gera_graficos(2,5,8)


# In[ ]:




# In[ ]:




# In[ ]:



