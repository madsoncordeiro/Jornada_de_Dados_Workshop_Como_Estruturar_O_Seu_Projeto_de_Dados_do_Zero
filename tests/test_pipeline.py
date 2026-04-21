import pandas as pd
from app.pipeline.transform import concatenate_data_frames

df_1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df_2 = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})

def testar_a_concatenacao_da_lista_de_dataframe():
    """
    Use arrange, act e assert para testar a função concatenate_data_frames
    """
    
    # Arrange
    data_frame_list = [df_1, df_2]
    data_frame = pd.concat(data_frame_list, ignore_index = True)
    
    # Act
    df = concatenate_data_frames(data_frame_list)
    
    # Assert
    assert df.shape == (4, 2)
    assert data_frame.equals(df)