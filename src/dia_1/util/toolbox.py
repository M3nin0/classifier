import numpy as np
import pandas as pd


class Carry():
    '''
        Classe que prove facilidades
    '''
    

    @staticmethod
    def get_classificados():
        '''
            Método para carregar os dados com classificação
        
            :return: Dataset classificado
            :rtype: Pandas.DataFrame()
        '''
        
        temp = pd.read_csv('data/baseClassificada.txt', '\t', ';')
        
        temp.columns = ['pais', 'raca', 'porte', 'altura', 'peso']

        return temp

    
    @staticmethod
    def get_no_carry():
        '''
            Método para carregar os dados sem classificação de portes 

            :return: Dataset classificado
            :rtype: Pandas.DataFrame() 
        '''

        temp = pd.read_csv('data/baseSemPort.txt', '\t', ';')

        temp.columns = ['pais', 'raca', 'porte', 'altura', 'peso']

        return temp


    @staticmethod
    def gen_points():
        '''
            Método para gerar os pontos que serão utilizados na distância euclidiana
        
            :return: média da tabela de classificação
            :rtype: dict
        '''
    
        _infos = {'mini': [[1, 6.5], [17.8, 34]], 'pequeno': [[2.5, 16], [15, 47]],
                'medio': [[8, 35], [30, 58]], 'grande': [[18, 59], [50, 73]],
                'gigante': [[25, 100], [60, 90]]}
        
        _points = {'mini': [np.mean(_infos['mini'][0][0:]), np.mean(_infos['mini'][1][0:])],
            'pequeno': [np.mean(_infos['pequeno'][0][0:]), np.mean(_infos['pequeno'][1][0:])],
            'medio': [np.mean(_infos['medio'][0][0:]), np.mean(_infos['medio'][1][0:])],
            'grande': [np.mean(_infos['grande'][0][0:]), np.mean(_infos['grande'][1][0:])],
            'gigante': [np.mean(_infos['gigante'][0][0:]), np.mean(_infos['gigante'][1][0:])]}

        return _points


    @staticmethod
    def get_distance(points_unclassified, points_default):
        '''
            Método para devolver a distância euclidiana entre os pontos

            :param: points_unclassified (Pontos a serem comparados)
            :type: list

            :param: points_default (Pontos a serem usados como comparação)
            :type: dict

            :return: Dicionários com as distâncias
            :rtype: dict
        '''

        x_1 = points_unclassified[0]
        y_1 = points_unclassified[1]

        distances = {}

        # Encontra as distâncias
        for key in points_default:
            distances[key] = np.sqrt(
                np.power(points_default[key][0] - x_1, 2) + np.power(points_default[key] - y_1, 2))

        return distances


    @staticmethod
    def get_carry(points_unclassified, points_default):
        '''
            Método para tratar as distâncias e fazer classificação

            :param: points_unclassified (Pontos a serem comparados)
            :type: list

            :param: points_default (Pontos a serem usados como comparação)
            :type: dict

            :return: Porte do animal
            :rtype: str
        '''
        
        distances = Carry.get_distance(points_unclassified, points_default)
        
        means = {}
        for key in distances:
            means[key] = np.mean(distances[key][0:])
        
        return means
