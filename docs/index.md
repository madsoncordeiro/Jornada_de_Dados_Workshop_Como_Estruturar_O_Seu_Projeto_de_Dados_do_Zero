# Workflow

```mermaid
flowchart LR
    subgraph ETL[Pipeline]
        A(Múltiplos Arquivos Excel) --> B[Extract: extract_from_excel]
        B[Extract: extract_from_excel] --> |Gera uma lista de DataFrames| C[Transformation: concatenate_data_frames]
        C[Transformation: concatenate_data_frames] -->|Gera um DataFrame Consolidado| D[Load: Converte para Excel]
        D(Load: Converte para Excel) --> |Salva o consolidado em Excel| E(Pasta Output: Um arquivo único Excel)
    end
```

# Função de extração de dados

## ::: app.pipeline.extract.extract_from_excel

# Função de transformação de dados

## ::: app.pipeline.transform.concatenate_data_frames

# Função de carga de dados

## ::: app.pipeline.load.load_excel
