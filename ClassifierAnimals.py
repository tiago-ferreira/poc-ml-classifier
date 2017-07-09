from ReadFile import readZoo
from PorcentagemConfig import PorcentagemConfig
from Dados import Dados
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn import neighbors
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC

class ClassifierAnimals(object):

  def fitAndPredict(self, model, data):
      model.fit(data.dadosTreino(), data.marcacoesTreino())
      result = model.predict(data.dadosTeste())
      return result

  def calculateAccuracy(self, result, data, classifier_name):
    acertos = (result == data)
    taxa_de_acerto = 100.0 * sum(acertos) / len(data)
    print "Taxa de acerto do {0}: {1}".format(classifier_name, taxa_de_acerto)


if __name__ == '__main__':

  X, Y = readZoo()

  classifier = ClassifierAnimals()
  config = PorcentagemConfig(0.9,0.1)
  data = Dados(config, X, Y)

  result = classifier.fitAndPredict(MultinomialNB(), data)
  classifier.calculateAccuracy(result, data.marcacoesTeste(), 'Naive Bayes')
  result = classifier.fitAndPredict(AdaBoostClassifier(), data)
  classifier.calculateAccuracy(result, data.marcacoesTeste(), 'AdaBoostClassifier')
  result = classifier.fitAndPredict(neighbors.KNeighborsClassifier(), data)
  classifier.calculateAccuracy(result, data.marcacoesTeste(), 'KNeighborsClassifier')
  result = classifier.fitAndPredict(OneVsRestClassifier(LinearSVC(random_state = 0)), data)
  classifier.calculateAccuracy(result, data.marcacoesTeste(), 'OneVsRestClassifier')