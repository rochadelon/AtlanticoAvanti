# -*- coding: utf-8 -*-
import logging
import pickle
from pathlib import Path


def main(input_filepath, model_filepath):
    """
    Treina modelo usando dados processados
    
    Parameters:
    ----------
    input_filepath : str
        Caminho para os dados processados
    model_filepath : str
        Caminho para salvar o modelo treinado
    """
    logger = logging.getLogger(__name__)
    logger.info('Iniciando treinamento do modelo')

    # Implemente a lógica de treinamento aqui
    # Exemplo:
    # df = pd.read_csv(input_filepath)
    # X = df.drop('target', axis=1)
    # y = df['target']
    # modelo = RandomForestClassifier()
    # modelo.fit(X, y)
    # 
    # with open(model_filepath, 'wb') as f:
    #     pickle.dump(modelo, f)

    logger.info('Modelo treinado e salvo')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main('data/processed/dataset.csv', 'models/model.pkl')
