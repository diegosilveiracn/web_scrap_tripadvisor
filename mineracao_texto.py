import re
from os import listdir
import nltk
from nltk.tokenize import word_tokenize

class Base:
    def __init__(self):
        self.base_treinamento = []
        self.base_teste = []
        self.stopwordsnltk = nltk.corpus.stopwords.words('portuguese')
        self.atributos = []

    def importar_base_treinamento(self,nome_base):
        path = 'base/treinamento/' + nome_base
        file = open(path, 'r')
        texto = file.readlines()
        file.close()
        for linha in texto:
            self.base_treinamento.append((linha,nome_base))

    def importar_base_teste(self,nome_base):
        path = 'base/teste/' + nome_base
        file = open(path, 'r')
        texto = file.readlines()
        file.close()
        for linha in texto:
            self.base_teste.append(linha)

    def aplicar_stemming_treinamento(self):
        stemmer = nltk.stem.RSLPStemmer()
        comentario_stemming = []
        for (comentario, classe) in self.base_treinamento:
            tokens = word_tokenize(re.sub(r'[\n.()!\\\',;:\-\\"]','',comentario.lower()))
            comstemming = [str(stemmer.stem(p)) for p in tokens if p not in self.stopwordsnltk]
            comentario_stemming.append((comstemming, classe))
        return comentario_stemming

    def aplicar_stemming_teste(self,comentario):
        testestemming = []
        stemmer = nltk.stem.RSLPStemmer()
        tokens = word_tokenize(re.sub(r'[\n.()!\\\',;:\-\\"]','',comentario.lower()))
        for token in tokens:
            comstem = [p for p in token.split()]
            testestemming.append(str(stemmer.stem(comstem[0])))
        return testestemming

    def listar_atributos(self,base_stemming):
        todaspalavras = []
        for (comentario, classe) in base_stemming:
            todaspalavras.extend(comentario)
        lista_atributos = nltk.FreqDist(todaspalavras).keys()
        self.atributos = lista_atributos

    def construir_amostragem(self,comentario_stemming):
        texto = set(comentario_stemming)
        amostragem = {}
        for valores in self.atributos:
            amostragem['%s' % valores] = (valores in texto)
        return amostragem

base = Base()
base.importar_base_treinamento('afetivo')
#print(len(base.base_treinamento))
base.importar_base_treinamento('cognitivo')
#print(len(base.base_treinamento))
base.importar_base_treinamento('conotativo')
#print(len(base.base_treinamento))

base_treinamento_stemming = base.aplicar_stemming_treinamento()
base.listar_atributos(base_treinamento_stemming)

base_treinamento_completa = nltk.classify.apply_features(base.construir_amostragem, base_treinamento_stemming)
classificador = nltk.NaiveBayesClassifier.train(base_treinamento_completa)

# Testando para todas as bases

diretorios = listdir('base/teste')
for d in diretorios:
    print('Diretório:'+d)
    base.base_teste = []
    arquivos = listdir('base/teste/' + d)
    #print(arquivos)
    for a in arquivos:
        base.importar_base_teste(d+'/'+a)

    #print(len(base.base_teste))

    file = open('probabilidades/'+d,'w')

    print('----------------------------------')
    for comentario_teste in base.base_teste:
        base_teste_stemming = base.aplicar_stemming_teste(comentario_teste)
        #print(base_teste_stemming)

        novo = base.construir_amostragem(base_teste_stemming)
        #print(novo)

        distribuicao = classificador.prob_classify(novo)
        resultados = '%.4f,%.4f,%.4f\n' % (distribuicao.prob('afetivo'),distribuicao.prob('cognitivo'),distribuicao.prob('conotativo'))
        file.write(resultados)

        #if distribuicao.prob('afetivo') >= 0.8:
        #    print(comentario_teste)

    file.close()

print('Finalizado!')