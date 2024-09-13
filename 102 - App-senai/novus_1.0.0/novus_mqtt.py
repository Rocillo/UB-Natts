#logica para comunicação Mqtt

import paho.mqtt.client as mqtt
import time
import json
import database
from datetime import datetime

databaseOBJ=database.postgresDatabase(host='localhost')

mqttip = "test.mosquitto.org"
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
    client.subscribe("teste/teste/nvus",1)

def on_message(client, userdata, msg):
    dado = str(msg.payload).split("'")
    t=str(dado[1])
    qtprod = t
    if qtprod != '':
        ch = json.loads(qtprod)
        dt = datetime.now()
        #print(ch)
        dtstring = dt.strftime ('%Y/%m/%d %H:%M:%S')
        print (str(ch))
        while ("chd1" in str(ch)):
            if ("chd2" in str(ch)):
                try:
                    contagem_maq1 = ch['events']['chd1']['edge']
                    contagem_maq2 = ch['events']['chd2']['edge']
                    if(contagem_maq1==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd1": 1}}}')
                    if(contagem_maq2==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd2": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            elif ("chd3" in str(ch)):
                try:
                    contagem_maq1 = ch['events']['chd1']['edge']
                    contagem_maq3 = ch['events']['chd3']['edge']
                    if(contagem_maq1==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd1": 1}}}')
                    if(contagem_maq3==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd3": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            elif ("chd4" in str(ch)):
                try:
                    contagem_maq1 = ch['events']['chd1']['edge']
                    contagem_maq4 = ch['events']['chd4']['edge']
                    if(contagem_maq1==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd1": 1}}}')
                    if(contagem_maq4==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd4": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            elif ("chd5" in str(ch)):
                try:
                    contagem_maq1 = ch['events']['chd1']['edge']
                    contagem_maq5 = ch['events']['chd5']['edge']
                    if(contagem_maq1==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd1": 1}}}')
                    if(contagem_maq5==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 3)")
                        print('Adicionado Ciclo - BANCADA 3 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd5": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            
            elif("chd6" in str(ch)):
                try:
                    contagem_maq1 = ch['events']['chd1']['edge']
                    contagem_maq6 = ch['events']['chd6']['edge']
                    if(contagem_maq1==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd1": 1}}}')  
                    if(contagem_maq6==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 4)")
                        print('Adicionado Ciclo - BANCADA 4 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd6": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            else:
                try:
                    contagem_maq1 = ch['events']['chd1']['edge']
                    #Dados da MÁQUINA - 1
                    if(contagem_maq1==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd1": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
        while ("chd2" in str(ch)):
            if ("chd1" in str(ch)):
                try:
                    contagem_maq1 = ch['events']['chd1']['edge']
                    contagem_maq2 = ch['events']['chd2']['edge']
                    if(contagem_maq1==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd1": 1}}}')
                    if(contagem_maq2==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd2": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            elif ("chd3" in str(ch)):
                try:
                    contagem_maq2 = ch['events']['chd2']['edge']
                    contagem_maq3 = ch['events']['chd3']['edge']
                    if(contagem_maq2==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd2": 1}}}')
                    if(contagem_maq3==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd3": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
                
            elif ("chd4" in str(ch)):
                try:
                    contagem_maq2 = ch['events']['chd2']['edge']
                    contagem_maq4 = ch['events']['chd4']['edge']
                    if(contagem_maq2==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd2": 1}}}')
                    if(contagem_maq4==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd4": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break

            elif ("chd5" in str(ch)):
                try:
                    contagem_maq2 = ch['events']['chd2']['edge']
                    contagem_maq5 = ch['events']['chd5']['edge']
                    if(contagem_maq2==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd2": 1}}}')
                    if(contagem_maq5==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 3)")
                        print('Adicionado Ciclo - BANCADA 3 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd5": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            
            elif("chd6" in str(ch)):
                try:
                    contagem_maq2 = ch['events']['chd2']['edge']
                    contagem_maq6 = ch['events']['chd6']['edge']
                    if(contagem_maq2==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd2": 1}}}')
                    if(contagem_maq6==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 4)")
                        print('Adicionado Ciclo - BANCADA 4 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd6": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            else:
                try:
                    contagem_maq2 = ch['events']['chd2']['edge']
                    #Dados da MÁQUINA - 2
                    if(contagem_maq2==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd2": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
        while ("chd3" in str(ch)):
            if ("chd1" in str(ch)):
                try:
                    contagem_maq1 = ch['events']['chd1']['edge']
                    contagem_maq3 = ch['events']['chd3']['edge']
                    if(contagem_maq1==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd1": 1}}}')
                    if(contagem_maq3==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd3": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            elif ("chd2" in str(ch)):
                try:
                    contagem_maq2 = ch['events']['chd2']['edge']
                    contagem_maq3 = ch['events']['chd3']['edge']
                    if(contagem_maq2==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd2": 1}}}')
                    if(contagem_maq3==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd3": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break  
            elif ("chd4" in str(ch)):
                try:
                    contagem_maq3 = ch['events']['chd3']['edge']
                    contagem_maq4 = ch['events']['chd4']['edge']
                    if(contagem_maq3==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd3": 1}}}')
                    if(contagem_maq4==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd4": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break

            elif ("chd5" in str(ch)):
                try:
                    contagem_maq3 = ch['events']['chd3']['edge']
                    contagem_maq5 = ch['events']['chd5']['edge']
                    if(contagem_maq3==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd3": 1}}}')
                    if(contagem_maq5==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 3)")
                        print('Adicionado Ciclo - BANCADA 3 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd5": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            elif("chd6" in str(ch)):
                try:
                    contagem_maq3 = ch['events']['chd3']['edge']
                    contagem_maq6 = ch['events']['chd6']['edge']
                    if(contagem_maq3==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd3": 1}}}')
                    if(contagem_maq6==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 4)")
                        print('Adicionado Ciclo - BANCADA 4 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd6": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            else:
                try:
                    contagem_maq3 = ch['events']['chd3']['edge']
                    #Dados da MÁQUINA - 3
                    if(contagem_maq3==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd3": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
        while ("chd4" in str(ch)):
            if ("chd1" in str(ch)):
                try:
                    contagem_maq1 = ch['events']['chd1']['edge']
                    contagem_maq4 = ch['events']['chd4']['edge']
                    if(contagem_maq1==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd1": 1}}}')
                    if(contagem_maq4==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd4": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            elif ("chd2" in str(ch)):
                try:
                    contagem_maq2 = ch['events']['chd2']['edge']
                    contagem_maq4 = ch['events']['chd4']['edge']
                    if(contagem_maq2==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd2": 1}}}')
                    if(contagem_maq4==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd4": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break  
            elif ("chd3" in str(ch)):
                try:
                    contagem_maq3 = ch['events']['chd3']['edge']
                    contagem_maq4 = ch['events']['chd4']['edge']
                    if(contagem_maq3==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd3": 1}}}')
                    if(contagem_maq4==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd4": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break

            elif ("chd5" in str(ch)):
                try:
                    contagem_maq4 = ch['events']['chd4']['edge']
                    contagem_maq5 = ch['events']['chd5']['edge']
                    if(contagem_maq4==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd4": 1}}}')
                    if(contagem_maq5==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 3)")
                        print('Adicionado Ciclo - BANCADA 3 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd5": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            elif("chd6" in str(ch)):
                try:
                    contagem_maq4 = ch['events']['chd4']['edge']
                    contagem_maq6 = ch['events']['chd6']['edge']
                    if(contagem_maq4==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd4": 1}}}')
                    if(contagem_maq6==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 4)")
                        print('Adicionado Ciclo - BANCADA 4 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd6": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            else:
                try:
                    contagem_maq4 = ch['events']['chd4']['edge']
                    #Dados da MÁQUINA - 4
                    if(contagem_maq4==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd4": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
        while ("chd5" in str(ch)):
            if ("chd1" in str(ch)):
                try:
                    contagem_maq1 = ch['events']['chd1']['edge']
                    contagem_maq5 = ch['events']['chd5']['edge']
                    if(contagem_maq1==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd1": 1}}}')
                    if(contagem_maq5==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 3)")
                        print('Adicionado Ciclo - BANCADA 3 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd5": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            elif ("chd2" in str(ch)):
                try:
                    contagem_maq2 = ch['events']['chd2']['edge']
                    contagem_maq5 = ch['events']['chd5']['edge']
                    if(contagem_maq2==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd2": 1}}}')
                    if(contagem_maq5==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 3)")
                        print('Adicionado Ciclo - BANCADA 3 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd5": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break  
            elif ("chd3" in str(ch)):
                try:
                    contagem_maq3 = ch['events']['chd3']['edge']
                    contagem_maq5 = ch['events']['chd5']['edge']
                    if(contagem_maq3==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd3": 1}}}')
                    if(contagem_maq5==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 3)")
                        print('Adicionado Ciclo - BANCADA 3 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd5": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break

            elif ("chd4" in str(ch)):
                try:
                    contagem_maq4 = ch['events']['chd4']['edge']
                    contagem_maq5 = ch['events']['chd5']['edge']
                    if(contagem_maq4==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd4": 1}}}')
                    if(contagem_maq5==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 3)")
                        print('Adicionado Ciclo - BANCADA 3 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd5": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            elif("chd6" in str(ch)):
                try:
                    contagem_maq5 = ch['events']['chd5']['edge']
                    contagem_maq6 = ch['events']['chd6']['edge']
                    if(contagem_maq5==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 3)")
                        print('Adicionado Ciclo - BANCADA 3 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd5": 1}}}')
                    if(contagem_maq6==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 4)")
                        print('Adicionado Ciclo - BANCADA 4 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd6": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            else:
                try:
                    contagem_maq5 = ch['events']['chd5']['edge']
                    #Dados da MÁQUINA - 5
                    if(contagem_maq5==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 3)")
                        print('Adicionado Ciclo - BANCADA 3 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd5": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
        while ("chd6" in str(ch)):
            if ("chd1" in str(ch)):
                try:
                    contagem_maq1 = ch['events']['chd1']['edge']
                    contagem_maq6 = ch['events']['chd6']['edge']
                    if(contagem_maq1==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd1": 1}}}')
                    if(contagem_maq6==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 4)")
                        print('Adicionado Ciclo - BANCADA 4 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd6": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            elif ("chd2" in str(ch)):
                try:
                    contagem_maq2 = ch['events']['chd2']['edge']
                    contagem_maq6 = ch['events']['chd6']['edge']
                    if(contagem_maq2==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 1)")
                        print('Adicionado Ciclo - BANCADA 1 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd2": 1}}}')
                    if(contagem_maq6==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 4)")
                        print('Adicionado Ciclo - BANCADA 4 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd6": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break  
            elif ("chd3" in str(ch)):
                try:
                    contagem_maq3 = ch['events']['chd3']['edge']
                    contagem_maq6 = ch['events']['chd6']['edge']
                    if(contagem_maq3==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd3": 1}}}')
                    if(contagem_maq6==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 4)")
                        print('Adicionado Ciclo - BANCADA 4 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd6": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break

            elif ("chd4" in str(ch)):
                try:
                    contagem_maq4 = ch['events']['chd4']['edge']
                    contagem_maq6 = ch['events']['chd6']['edge']
                    if(contagem_maq4==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 2)")
                        print('Adicionado Ciclo - BANCADA 2 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd4": 1}}}')
                    if(contagem_maq6==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 4)")
                        print('Adicionado Ciclo - BANCADA 4 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd6": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            elif("chd5" in str(ch)):
                try:
                    contagem_maq5 = ch['events']['chd5']['edge']
                    contagem_maq6 = ch['events']['chd6']['edge']
                    if(contagem_maq5==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 3)")
                        print('Adicionado Ciclo - BANCADA 3 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd5": 1}}}')
                    if(contagem_maq6==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 4)")
                        print('Adicionado Ciclo - BANCADA 4 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd6": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
            else:
                try:
                    contagem_maq6 = ch['events']['chd6']['edge']
                    #Dados da MÁQUINA - 5
                    if(contagem_maq6==0):
                        databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dtstring) +"','"+ str(dtstring) +"', 4)")
                        print('Adicionado Ciclo - BANCADA 4 - ' + str(dtstring))
                        client.publish("teste/teste/nvus", '{"timestamp":0,"desired": {"reset_counters" : {"reset_chd6": 1}}}')
                    break
                except:
                    print('Aguardando Mensagem ...')
                    break
                

    #Carrega na Variavel os dados recebidos no Tópico

    if msg.topic == "teste/teste/nvus":
        dado = str(msg.payload).split("'")
        t=str(dado[1])
        qtprod = t
        return qtprod

#Inicialização da Aplicação - LOOP FOREVER
   
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()

    
        









    
    
    