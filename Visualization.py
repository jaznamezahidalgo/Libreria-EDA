import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualization(object):
	def __init__(self, data_frame) :
		self.data_frame = data_frame

	def view_histogram_by_column(self, column, title):
		try:
			sns.set(style='whitegrid')
			f, ax = plt.subplots(1,1, figsize=(6,4))
			ax = sns.histplot(self.data_frame[column], kde = True, color = 'c')
			plt.title(title, fontsize = 18, fontweight="bold")
			plt.xlabel(column.capitalize(), fontsize=14)
			plt.ylabel("Densidad", fontsize=14)
			plt.show();
		except KeyError:
			print("Problema para visualizar gráfico")

	def count_by_column(self, column):
		return self.data_frame.groupby(column).size()

	def view_distribution(self, hue, features):
		""" Return None
		Permite mostrar unos histogramas para ver la distribución de la categoría (hue) respecto de las variables indicadas en features
		"""
		sns.pairplot(self.data_frame, hue=hue, height=4, vars=features, kind='scatter');

	def view_correlation(self):
		plt.figure(figsize=(10, 10))
		sns.heatmap(self.data_frame.corr(), annot=True, cmap='Blues_r')
		plt.title("Correlación de características", fontsize=18, fontweight="bold")
		plt.show()   

	def view_outliers(self, x, y):
  		plt.figure(figsize=(5,5))
  		sns.boxplot(x=x.lower(), y = y.lower(), data=self.data_frame)
  		plt.title("Outliers {}".format(y.capitalize()), fontsize=18, fontweight="bold")
  		plt.xlabel(x.capitalize(), fontsize=14)
  		plt.ylabel(y.capitalize(), fontsize=14)
  		plt.show()