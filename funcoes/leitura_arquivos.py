import re
import pandas as pd
from funcoes.dicionario_piscofins import piscofins as dpiscofins
from funcoes.dicionario_icms import icms as dicms
from funcoes.dicionario_ecd import ecd as decd

def leitura_tipo_arquivo(nome_arquivo):
    # Tentativa de encontrar padrões específicos nos nomes dos arquivos
    padroes = [
        r"SPED-ECD",
        r"PISCOFINS",
        r"SPED-EFD"
    ]
    
    for padrao in padroes:
        if re.search(padrao, nome_arquivo):
            return re.search(padrao, nome_arquivo).group()
    return "Padrão não encontrado"

def processar_arquivo_upload(arquivo, tipo_arquivo):
    dados_por_registro = {}
    contador_de_linhas = 1
    
    # Seleciona o dicionário correto baseado no tipo de arquivo
    if tipo_arquivo == 'SPED-ECD':
        dicionario_atual = decd
    elif tipo_arquivo == 'PISCOFINS':
        dicionario_atual = dpiscofins
    elif tipo_arquivo == 'SPED-EFD':
        dicionario_atual = dicms
    else:
        dicionario_atual = {}
    
    # Supondo que o arquivo esteja codificado em 'iso-8859-1'
    conteudo = arquivo.read().decode('iso-8859-1')
    
    for linha in conteudo.splitlines():
        linha = linha.replace('\x00', '')
        if linha.startswith("|"):
            partes = linha.strip().split('|')[1:-1]  # Remove elementos vazios das extremidades
            if partes:  # Verifica se 'partes' não está vazia
                tipo_registro = partes[0]
                linha_dados = [contador_de_linhas] + partes
                    
                if tipo_registro not in dados_por_registro:
                    dados_por_registro[tipo_registro] = []
                dados_por_registro[tipo_registro].append(linha_dados)
                    
                contador_de_linhas += 1
    
    dfs = {}
    for registro, linhas in dados_por_registro.items():
        if registro in dicionario_atual:
            # Usar o dicionário para definir os nomes das colunas, excluindo a última coluna
            colunas = ['Contador_Linhas'] + [dicionario_atual[registro].get(f'Coluna_{i}', f'Coluna_{i}') for i in range(1, len(linhas[0])-1)]  # Modificação aqui
        else:
            # Se o registro não estiver no dicionário, usar nomes genéricos, excluindo a última coluna
            colunas = ['Contador_Linhas'] + [f'Coluna_{i}' for i in range(1, len(linhas[0])-1)]  # Modificação aqui
        
        # Modificação aqui para excluir a última coluna de dados de cada linha
        linhas_ajustadas = [linha[:-1] for linha in linhas]
        
        dfs[registro] = pd.DataFrame(linhas_ajustadas, columns=colunas)
    
    return dfs
