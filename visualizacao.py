import csv
import matplotlib.pyplot as plt
from os import listdir
from statistics import mean

arquivos = listdir('classificacao')
#print(arquivos)

for a in arquivos:
    data = csv.reader(open('classificacao/' + a, 'r'))

    afetivo = []
    cognitivo = []
    conotativo = []

    for rows in data:
        afetivo.append(float(rows[0]))
        cognitivo.append(float(rows[1]))
        conotativo.append(float(rows[2]))

    resultados = {'Afetivo': afetivo, 'Cognitivo' : cognitivo, 'Conotativo' : conotativo}

    #print(resultados.get('Afetivo'))
    #print(resultados.get('Cognitivo'))
    #print(resultados.get('Conotativo'))

    for c in resultados.keys():
        plt.plot(resultados.get(c),linestyle='',marker='.',linewidth=.1)
        #plt.plot([mean(resultados.get(c))] * len(resultados.get(c)), color='r',label='Média')
        plt.plot([mean(resultados.get(c))] * len(resultados.get(c)))
        plt.title(a +' - '+c)
        #plt.xlabel('Comentários')
        #plt.ylabel('Probabilidade')
        plt.legend()
        plt.savefig('graficos/'+a+'-'+c)
        plt.close()