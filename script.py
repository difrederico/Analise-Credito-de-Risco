import pandas as pd

# Nome do arquivo CSV de entrada
csv_file = 'dados_risco_credito.csv'
# Nome do arquivo SQL de saída
sql_file = 'insert_dados_risco_credito.sql'

try:
    
    df = pd.read_csv(csv_file, encoding='utf-8') # Ou encoding='latin1' se o problema de codificação anterior persistir
    print(f"Arquivo '{csv_file}' carregado com sucesso. {len(df)} registros encontrados.")

    with open(sql_file, 'w', encoding='utf-8') as f:
        f.write("-- SQL Inserts gerados a partir de dados_risco_credito.csv\n")
        f.write("-- Certifique-se de que a tabela DADOS_RISCO_CREDITO exista antes de executar.\n")
        f.write("-- Lembre-se de executar COMMIT; no final para salvar as alterações.\n\n")

        # Gerar uma instrução INSERT para cada linha do DataFrame
        for index, row in df.iterrows():
            # ****** ATENÇÃO AQUI: AJUSTAR A CAPITALIZAÇÃO DOS NOMES DAS COLUNAS ******
            # Se o CSV original tinha 'historico_pagamento' e 'status_emprego' (minúsculas ou snake_case):
            historico_pagamento_val = f"'{str(row['historico_pagamento']).upper()}'" # Acessa 'historico_pagamento'
            status_emprego_val = f"'{str(row['status_emprego']).upper()}'" # Acessa 'status_emprego'
            

            insert_statement = (
                f"INSERT INTO DADOS_RISCO_CREDITO (\n"
                f"    ID_CLIENTE, IDADE, SALARIO_MENSAL, ANOS_EMPREGADO, DIVIDA_TOTAL,\n"
                f"    NUMERO_CONTAS_BANCO, HISTORICO_PAGAMENTO, STATUS_EMPREGO,\n" # Os nomes aqui são os da TABELA Oracle, que podem ser diferentes (maiúsculas)
                f"    SCORE_CREDITO_EXTERNO, INADIMPLENTE\n"
                f") VALUES (\n"
                f"    {int(row['id_cliente'])}, {int(row['idade'])}, {float(row['salario_mensal']):.2f}, {int(row['anos_empregado'])}, {float(row['divida_total']):.2f},\n"
                f"    {int(row['numero_contas_banco'])}, {historico_pagamento_val}, {status_emprego_val},\n" # Aqui usa as variáveis com o valor ajustado
                f"    {int(row['score_credito_externo'])}, {int(row['inadimplente'])}\n"
                f");\n"
            )
            f.write(insert_statement)

        f.write("\nCOMMIT;\n")

    print(f"Arquivo '{sql_file}' gerado com sucesso. Contém {len(df)} instruções INSERT + COMMIT.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{csv_file}' não foi encontrado. Certifique-se de que ele está na mesma pasta do script.")
except KeyError as e:
    print(f"Ocorreu um erro: A coluna '{e}' não foi encontrada no DataFrame. Verifique a capitalização dos nomes das colunas no CSV.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")