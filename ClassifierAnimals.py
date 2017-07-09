from ReadFile import readZoo
from PorcentagemConfig import PorcentagemConfig
from Dados import Dados
from sklearn.naive_bayes import MultinomialNB
import numpy as np


if __name__ == '__main__':
  X, Y = readZoo()

  config = PorcentagemConfig(0.9,0.1)
  data = Dados(config, X, Y)

  modelo = MultinomialNB()
  modelo.fit(data.dadosTreino(), data.marcacoesTreino().ravel())
  resultado = modelo.predict(data.dadosTeste())
  acertos = (resultado == data.marcacoesTeste().ravel())

  total_de_acertos = np.sum(acertos)

  total_de_elementos = len(data.marcacoesTeste())

  taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

  msg = "Taxa de acerto do {0}: {1}".format('Naive Bayes', taxa_de_acerto)
  print(msg)
