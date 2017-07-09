class PorcentagemConfig(object):

  def __init__(self, treino, teste):
    self.__treino = treino
    self.__teste = teste

  @property
  def treino(self):
    return self.__treino

  @property
  def teste(self):
    return self.__teste