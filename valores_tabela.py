import csv
from os import listdir
from statistics import mean,stdev

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

    print('%s,%.4f +/- %.4f,%.4f +/- %.4f,%.4f +/- %.4f' % (a,mean(afetivo),stdev(afetivo),mean(cognitivo),stdev(cognitivo),mean(conotativo),stdev(conotativo)))