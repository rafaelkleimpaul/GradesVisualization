import matplotlib.pyplot as plt
import theme
import sqlite3
import pandas as pd
import logging 


## Faz a media de notas dos alunos entre 18 e 35 anos
## Faz uma classificação de notas e mostra em ordem alfabetica da maior para menor

## Cursor -- Retorna lista de tuples
## Pandas -- Retorna um DataFrame

logging.basicConfig(level = logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ]
    )
try:
    
    def selecionar_tema():
        try:
            #logging.info('---- Selecionar Tema ----')
            #print('----- Lista de Temas -----\n')
            #for i in theme.plt_theme:
            #    print(f'Opção:{theme.plt_theme.index(i)} --- {i}')
            #tema = int(input('Digite um numero de 1 à 28 para selecionar o tema: \n'))
            #logging.info(f'Tema selecionado{tema}')
            print('')
        except Exception as e:
            logging.error("Erro ao executar o código", exc_info=True)
        
    def conectar_DB():
        try:
            logging.info('----Conectando ao DB----')
            conn = sqlite3.connect('./SENAI.db') #chama DB
            return conn
        except Exception as e:
            logging.error("Erro ao conectar no banco de dados", exc_info=True )
            return None
        
    def criar_DataFrame(conn):
        try:    
            df = pd.read_sql_query('SELECT Nomes, Idade FROM Dados WHERE Idade >= 18 AND Idade <=35', conn)
            logging.info(f"DataFrame criado:\n{df}")
            return df
        except Exception as e:
            logging.error("Erro ao criar DataFrame", exc_info=True)
            return None
            
            
    def main():
        conn = conectar_DB()
        if not conn:
            logging.critical("Sem conexão. Encerrando.")
            return
        try:
            df = criar_DataFrame(conn)
            if df is not None:
                #print(df.head())     # mostra primeiras linhas
                #print(df.dtypes)     # mostra tipos das colunas
                print(df.describe()) # estatísticas básicas
        finally:
            conn.close()

except Exception as e:
    logging.error("Erro ao executar o código", exc_info=True)
    
    
if __name__ == '__main__':
    main()