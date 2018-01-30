# Aula 1

Introdução a mineração de dados

## Conceitos importantes

Abaixo alguns dos conceitos básicos e bastante relevantes para o processamento de dados.

- Classificação
	- Aprendizado de uma função que pode ser usada para mapear dados em uma de várias classes discretas definidas previamente;
	- Classificar, dividir em grupos (Buscar as partes discretas).
	
- Agrupamento (ou clustering)
	- Identificação de grupos de dados onde os dados tem aracterísticas semelhantes aos do mesmo grupo.
	
- Detecção de desvios (Outliers)
	- Identificação de dados que deveriam seguir um padrão esperado mas não o fazem.

- Identificação de associações


## Conceitos matemáticos

- Distância euclidiana

## Classificação

É a predição de uma categoria ou classe discreta.

O que é necessário para realizar a classificação ?
- Instâncias para as quais a classe é conhecida.

OBS: Preste a atenção nos atributos.

Algoritimos para calcular e realizar a classificação 

- Supervisionadas
	- Distância euclidiana;
		- Existem várias formas de implementar
			- Implementação linear.
		- Vantagem
			- Simples.
		- Desvantagem
			- Aceita apenas atributos numéricos.

	- Hiperparalelepipedo regular
		- Usa os extremos da classe
		- Permite rejeição (Verifica se o dado pertence ou não a um grupo)
		- Facil implementação
		- Pode trabalhar com atributos titulares;
		- Pode ter impate
			- Há classes duplas em uma mesma informação

	- Árvore de decisão
		- Facil interpretação
		- Utilizado para sistemas especialistas
			- Sistema especialista para entregar dados médicos
		- Não há impate

	- Rede neural artificial
		- Matematicamente complicada

Existem vários outros e de várias formas diferentes.
