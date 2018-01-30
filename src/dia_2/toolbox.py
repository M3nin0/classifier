class Fuzzy():
	'''
        Classe que prove facilidades
    '''

	@staticmethod
	def fuzzy(reference_point, tested_point):
		'''
			Método para aplicação do método fuzzy

			:param: reference_point (Ponto de referência)
			:type: list

			:param: tested_point (Pontos que serão testados)
			:type: list

			:return Classificação do ponto testado 
		'''

		x1 = tested_point[0]
		y1 = tested_point[1]

		x2 = reference_point[0]
		y2 = reference_point[1]


	@staticmethod
	def angular(x1, x2, y1, y2):
		'''
			Método para calcular o coeficiente angular

			:param: x1
			:type: double

			:param x2
			:type: double

			:param y1
			:type: double

			:param: y2
			:type: double
		'''

		# m = (y2 - y1 ) + (x2 - x1)
		return (y2 - y1) / (x2 - x1)


	@staticmethod
	def linear(x1, x2, y1, y2):
		'''
			Método para encontrar o coeficiente linear

			:param: x1
			:type: double

			:param x2
			:type: double

			:param y1
			:type: double

			:param: y2
			:type: double
		'''

		m = Fuzzy.angular(x1, x2, y1, y2)

		# y1 - m * x1
		return m, y1 - (m * x1)


	@staticmethod
	def percent(x1, x2, y1, y2, altura):
		'''
			Método para devolver a probabilidade de alturas
		'''

		m, linear = Fuzzy.linear(x1, x2, y1, y2)

		return (m * altura) + linear
