import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib import cm
from matplotlib import colors

class DataReview(object):

  def __init__(self, source, sep=";"):
    self.data = pd.read_csv(source, sep=sep, index_col = 0)
    self.num_observation = self.data.shape[0]
    self.num_features = self.data.shape[1]
    self.data.columns = self.data.columns.str.lower().str.replace("_", " ", regex=True)
    self.data.columns = self.data.columns.str.lower().str.replace(".", "", regex=True)
    self.data.columns = self.data.columns.str.lower().str.replace(" ", "_", regex=True)
    
    self.features_names = self.data.columns     

  def __getattr__(self, name: str):
    return object.__getattribute__(name)

  def __setattr__(self, name: str, value):
    self.__dict__[name] = value  

  def view_statistics(self, include=None):
    """ Return DataFrame con el resumen de las medidas estadísticas básicas
    include -> str que indica que tipo de columnas a incluir
      'categorical' -> indica que se desea obtener las medidas de las variables categóricas
    """
    if include == None:
      return self.data.describe()
    if include.lower() == 'categorical':
      return self.data.describe(include = np.object0)

  def view_class_distribution(self, column):
    """ Return DataFrame con las ocurrencias de los valores de la columna
    """
    return self.data[column].value_counts()

  def selection_features(self, columns):
    """ Return DataFrame con la columnas seleccionadas 
    """
    return self.data[columns]

  def summary(self):
    """ Return DataFrame con el resumen de las columnas indicando tipo, nombre, indicador 
    para saber si tiene nulos y la cantidad de nulos
    """
    d_tipos, d_nulos, d_count = pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    d_tipos['name'] = pd.DataFrame(self.data.dtypes).index
    d_tipos['type'] = pd.DataFrame(self.data.dtypes)[0].values

    d_nulos['name'] = pd.DataFrame(self.data.isnull().any()).index
    d_nulos['isNull'] = pd.DataFrame(self.data.isnull().any())[0].values

    d_count['name'] = pd.DataFrame(self.data.isnull().sum()).index
    d_count['count.null'] = pd.DataFrame(self.data.isnull().sum())[0].values

    return pd.merge(pd.merge(d_tipos, d_nulos, on = 'name'), d_count, on="name")    