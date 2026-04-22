import pandas as pd
from typing import List

def concatenate_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Função para transformar uma lista de DataFrames em um único DataFrame
    """
    
    return pd.concat(data_frame_list, ignore_index = True)