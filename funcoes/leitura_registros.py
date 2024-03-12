import streamlit as st

def exibir_linha_especifica(df, valor_coluna='0000'):
    # Verifica se a "Coluna 1" existe no DataFrame
    if 'Coluna_1' in df.columns:
        # Filtra o DataFrame para linhas onde a "Coluna 1" é igual ao valor_coluna
        linha_filtrada = df[df['Coluna_1'] == valor_coluna]
        
        # Verifica se a linha filtrada não está vazia
        if not linha_filtrada.empty:
            # Exibe todas as colunas da linha filtrada
            st.write(linha_filtrada)
        else:
            st.write(f"Nenhuma linha encontrada com 'Coluna_1' igual a {valor_coluna}.")
    else:
        st.write("A 'Coluna_1' não existe neste DataFrame.")
