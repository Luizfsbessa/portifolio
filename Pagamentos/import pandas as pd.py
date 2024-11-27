import pandas as pd
import time
import os
print("Diretório atual:", os.getcwd())
start_time = time.time()
print("Iniciando a leitura do arquivo...")
df = pd.read_csv('pg25.csv')
print("Arquivo lido com sucesso!")
print(f"Tempo de execução: {time.time() - start_time} segundos")
