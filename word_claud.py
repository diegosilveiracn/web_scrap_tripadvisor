#-*- conding: utf8 -*-
import re
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from os import listdir


text = ''


#diretorios = listdir('base/teste')
#['praças e parques', 'compras', 'edificacoes e monumentos historicos', 'praias e lagoas']
diretorios = ['praias e lagoas']

for d in diretorios:
    arquivos = listdir('base/teste/'+d)
    for a in arquivos:
        file = open('base/teste/'+d+'/'+a,'r')
        text += file.read()
        file.close()

#split a document to words
text_1 = re.split(r'[\n.()!\\\';\-, ""/]', text.lower())

# delete some empty string
text_2 = [x for x in text_1 if len(x) > 0]

# get word frequency and delete some stopwords
wg = text_2
wd = {}

stopwords = [u'a', u'as', u'à', u'às',u'o', u'ó', u'os', u'ao', u'aos', u'ai', u'aí',u'ou',u'é',
             u'um', u'uns', u'uma', u'umas',
             u'de', u'do', u'da', u'dos', u'das',
             u'algum', u'alguns', u'alguma', u'algumas',u'quem', u'que', u'qual', u'quais',
             u'com', u'como', u'em', u'na', u'nas', u'no', u'nos',
             u'esse', u'esses', u'essa', u'essas', u'aquele', u'aqueles', u'aquela', u'aquelas', u'aquilo',
             u'onde', u'aonde',
             u'eu', u'tu', u'ele', u'ela', u'nós', u'vós', u'eles', u'elas',
             u'mim', u'ti', u'dele', u'dela', u'deles', u'delas', u'meu', u'teu', u'tua',u'tuas', u'te',
             u'seu',u'seus',u'sua',u'suas',u'si',
             u'sim', u'não', u'nada', u'nenhum', u'nehuma', u'nehuns', u'nenhumas', u'ninguem',u'além',u'porém',
             u'nem', u'quem',
             u'e', u'é', u'és', u'são', u'esta', u'este', u'estas',u'estes',u'está',u'estás',
             u'se',u'senão',u'então',
             u'por',u'para',u'pelo',u'pela',u'pelos',u'pelas',
             u'pra',u'porque',u'porquê',
             u'todo',u'toda',u'todos',u'todas',u'cada',
             u'mesmo',u'mesma',u'mesmos',u'mesmas',
             u'ali',u'aqui',u'agora',u'além',u'já',u'através',u'antes',u'depois',u'até', u'fora',
             u'mas',u'mais', u'num', u'numa',
             u'só',u'ser',u'mas',u'foi',u'fica',u'também',u'pois',u'estava',
             u'fazer',u'fui',u'muita',u'pelo',u'quando',u'possui',u'frente',
             u'lado',u'estava',u'parte',u'lá',u'fomos',u'muito',
             u'vai',u'há',u'sem',u'dá',u'nao',u'baixa',u'me',u'ainda',
             u'ir',u'levar',u'cheia',u'achei',u'nessa',u'pelas',u'principalmente',
             u'nte',u'várias',u'você',u'dá',u'minha',u'vai',u'dentro',u'isso',
             u'sobre',u'apesar',u'sem',u'tem',u'faz',u'tirar',u'ficar',
             u'vc',u'entre',u'ter',u'tanto',u'la',u'assim',u'vezes',u'quer',u'pode',
             u'maior',u'tão',u'for']

for w in wg:
    if w in stopwords:
        continue
    else:
        str(w)
        if w not in wd:
            wd[w] = 1
        else:
            wd[w] += 1

# get the wordcloud
wordcloud = WordCloud(width=1600, height=800).generate_from_frequencies(wd)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()