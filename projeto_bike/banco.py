import sqlite3
import csv

banco = 'banco_bikes'
con = sqlite3.connect(banco)
cursor = con.cursor()

# Crie a tabela (se ainda não existir)
query_tabela = '''
    CREATE TABLE IF NOT EXISTS df_stations (
        ID INTEGER PRIMARY KEY NOT NULL,
        STATION VARCHAR NOT NULL,
        STATION_NUMBER VARCHAR NOT NULL,
        STATION_NAME VARCHAR NOT NULL,
        LAT VARCHAR NOT NULL,
        LON VARCHAR NOT NULL
    );
'''
cursor.execute(query_tabela)

# Abra o arquivo CSV com o codec apropriado (exemplo: UTF-8)
try:
    with open('df_stations.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Pule o cabeçalho, se houver

        # Itere pelas linhas do CSV e insira os dados na tabela
        for row in csv_reader:
            cursor.execute('''
                INSERT INTO df_stations (STATION, STATION_NUMBER, STATION_NAME, LAT, LON)
                VALUES (?, ?, ?, ?, ?)
            ''', (row[0], row[1], row[2], row[3], row[4]))

    # Commit para salvar as alterações no banco de dados
    con.commit()

except sqlite3.Error as e:
    print("Erro ao inserir dados no banco de dados:", e)
finally:
    con.close()
