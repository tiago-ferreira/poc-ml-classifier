class Dados(object):

  def __init__(self, porcentagem_config, X, Y):
    self.__porcentagem_config = porcentagem_config
    self.__X = X
    self.__Y = Y

  def dadosTreino(self):
    return self.__X[0:self.tamanhoTreino()]

  def marcacoesTreino(self):
    return self.__Y[0:self.tamanhoTreino()]

  def dadosTeste(self):
    return self.__X[self.tamanhoTreino():self.fimTeste()]

  def marcacoesTeste(self):
    return self.__Y[self.tamanhoTreino():self.fimTeste()]

  def dadosValidacao(self):
    return self.__X[self.fimTeste():]

  def marcacoesValidacao(self):
    return self.__Y[self.fimTeste():]

  def tamanhoTreino(self):
    return int(self.__porcentagem_config.treino * len(self.__Y))

  def tamanhoTeste(self):
    return int(self.__porcentagem_config.teste * len(self.__Y))

  def fimTeste(self):
    return int(self.tamanhoTreino() + self.tamanhoTeste())
