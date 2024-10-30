#logica para comunicação Mqtt

import paho.mqtt.client as mqtt
import time
import json
import database
import psycopg2
from datetime import datetime

#databaseOBJ=database.postgresDatabase(host='localhost')

mqttip = "localhost"
client = mqtt.Client(clean_session=True)
#client.username_pw_set("ist","ist")
client.connect(mqttip, 1883, 60)
# Variável global para a conexão
conn = None
qtprod = ''
estado_maq1=0
estado_maq2=0
estado_maq3=0
contagem_maq1=0
contagem_maq2=0
contagem_maq3=0
contagem_maq4=0
contagem_maq5=0
contagem_maq6=0

# Função para conectar ao banco de dados (é chamada dentro de on_message)
def connect_db():
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='ub_natts',
            user='postgres',
            password='postgres'
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


def on_connect(client, userdata, flags, rc):
    print("Connectado no BROKER com sucesso!! - RC="+str(rc))

    #Declara os tópicos que está inscrito
    client.subscribe("NOVUS/Maquina01/events",0)

def on_message(client, userdata, msg):
    dado = str(msg.payload).split("'")
    t=str(dado[1])
    qtprod = t
    if qtprod != '':
        ch = json.loads(qtprod)
        dt = datetime.now()
        dtstring = dt.strftime('%Y/%m/%d %H:%M:%S')
        # print(str(ch), ch['events'])

        for canal in range(1, 7):  # De 1 a 6
            ch_key = f'chd{canal}'
            workstation_id = canal

            if ch_key in str(ch):
                conn = connect_db()
                cursor = conn.cursor()
                status = ch['events'][ch_key]['edge']
                timestamp = ch['events'][ch_key]['timestamp']
                date_timestamp = datetime.fromtimestamp(timestamp).strftime('%d-%m-%Y %H:%M:%S')
                print(f"Status Canal {canal}: {status}, Timestamp: {timestamp}, Data: {date_timestamp}")

                if status == 0:  # Quando o canal for ativado
                    print(f"Canal {canal} Ativado")
                    data_atual = dtstring

                    # Seleciona a sessão mais recente para a workstation correspondente com is_done = 'false'
                    cursor.execute(f"""
                        SELECT session_id 
                        FROM worksessions
                        WHERE workstation_id = %s AND is_done = 'false'
                        ORDER BY start_time DESC
                        LIMIT 1;
                    """, (workstation_id,))
                    
                    resultado = cursor.fetchone()

                    if resultado:
                        session_id = resultado[0]

                        # Atualiza o campo start_time da sessão mais recente
                        cursor.execute("""
                            UPDATE worksessions
                            SET start_time = %s
                            WHERE session_id = %s;
                        """, (data_atual, session_id))

                        conn.commit()
                        print(f"start_time atualizado com sucesso para a sessão mais recente da workstation {workstation_id}.")
                    else:
                        print(f"Nenhuma sessão encontrada para workstation_id = {workstation_id} com is_done = 'false'.")

                elif status == 1:  # Quando o cartão for retirado
                    print(f"Cartão retirado do posto de trabalho no Canal {canal}")
                    data_atual = dtstring

                    # Seleciona a sessão mais recente com is_done = 'false' e start_time já definido
                    cursor.execute(f"""
                        SELECT session_id, start_time 
                        FROM worksessions
                        WHERE workstation_id = %s AND is_done = 'false' AND start_time IS NOT NULL
                        ORDER BY start_time DESC
                        LIMIT 1;
                    """, (workstation_id,))

                    resultado = cursor.fetchone()

                    if resultado:
                        session_id = resultado[0]
                        start_time = resultado[1]

                        if start_time:
                            # Atualiza o campo end_time e is_done da sessão mais recente
                            cursor.execute("""
                                UPDATE worksessions
                                SET end_time = %s, is_done = 'true'
                                WHERE session_id = %s;
                            """, (data_atual, session_id))

                            conn.commit()
                            print(f"end_time atualizado e sessão marcada como finalizada para workstation {workstation_id}.")
                        else:
                            print(f"Sessão encontrada para workstation {workstation_id}, mas start_time não está definido.")
                    else:
                        print(f"Nenhuma sessão válida encontrada para workstation_id = {workstation_id} com is_done = 'false' e start_time definido.")

                cursor.close()
                conn.close()

#Inicialização da Aplicação - LOOP FOREVER 
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()

    
        









    
    
    