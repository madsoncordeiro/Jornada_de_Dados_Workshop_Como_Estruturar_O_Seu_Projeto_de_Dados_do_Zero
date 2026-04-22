import glob  # Biblioteca para listar arquivos
import os  # Biblioteca para manipular arquivos e pastas
from typing import List  # Biblioteca para tipagem de listas

import pandas as pd  # Biblioteca para manipulação de dados

path = 'data/input'


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    Função para ler os arquivos de uma pasta data/input e retornar uma lista de DataFrames

    args: input_path (str): caminho da pasta com os arquivos

    return: lista de DataFrames
    """

    all_files = glob.glob(os.path.join(path, '*.xlsx'))

    data_frame_list = []

    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list


# Criando uma variável que vai comportar todas essas listas, está chamando a função criada e passando o path
if __name__ == '__main__':
    data_frame_list = extract_from_excel(path)
    print(data_frame_list)
