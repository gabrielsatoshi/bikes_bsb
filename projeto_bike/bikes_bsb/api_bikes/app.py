from flask import Flask, jsonify, request,g
import sqlite3
app = Flask(__name__)

# Dados em memória para simular um "banco de dados"


# Rota para obter todas as tarefas

@app.route('/', methods=['GET'])
def getHome():  
    text ="<h1>Bem vindo a Api de python</h1> <br/><table border='1'><tr><th>Rota</th><th>Método</th><th>Link</th></tr><tr><td>/df_stations</td><td>GET</td><td><a href='/df_stations'>link</a></td></tr><tr><td>/df_stations/:id</td><td>GET</td><td><a href='/df_stations/4'>link</a></td></tr><tr><td>/df_rides</td><td>GET</td><td><a href='/df_rides'>link</a></td></tr><tr><td>/df_rides/id</td><td>GET</td><td><a href='/df_rides/8'>link</a></td></tr><tr><td>/df_station</td><td>POST</td><td>Necessita Postman</td></tr></table>"    
    return  text

    


@app.route('/df_stations', methods=['GET'])
def getStations():
    
    conn = sqlite3.connect('banco_bikes')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM df_stations')
    dados = cursor.fetchall()
    conn.close()
    chaves = [description[0] for description in cursor.description]
    dados_com_chaves = []
    for linha in dados:
        dados_com_chaves.append({chaves[i]: valor for i, valor in enumerate(linha)})

    # Retornar os dados com chaves personalizadas como JSON
    return jsonify({'dados': dados_com_chaves})

@app.route('/df_stations/<int:station_id>', methods=['GET'])
def getStationsById(station_id):    
    conn = sqlite3.connect('banco_bikes')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM df_stations WHERE ID = ?',(station_id,))
    dados = cursor.fetchall()
    conn.close()
    chaves = [description[0] for description in cursor.description]
    dados_com_chaves = []
    for linha in dados:
        dados_com_chaves.append({chaves[i]: valor for i, valor in enumerate(linha)})

    # Retornar os dados com chaves personalizadas como JSON
    return jsonify( {'dados': 'nao ha dados com esse ID'} if dados == [] else {'dados': dados_com_chaves})

@app.route('/df_rides', methods=['GET'])
def getRides():
    
    conn = sqlite3.connect('banco_bikes')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM df_rides')
    dados = cursor.fetchall()
    conn.close()
    chaves = [description[0] for description in cursor.description]
    dados_com_chaves = []
    for linha in dados:
        dados_com_chaves.append({chaves[i]: valor for i, valor in enumerate(linha)})

    # Retornar os dados com chaves personalizadas como JSON
    return jsonify({'dados': dados_com_chaves})

@app.route('/df_rides/<int:ride_id>', methods=['GET'])
def getRidesById(ride_id):
    
    conn = sqlite3.connect('banco_bikes')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM df_rides WHERE ID = ?',(ride_id,))
    dados = cursor.fetchall()
    conn.close()
    chaves = [description[0] for description in cursor.description]
    dados_com_chaves = []
    for linha in dados:
        dados_com_chaves.append({chaves[i]: valor for i, valor in enumerate(linha)})

    # Retornar os dados com chaves personalizadas como JSON
    return jsonify( {'dados': 'nao ha dados com esse ID'} if dados == [] else {'dados': dados_com_chaves})

@app.route('/df_stations', methods=['POST'])
def post_example():
    if request.method == 'POST':
        data = request.json         
        lat=data.get('lat')
        long =data.get('long')
        station=data.get('station')
        station_name = data.get('station_name')
        station_number = data.get('station_number')
        
        conn = obter_conexao()
        cursor = conn.cursor()      
    
        cursor.execute("INSERT INTO df_stations (STATION,STATION_NUMBER,STATION_NAME,LAT,LON) VALUES (?,?,?,?,?)", (station, station_number,station_name,lat,long ))
        conn.commit()

        conn.close()

        return jsonify({'message': 'Estação adicionada com sucesso!'})        
    else:
        return 'Requisição não é do tipo POST'
    
def obter_conexao():
    conexao = getattr(g, '_conexao', None)
    if conexao is None:
        conexao = g._conexao = sqlite3.connect('banco_bikes',timeout=60)
    return conexao

def fechar_conexao(exception):
    conexao = getattr(g, '_conexao', None)
    if conexao is not None:
        conexao.close()
        
if __name__ == '__main__':
    app.run(debug=True)