from fastapi import FastAPI
import sqlite3
#Lembrar de utilizar o pip install uvicorn
app = FastAPI()


def conectar_banco():
    return sqlite3.connect("banco_bikes")
@app.get("/df_stations")
def pegar_df_stations():
    con = conectar_banco()
    cursor = con.cursor()
    query = 'select * from df_stations'
    cursor.execute(query)
    dados = cursor.fetchall()
    con.close()
    return {"Dados df_stations :":dados}

@app.get("/df_rides")
def pegar_df_stations():
    con = conectar_banco()
    cursor = con.cursor()
    query = 'select * from df_rides'
    cursor.execute(query)
    dados = cursor.fetchall()
    con.close()

    return {"Dados df_rides :":dados}
