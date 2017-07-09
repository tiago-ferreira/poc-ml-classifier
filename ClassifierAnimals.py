from ReadFile import readZoo
from PorcentagemConfig import PorcentagemConfig
from Dados import Dados
from sklearn.naive_bayes import MultinomialNB

class ClassifierAnimals(object):

  def fitAndPredict(self, model, data):
      model.fit(data.dadosTreino(), data.marcacoesTreino())
      result = model.predict(data.dadosTeste())
      return result

  def calculateAccuracy(self, result, data):
    acertos = (result == data)
    total_de_acertos = sum(acertos)
    total_de_elementos = len(data)
    taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos
    return taxa_de_acerto

if __name__ == '__main__':
  X, Y = readZoo()

  classifier = ClassifierAnimals()
  config = PorcentagemConfig(0.9,0.1)
  data = Dados(config, X, Y)

  result = classifier.fitAndPredict(MultinomialNB(), data)
  taxa_de_acerto = classifier.calculateAccuracy(result, data.marcacoesTeste())

  msg = "Taxa de acerto do {0}: {1}".format('Naive Bayes', taxa_de_acerto)
  print(msg)
