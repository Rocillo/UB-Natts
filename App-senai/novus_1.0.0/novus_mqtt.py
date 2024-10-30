#logica para comunicação Mqtt

import paho.mqtt.client as mqtt
import time
import json
import database
import psycopg2
from datetime import datetime

#databaseOBJ=database.postgresDatabase(host='localhost')

mqttip = "192.168.1.158"
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
            host='192.168.1.158',
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

        # Canal 1
        if "chd1" in str(ch):

            conn = connect_db()
            status_ch1 = ch['events']['chd1']['edge']
            timestamp_ch1 = ch['events']['chd1']['timestamp']
            date_timestamp_ch1 = datetime.fromtimestamp(timestamp_ch1).strftime('%d-%m-%Y %H:%M:%S')
            print(f"Status Canal 1: {status_ch1}, Timestamp: {timestamp_ch1}, Data: {date_timestamp_ch1}")
            cursor = conn.cursor()
            if status_ch1 == 0:  # Quando o canal 1 for ativado
                print("Canal 1 Ativado")
                data_atual = dtstring
                
                # Seleciona a sessão mais recente com workstation_id = 1 e is_done = 'false'
                cursor.execute("""
                    SELECT session_id 
                    FROM worksessions
                    WHERE workstation_id = 1 AND is_done = 'false'
                    ORDER BY start_time DESC  -- Pega a sessão mais recente
                    LIMIT 1;
                """)
                
                resultado = cursor.fetchone()
                
                if resultado:
                    session_id = resultado[0]
                    
                    # Atualiza o campo start_time da sessão mais recente
                    cursor.execute("""
                        UPDATE worksessions
                        SET start_time = %s
                        WHERE session_id = %s;
                    """, (data_atual, session_id))
                    
                    conn.commit()  # Confirma a transação
                    print("start_time atualizado com sucesso para a sessão mais recente.")
                else:
                    print("Nenhuma sessão encontrada para workstation_id = 1 com is_done = 'false'.")
            
            # Quando o cartão for retirado (ch1 == 1)
            elif status_ch1 == 1:  
                print("Cartão retirado do posto de trabalho")
                data_atual = dtstring

                # Seleciona a sessão mais recente com workstation_id = 1, is_done = 'false', e start_time já definido
                cursor.execute("""
                    SELECT session_id, start_time 
                    FROM worksessions
                    WHERE workstation_id = 1 AND is_done = 'false' AND start_time IS NOT NULL
                    ORDER BY start_time DESC
                    LIMIT 1;
                """)
                
                resultado = cursor.fetchone()
                
                if resultado:
                    session_id = resultado[0]
                    start_time = resultado[1]

                    if start_time:  # Verifica se o start_time está definido
                        # Atualiza o campo end_time e is_done da sessão mais recente
                        cursor.execute("""
                            UPDATE worksessions
                            SET end_time = %s, is_done = 'true'
                            WHERE session_id = %s;
                        """, (data_atual, session_id))
                        
                        conn.commit()
                        print("end_time atualizado e sessão marcada como finalizada.")
                    else:
                        print("Sessão encontrada, mas start_time não está definido.")
                else:
                    print("Nenhuma sessão válida encontrada para workstation_id = 1 com is_done = 'false' e start_time definido.")                    

        # Canal 2
        if "chd2" in str(ch):

            conn = connect_db()
            status_ch2 = ch['events']['chd2']['edge']
            timestamp_ch2 = ch['events']['chd2']['timestamp']
            date_timestamp_ch2 = datetime.fromtimestamp(timestamp_ch2).strftime('%d-%m-%Y %H:%M:%S')
            print(f"Status Canal 2: {status_ch2}, Timestamp: {timestamp_ch2}, Data: {date_timestamp_ch2}")
            cursor = conn.cursor()
            if status_ch2 == 0:  # Quando o canal 1 for ativado
                print("Canal 2 Ativado")
                data_atual = dtstring
                
                # Seleciona a sessão mais recente com workstation_id = 1 e is_done = 'false'
                cursor.execute("""
                    SELECT session_id 
                    FROM worksessions
                    WHERE workstation_id = 2 AND is_done = 'false'
                    ORDER BY start_time DESC  -- Pega a sessão mais recente
                    LIMIT 1;
                """)
                
                resultado = cursor.fetchone()
                
                if resultado:
                    session_id = resultado[0]
                    
                    # Atualiza o campo start_time da sessão mais recente
                    cursor.execute("""
                        UPDATE worksessions
                        SET start_time = %s
                        WHERE session_id = %s;
                    """, (data_atual, session_id))
                    
                    conn.commit()  # Confirma a transação
                    print("start_time atualizado com sucesso para a sessão mais recente.")
                else:
                    print("Nenhuma sessão encontrada para workstation_id = 2 com is_done = 'false'.")
            
            # Quando o cartão for retirado (ch1 == 1)
            elif status_ch2 == 1:  
                print("Cartão retirado do posto de trabalho")
                data_atual = dtstring

                # Seleciona a sessão mais recente com workstation_id = 1, is_done = 'false', e start_time já definido
                cursor.execute("""
                    SELECT session_id, start_time 
                    FROM worksessions
                    WHERE workstation_id = 2 AND is_done = 'false' AND start_time IS NOT NULL
                    ORDER BY start_time DESC
                    LIMIT 1;
                """)
                
                resultado = cursor.fetchone()
                
                if resultado:
                    session_id = resultado[0]
                    start_time = resultado[1]

                    if start_time:  # Verifica se o start_time está definido
                        # Atualiza o campo end_time e is_done da sessão mais recente
                        cursor.execute("""
                            UPDATE worksessions
                            SET end_time = %s, is_done = 'true'
                            WHERE session_id = %s;
                        """, (data_atual, session_id))
                        
                        conn.commit()
                        print("end_time atualizado e sessão marcada como finalizada.")
                    else:
                        print("Sessão encontrada, mas start_time não está definido.")
                else:
                    print("Nenhuma sessão válida encontrada para workstation_id = 2 com is_done = 'false' e start_time definido.")

        # Canal 3
        if "chd3" in str(ch):
            status_ch3 = ch['events']['chd3']['edge']
            timestamp_ch3 = ch['events']['chd3']['timestamp']
            date_timestamp_ch3 = datetime.utcfromtimestamp(timestamp_ch3).strftime('%d-%m-%Y %H:%M:%S')
            print(f"Status Canal 3: {status_ch3}, Timestamp: {timestamp_ch3}, Data: {date_timestamp_ch3}")
            if status_ch3 == 0:
                print("Canal 3 Ativado")

        # Canal 4
        if "chd4" in str(ch):
            status_ch4 = ch['events']['chd4']['edge']
            timestamp_ch4 = ch['events']['chd4']['timestamp']
            date_timestamp_ch4 = datetime.utcfromtimestamp(timestamp_ch4).strftime('%d-%m-%Y %H:%M:%S')
            print(f"Status Canal 4: {status_ch4}, Timestamp: {timestamp_ch4}, Data: {date_timestamp_ch4}")
            if status_ch4 == 0:
                print("Canal 4 Ativado")

        # Canal 5
        if "chd5" in str(ch):
            status_ch5 = ch['events']['chd5']['edge']
            timestamp_ch5 = ch['events']['chd5']['timestamp']
            date_timestamp_ch5 = datetime.utcfromtimestamp(timestamp_ch5).strftime('%d-%m-%Y %H:%M:%S')
            print(f"Status Canal 5: {status_ch5}, Timestamp: {timestamp_ch5}, Data: {date_timestamp_ch5}")
            if status_ch5 == 0:
                print("Canal 5 Ativado")

        # Canal 6
        if "chd6" in str(ch):
            status_ch6 = ch['events']['chd6']['edge']
            timestamp_ch6 = ch['events']['chd6']['timestamp']
            date_timestamp_ch6 = datetime.utcfromtimestamp(timestamp_ch6).strftime('%d-%m-%Y %H:%M:%S')
            print(f"Status Canal 6: {status_ch6}, Timestamp: {timestamp_ch6}, Data: {date_timestamp_ch6}")
            if status_ch6 == 0:
                print("Canal 6 Ativado")
    

#Inicialização da Aplicação - LOOP FOREVER
   
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()

    
        









    
    
    