from DataReview import DataReview
from Visualization import DataVisualization

def run():
	data_pokemon = DataReview("Pokemon.csv", sep=",")
	view = DataVisualization(data_pokemon.data)
	# print("Observaciones :", data_pokemon.num_features)
	# Ver los nombres de las columnas
	#print(data_pokemon.features_names)
	# Obtiene estadisticas
	#print(data_pokemon.view_statistics())
	#print(data_pokemon.view_statistics(include='categorical'))
	# Ver correlación
	# data_pokemon.view_correlation()
	# Ver resumen de nulos
	# print(data_pokemon.summary())

	# Ver distriución de clases
	# print(data_pokemon.view_class_distribution('legendary'))

	# Selección de características
	#features = ['hp','attack','defense','sp_atk','sp_def','speed','generation']
	#X = data_pokemon.selection_features(features)
	#y = data_pokemon.selection_features(['legendary'])
	#print(X)
	#print(y)

	# Ver outliers
	# view.view_outliers(x='legendary', y = 'attack')
	# Ver histograma por columna
	#view.view_histogram_by_column('sp_atk','Distrbución de velocidad de ataque')
	pycac:wqprint(view.count_by_column('type_1'))



if __name__ == '__main__':
	run()