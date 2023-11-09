import sqlite3
import csv

banco = 'banco_bikes'
con = sqlite3.connect(banco)
cursor = con.cursor()


query_tabela_df_stations = '''
    CREATE TABLE IF NOT EXISTS df_stations (
        ID INTEGER PRIMARY KEY NOT NULL,
        STATION VARCHAR NOT NULL,
        STATION_NUMBER VARCHAR NOT NULL,
        STATION_NAME VARCHAR NOT NULL,
        LAT VARCHAR NOT NULL,
        LON VARCHAR NOT NULL
    );
'''

cursor.execute(query_tabela_df_stations)


try:
    with open('df_stations.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  


        for row in csv_reader:
            cursor.execute('''
                INSERT INTO df_stations (STATION, STATION_NUMBER, STATION_NAME, LAT, LON)
                VALUES (?, ?, ?, ?, ?)
            ''', (row[0], row[1], row[2], row[3], row[4]))


    con.commit()

except sqlite3.Error as e:
    print("Erro ao inserir dados no banco de dados:", e)


query_tabela_df_rides = '''
    CREATE TABLE IF NOT EXISTS df_rides (
        ID INTEGER PRIMARY KEY NOT NULL,
        USER_GENDER VARCHAR NOT NULL,
        USER_BIRTHDATE VARCHAR NOT NULL,
        USER_RESIDENCE VARCHAR NOT NULL,
        RIDE_DATA VARCHAR NOT NULL,
        TIME_START VARCHAR NOT NULL,
        TIME_END DATE NOT NULL,
        STATION_START VARCHAR NOT NULL,
        STATION_END VARCHAR NOT NULL,
        RIDE_DURATION VARCHAR NOT NULL,
        RIDE_LATE VARCHAR NOT NULL);
        '''
cursor.execute(query_tabela_df_rides)

try:
    with open('df_rides.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  


        for row in csv_reader:
            cursor.execute('''
                INSERT INTO df_rides (USER_GENDER, USER_BIRTHDATE,USER_RESIDENCE,RIDE_DATA,TIME_START,TIME_END,STATION_START,STATION_END,RIDE_DURATION,RIDE_LATE)
                VALUES (?, ?, ?, ?, ?,?, ?, ?, ?,?)
            ''', (row[0], row[1], row[2], row[3], row[4],row[5],row[6],row[7],row[8],row[9]))

    con.commit()

except sqlite3.Error as e:
    print("Erro ao inserir dados na tabela outra_tabela:", e)

finally:
    con.close()
