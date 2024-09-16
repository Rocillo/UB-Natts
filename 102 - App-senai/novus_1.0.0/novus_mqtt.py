#logica para comunicação Mqtt

import paho.mqtt.client as mqtt
import time
import json
import database
from datetime import datetime

databaseOBJ=database.postgresDatabase(host='localhost')

mqttip = "192.168.0.3"
client = mqtt.Client(clean_session=True)
#client.username_pw_set("ist","ist")
client.connect(mqttip, 1883, 60)

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
        #print(ch)
        dtstring = dt.strftime ('%Y/%m/%d %H:%M:%S')
        print (str(ch), ch['events'])

       

        # Canal 1
        if "chd1" in str(ch):
            status_ch1 = ch['events']['chd1']['edge']
            timestamp_ch1 = ch['events']['chd1']['timestamp']
            date_timestamp_ch1 = datetime.utcfromtimestamp(timestamp_ch1).strftime('%d-%m-%Y %H:%M:%S')
            print(f"Status Canal 1: {status_ch1}, Timestamp: {timestamp_ch1}, Data: {date_timestamp_ch1}")
            if status_ch1 == 0:  # Substitua "ativado" pelo evento específico
                print("Canal 1 Ativado")

        # Canal 2
        if "chd2" in str(ch):
            status_ch2 = ch['events']['chd2']['edge']
            timestamp_ch2 = ch['events']['chd2']['timestamp']
            date_timestamp_ch2 = datetime.utcfromtimestamp(timestamp_ch2).strftime('%d-%m-%Y %H:%M:%S')
            print(f"Status Canal 2: {status_ch2}, Timestamp: {timestamp_ch2}, Data: {date_timestamp_ch2}")
            if status_ch2 == 0:
                print("Canal 2 Ativado")

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

    
        









    
    
    