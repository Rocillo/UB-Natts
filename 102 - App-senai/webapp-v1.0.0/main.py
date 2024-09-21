import os
import flask
import bcrypt
import database
import flask_login
from datetime import datetime, time, timedelta
from flask import jsonify, request, redirect, url_for
import psycopg2
from datetime import datetime


######################################################## INIT ########################################################

#Flask configuration
versao=''
app = flask.Flask(__name__)
#app.secret_key = 'key'
app.secret_key = os.environ['SECRETKEY']
#Flask-Login configuration
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

#Database configuration
databaseOBJ=database.postgresDatabase(user=os.environ['DBUSER'], password=os.environ['DBPASSWORD'], host=os.environ['DBHOST'], dbname=os.environ['DBNAME'])
#databaseOBJ=database.postgresDatabase(host='localhost')

######################################################## AUTHENTICATION ####################################################

#Create class that extends default flask_login User Class
class User(flask_login.UserMixin):
    def __init__(self):
        super(User, self).__init__()
        self.name = ''
        self.privileges = 1

#Callback to check if current authenticated user is right
@login_manager.user_loader
def load_user(userid):
    global databaseOBJ
    #Check if user id exists and returns its object
    credentials = databaseOBJ.readRaw("select id, nome, privilegio from usuarios where id=" + userid + ";")
    if credentials != []:
        user = User()
        user.id = credentials[0][0]
        user.name = credentials[0][1]
        user.privileges = credentials[0][2]
        return user
    else:
        return None

#Callback to manage unauthorized acess
@login_manager.unauthorized_handler
def unauth_handler():
    #Redirect to index when user try to access protected resources without an authentication
    return flask.redirect(flask.url_for('autenticacao'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET' or flask.request.method == 'POST':
        global databaseOBJ
        form = flask.request.form
        user = str(form['user'])
        password = str(form['password'])
        if user !=None and password != None:
            #Check if user and password are right
            credentials = databaseOBJ.readRaw("select id, nome, privilegio, senha from usuarios where usuario='" + user + "';")
            if credentials != []:
                if bcrypt.checkpw(password.encode(), credentials[0][3].encode()):
                    #Login the user
                    user = User()
                    user.id = credentials[0][0]
                    user.name = credentials[0][1]
                    user.privileges = credentials[0][2]
                    flask_login.login_user(user)
                    return flask.make_response({'Login': True})
            #Don't Login the user
            return flask.make_response({'Login': False})
        else:
            return flask.abort(400)
    else:
        flask.abort(405)

@app.route('/logout', methods=['GET'])
def logout():
    #Logout current user
    flask_login.logout_user()
    return flask.make_response({'Logout': True})

######################################################## CRUD RESOURCES ####################################################

@app.route('/usuarios', methods=['GET', 'DELETE', 'PUT', 'POST'])
@flask_login.login_required
def usuarios():
    global databaseOBJ
    form = flask.request.form

    if flask.request.method == 'GET':
        return {'users': databaseOBJ.readRaw("select id, usuario, nome, setor, privilegio from usuarios order by id DESC;")}
    
    elif flask.request.method == 'DELETE':
        userid = form['id']
        if userid != None:
            databaseOBJ.writeRaw("delete from usuarios where id='" + userid + "';")
            print('Deleting user id: ' + userid)
            return flask.make_response({'deleted': 1})
        else: flask.abort(400)
    
    elif flask.request.method == 'PUT':
        userid = form['id']
        username = form['nome']
        usersector = form['setor']
        userprivileges = form['privilegios']
        if userid != None and username != None and usersector != None and userprivileges != None:
            databaseOBJ.writeRaw("update usuarios set (nome, setor, privilegio) = ('" + username + "', '" + usersector + "', " + userprivileges + ") where id=" + userid + ";")
            print('Updating user id: ' + userid + ' - ' + username + ' - ' + usersector + ' - Nível ' + userprivileges)
            return flask.make_response({'updated': 1})
        else: flask.abort(400)
    
    elif flask.request.method == 'POST':
        userlogin = form['usuario']
        username = form['nome']
        usersector = form['setor']
        userprivileges = form['privilegios']
        password = bcrypt.hashpw(userlogin.lower().encode(), bcrypt.gensalt())
        if userlogin != None and username != None and usersector != None and userprivileges != None:
            databaseOBJ.writeRaw("insert into usuarios(nome, setor, senha, usuario, privilegio ) values('" + username + "', '" + usersector + "', '" + password.decode() + "', '" + userlogin + "', " + userprivileges + ");")
            print('Creating user:' + userlogin + ' - ' + username + ' - ' + usersector + ' - Nível ' + userprivileges)
            return flask.make_response({'created': 1})
        else: flask.abort(400)
    
    else:
        flask.abort(405)

@app.route('/usuariodisponivel', methods=['GET'])
@flask_login.login_required
def usuariodisponivel():
    global databaseOBJ

    args = flask.request.args
    userlogin = str(args.get('usuario', default=''))

    if 'userlogin' != '': 
        query = databaseOBJ.readRaw("select * from usuarios where usuario='" + userlogin + "';")
        if len(query) == 0:
            return flask.make_response({'available': True})
        else:
            return flask.make_response({'available': False})
    else:
        return flask.abort(400)

@app.route('/mudarsenha', methods=['GET','PUT'])
@flask_login.login_required
def mudarsenha():
    global databaseOBJ
    form = flask.request.form
    userid = flask_login.current_user.get_id()
    currentPassword = form['currentPassword']
    newPassword = form['newPassword']

    if flask.request.method == 'GET' or flask.request.method == 'PUT':
        if currentPassword != None and newPassword != None:
            #Check if user typed right password
            password = databaseOBJ.readRaw("select senha from usuarios where id=" + userid + ";")[0][0]
            if bcrypt.checkpw(currentPassword.encode(), password.encode()):
                #Update user password
                newPassword = bcrypt.hashpw(newPassword.encode(), bcrypt.gensalt())
                print("Updating password from userid: " + userid)
                databaseOBJ.writeRaw("update usuarios set (senha) = row('" + newPassword.decode() + "') where id=" + userid + ";")
                return flask.make_response({'changeUserPassword': True})
            else:
                return flask.make_response({'changeUserPassword': False})
        else:
            flask.abort(400)
    else:
        flask.abort(405)

###########################################################################################

@app.route('/producao', methods=['GET', 'DELETE', 'PUT', 'POST'])
@flask_login.login_required
def producao():
    global databaseOBJ
    form = flask.request.form
    args = flask.request.args
         
    if flask.request.method == 'GET':
        id_maquina = str(args.get('id-maquina'))
        timebase = str(args.get('timebase', default='01 week'))
        return flask.make_response({'all': databaseOBJ.readRaw("select producao.id, maquina.nome, to_char(producao.dt_inicio, 'DD/MM/YY HH24:MI:SS'), \
                                                                to_char(producao.dt_fim, 'DD/MM/YY HH24:MI:SS'), producao.qtde_coletada,\
                                                                case when producao.estado=TRUE then 'Rodando' when producao.estado=FALSE then 'Parado' end,\
                                                                temp_refugo_total.total_refugo::int, to_char(temp_parada_total.total_parada, 'HH24:MI:SS'), usuarios.nome, maquina.id\
                                                                from producao inner join maquina on producao.id_maquina=maquina.id\
                                                                inner join usuarios on producao.id_usuario=usuarios.id\
                                                                inner join (select producao.id, sum(refugo.quantidade) as total_refugo from producao\
                                                                FULL OUTER JOIN refugo on refugo.id_producao=producao.id group by producao.id) as temp_refugo_total\
                                                                on temp_refugo_total.id=producao.id\
                                                                inner join (select producao.id, sum(parada.tempo) as total_parada from producao\
                                                                FULL OUTER JOIN parada on parada.id_producao=producao.id group by producao.id) as temp_parada_total\
                                                                on temp_parada_total.id=producao.id \
                                                                where producao.dt_inicio > (current_timestamp - '" + timebase + "'::interval) and producao.id_maquina = '" + id_maquina + "' order by producao.id DESC; "),
                                        'parada': databaseOBJ.readRaw("select case when parada.estado = true then 'parada' else 'funcionando' end as estado_parada \
                                                                from parada \
                                                                where parada.id_maquina = '" + id_maquina +"' and parada.estado = true order by parada.id DESC limit 1;")})
       
    elif flask.request.method == 'PUT':
        userid = flask_login.current_user.get_id()
        id_maquina = form['id_maquina']
        fim = form['finalizada']
        dt = datetime.now()
        dtstring = dt.strftime ('%Y/%m/%d %H:%M:%S')
        oee = "insert into oee(maquina, id_producao, dtoee, disponibilidade, perfomance, qualidade, oee)\
                select maquina.id as maquina, producao.id, producao.dt_inicio,\
                case when temp_parada_total.total_parada > '00:00:00' then (((extract(epoch from producao.dt_fim - producao.dt_inicio)/3600) - (extract(epoch from temp_parada_total.total_parada)/3600))/\
                (extract(epoch from producao.dt_fim - producao.dt_inicio)/3600))*100::real else '100'::real end disponibilidade,\
                case when qtde_coletada > 0 then (producao.qtde_coletada/((extract(epoch from producao.dt_fim - producao.dt_inicio - ((case when temp_parada_total.total_parada isnull then '0' else temp_parada_total.total_parada end)+ (case when temp_parada_programada_total.total_parada_programada isnull then '0' else temp_parada_programada_total.total_parada_programada end)))/3600) * producao.t_padrao))*100::real\
                else (0) end perfomance,\
                case when qtde_coletada > 0 then ((producao.qtde_coletada - coalesce (temp_refugo_total.total_refugo,0)) / producao.qtde_coletada)*100\
                else (0) end qualidade,\
                ((case when temp_parada_total.total_parada > '00:00:00' then (((extract(epoch from producao.dt_fim - producao.dt_inicio)/3600) - (extract(epoch from temp_parada_total.total_parada)/3600))/\
                (extract(epoch from producao.dt_fim - producao.dt_inicio)/3600))*100::real else '100'::real end)*\
                case when qtde_coletada > 0 then (producao.qtde_coletada/((extract(epoch from producao.dt_fim - producao.dt_inicio - ((case when temp_parada_total.total_parada isnull then '0' else temp_parada_total.total_parada end)+ (case when temp_parada_programada_total.total_parada_programada isnull then '0' else temp_parada_programada_total.total_parada_programada end)))/3600) * producao.t_padrao))*100::real\
                else (0) end *\
                (case when qtde_coletada > 0 then ((producao.qtde_coletada - coalesce (temp_refugo_total.total_refugo,0)) / producao.qtde_coletada)*100\
                else (0) end)/10000) as OEE\
                from producao inner join maquina on producao.id_maquina=maquina.id\
                inner join (select producao.id, sum(refugo.quantidade) as total_refugo from producao\
                FULL OUTER JOIN refugo on refugo.id_producao=producao.id group by producao.id) as temp_refugo_total\
                on temp_refugo_total.id=producao.id\
                inner join (select producao.id, sum(parada.tempo) as total_parada from producao\
                FULL OUTER JOIN parada on parada.id_producao=producao.id group by producao.id) as temp_parada_total\
                on temp_parada_total.id=producao.id\
                inner join (select producao.id, sum(parada_programada.tempo) as total_parada_programada from producao\
                FULL OUTER JOIN parada_programada on parada_programada.id_producao=producao.id group by producao.id) as temp_parada_programada_total \
                on temp_parada_programada_total.id=producao.id\
                where producao.estado = FALSE and producao.id_maquina= '" + id_maquina + "'\
                ON CONFLICT DO NOTHING" 

        if fim != None :
            qtde = databaseOBJ.readRaw("select count(*) from pecas where data_inicio>=(select dt_inicio from producao where id_maquina= '" + id_maquina +"' and producao.estado = true order by id DESC limit 1 ) and data_fim < '" + dtstring +"' ")
            pecasciclo = databaseOBJ.readRaw("select  p_ciclo  from producao where id_maquina= '" + id_maquina + "' and estado = true order by id DESC limit 1")
            coletado = str((qtde[0][0])*(pecasciclo[0][0]))
            databaseOBJ.writeRaw("  update producao SET (estado, qtde_coletada, id_usuario, dt_fim) = \
                                    (FALSE, '" + coletado +"','" + userid + "', '" + dtstring + "' ) from \
                                    (select id from producao where id_maquina= '" + id_maquina +"' order by id DESC limit 1) as subquery\
                                    where producao.id=subquery.id and estado=TRUE")
            databaseOBJ.writeRaw(oee)
            
            print('Updating Qtde: '+ coletado +' '  )
            return flask.make_response({'updated': 1})
                
        else: flask.abort(400)
   
    elif flask.request.method == 'POST':
        userid = flask_login.current_user.get_id()       
        id_maquina = form['id_maquina']
        liberacao = form['liberacao']
        dt = datetime.now()
        dtstring = dt.strftime ('%Y/%m/%d %H:%M:%S')
        id_produto = form['produto']
        lote = form['lote']
        ciclo = form['ciclo']
        tpadrao = form['tpadrao']
        if id_maquina != None:
            databaseOBJ.writeRaw(   "insert into producao(estado, id_maquina, id_usuario, dt_inicio, liberacao, id_produto, lote, t_padrao, p_ciclo) values(TRUE, " + 
                                    id_maquina + ", " + userid + ",'" + dtstring +"','" + liberacao +"','" + id_produto +"','" + lote +"','" + tpadrao +"','" + ciclo +"' );")
            return flask.make_response({'created': 1, 'datainicio': dtstring})
        else: flask.abort(400)
    
    else:
        flask.abort(405)

@app.route('/motivos', methods=['GET', 'DELETE', 'PUT', 'POST'])
@flask_login.login_required
def motivos():
    global databaseOBJ
    form = flask.request.form

    if flask.request.method == 'GET':
        return {'data': databaseOBJ.readRaw("select id, motivo, tipo from cadastro_motivos order by id DESC;")}
    
    elif flask.request.method == 'DELETE':
        motivo_id = form['id']
        if motivo_id != None:
            databaseOBJ.writeRaw("delete from cadastro_motivos where id='" + motivo_id + "';")
            print('Deleting motivo id: ' + motivo_id)
            return flask.make_response({'deleted': 1})
        else: flask.abort(400)
    
    elif flask.request.method == 'PUT':
        motivo_id = form['id']
        motivo = form['motivo']
        tipo = form['tipo']

        if motivo_id != None and motivo != None and tipo != None:
            databaseOBJ.writeRaw("update cadastro_motivos set (motivo, tipo) = ('" + motivo + "', '" + tipo + "') where id=" + motivo_id + ";")
            print('Updating motivo id: ' + motivo_id + ' - ' + motivo + ' - ' + tipo)
            return flask.make_response({'updated': 1})
        else: flask.abort(400)
    
    elif flask.request.method == 'POST':
        motivo = form['motivo']
        tipo = form['tipo']
        if motivo != None and tipo != None:
            databaseOBJ.writeRaw("insert into cadastro_motivos(motivo, tipo) values('" + motivo + "', '" + tipo + "');")
            print('Creating motivo:' + motivo + ' - ' + tipo)
            return flask.make_response({'created': 1})
        else: flask.abort(400)
    
    else:
        flask.abort(405)

@app.route('/componentes', methods=['GET', 'DELETE', 'PUT', 'POST'])
@flask_login.login_required
def componente():
    global databaseOBJ
    form = flask.request.form

    if flask.request.method == 'GET':
        return {'data': databaseOBJ.readRaw("select id, cod, descricao from componentes order by id DESC;")}
    
    elif flask.request.method == 'DELETE':
        motivo_id = form['id']
        if motivo_id != None:
            databaseOBJ.writeRaw("delete from componentes where id='" + motivo_id + "';")
            print('Deleting componente id: ' + motivo_id)
            return flask.make_response({'deleted': 1})
        else: flask.abort(400)
    
    elif flask.request.method == 'PUT':
        motivo_id = form['id']
        motivo = form['motivo']
        tipo = form['tipo']

        if motivo_id != None and motivo != None and tipo != None:
            databaseOBJ.writeRaw("update componentes set (cod, descricao) = ('" + motivo + "', '" + tipo + "') where id=" + motivo_id + ";")
            print('Updating componente id: ' + motivo_id + ' - ' + motivo + ' - ' + tipo)
            return flask.make_response({'updated': 1})
        else: flask.abort(400)
    
    elif flask.request.method == 'POST':
        motivo = form['motivo']
        tipo = form['tipo']
        if motivo != None and tipo != None:
            databaseOBJ.writeRaw("insert into componentes(cod, descricao) values('" + motivo + "', '" + tipo + "');")
            print('Creating componente:' + motivo + ' - ' + tipo)
            return flask.make_response({'created': 1})
        else: flask.abort(400)
    
    else:
        flask.abort(405)

@app.route('/produtos', methods=['GET', 'DELETE', 'PUT', 'POST'])
@flask_login.login_required
def produtos():
    global databaseOBJ
    form = flask.request.form

    if flask.request.method == 'GET':
        return {'data': databaseOBJ.readRaw("select id, nome, pecas_ciclo, t_padrao from produtos order by id DESC;")}
    
    elif flask.request.method == 'DELETE':
        motivo_id = form['id']
        if motivo_id != None:
            databaseOBJ.writeRaw("delete from produtos where id='" + motivo_id + "';")
            print('Deleting componente id: ' + motivo_id)
            return flask.make_response({'deleted': 1})
        else: flask.abort(400)
    
    elif flask.request.method == 'PUT':
        id = form['id']
        nome = form['nome']
        ciclo = form['ciclo']
        phora = form['phora']
        if id != None and nome != None and ciclo != None and phora != None:
            databaseOBJ.writeRaw("update produtos set (nome, pecas_ciclo, t_padrao) = ('" + nome + "', '" + ciclo + "', '" + phora + "') where id=" + id + ";")
            print('Updating componente id: ' + id + ' - ' + nome + ' - ' + ciclo + ' - ' + phora)
            return flask.make_response({'updated': 1})
        else: flask.abort(400)
    
    elif flask.request.method == 'POST':
        nome = form['nome']
        ciclo = form['ciclo']
        phora = form['phora']

        if nome != None and ciclo != None and phora != None:
            databaseOBJ.writeRaw("insert into produtos(nome, pecas_ciclo, t_padrao) values('" + nome + "', '" + ciclo + "', '" + phora + "');")
            print('Creating produto:' + nome + ' - ' + ciclo + ' - ' + phora)
            return flask.make_response({'created': 1})
        else: flask.abort(400)
    
    else:
        flask.abort(405)

@app.route('/refugo', methods=['GET', 'DELETE', 'POST'])
@flask_login.login_required
def refugo():
    global databaseOBJ
    form = flask.request.form
    args = flask.request.args

    if flask.request.method == 'GET':
        
        timebase = str(args.get('timebase', default='01 day'))
        id_maquina = str(args.get('id-maquina'))
        return {'data': databaseOBJ.readRaw("select refugo.id, componentes.descricao, cadastro_motivos.motivo,  refugo.quantidade, \
                                            to_char(refugo.data, 'DD/MM/YY HH24:MI:SS'),  justificativa \
                                            from refugo inner join cadastro_motivos on refugo.id_motivo=cadastro_motivos.id \
                                            inner join maquina on maquina.id=refugo.id_maquina\
                                            inner join componentes on componentes.id=refugo.id_componente\
                                            where refugo.data > (current_timestamp - '" + timebase + "'::interval) and refugo.id_maquina = '" + id_maquina + "' order by refugo.id DESC;")}
    
    elif flask.request.method == 'DELETE':
        refugo_id = form['id']
        if refugo_id != None:
            databaseOBJ.writeRaw("delete from refugo where id='" + refugo_id + "';")
            print('Deleting refugo id: ' + refugo_id)
            return flask.make_response({'deleted': 1})
        else: flask.abort(400)
    
    elif flask.request.method == 'POST':
        userid = flask_login.current_user.get_id()
        id_maquina = form['id_maquina']
        id_motivo = form['id_motivo']
        id_componente = form['id_componente']
        qtde_refugo = form['qtde_refugo']
        justificativa = form['justificativa']
        dt = datetime.now()
        dtstring = dt.strftime ('%Y/%m/%d %H:%M')
        if id_maquina != None and id_motivo != None and qtde_refugo != None:
            databaseOBJ.writeRaw("  insert into refugo(id_producao, id_motivo, quantidade, id_usuario, id_maquina, id_componente, justificativa, data) \
                                    select id, '" + id_motivo + "', '" + qtde_refugo + "', '" + userid + "', id_maquina, '" + id_componente + "' , '" + justificativa + "' ,  '" + dtstring + "' from producao \
                                    where estado=TRUE and id_maquina ='" + id_maquina + "';")
            
            print('Creating refugo: ' + id_maquina + ' - ' + id_motivo + ' - ' + qtde_refugo)
            return flask.make_response({'created': 1})
        else: flask.abort(400)
    
    else:
        flask.abort(405)

@app.route('/parada', methods=['GET', 'DELETE', 'POST', 'PUT'])
@flask_login.login_required
def parada():
    global databaseOBJ
    form = flask.request.form
    args = flask.request.args

    if flask.request.method == 'GET':
        dt = datetime.now()
        dtstring = dt.strftime ('%Y/%m/%d %H:%M:%S')
        timebase = str(args.get('timebase', default='01 day'))
        id_maquina = str(args.get('id-maquina'))
        return {'data': databaseOBJ.readRaw("select parada.id, cadastro_motivos.motivo, \
                                            to_char(parada.inicio_parada  , 'DD/MM/YY HH24:MI:SS'),  \
                                            to_char('" + dtstring + "' - parada.inicio_parada  , 'HH24:MI:SS') \
                                            from parada inner join cadastro_motivos on parada.id_motivo=cadastro_motivos.id \
                                            inner join maquina on maquina.id=parada.id_maquina \
                                            where parada.inicio_parada > (current_timestamp - '01 day'::interval) and parada.estado = TRUE and parada.id_maquina = '" + id_maquina +"' order by parada.id DESC limit 1;")}
    
    elif flask.request.method == 'DELETE':
        parada_id = form['id']
        if parada_id != None:
            databaseOBJ.writeRaw("delete from parada where id='" + parada_id + "';")
            print('Deleting parada id: ' + parada_id)
            return flask.make_response({'deleted': 1})
        else: flask.abort(400)
    
    elif flask.request.method == 'POST':
        userid = flask_login.current_user.get_id()
        id_maquina = form['id_maquina']
        id_motivo = form['id_motivo']
        dt = datetime.now()
        dtstring = dt.strftime ('%Y/%m/%d %H:%M:%S')
        if id_maquina != None and id_motivo != None:
            databaseOBJ.writeRaw("  insert into parada(id_producao, id_motivo, id_usuario, id_maquina, inicio_parada, estado) \
                                    select id, '" + id_motivo + "', '" + userid + "', id_maquina,  '"+ dtstring +"', TRUE from producao \
                                    where estado=TRUE and id_maquina ='" + id_maquina + "';")
            
            print('Creating parada: ' + id_maquina + ' - ' + id_motivo + ' - ' + dtstring)
            return flask.make_response({'created': 1})
        else: flask.abort(400)

    elif flask.request.method == 'PUT':
        userid = flask_login.current_user.get_id()
        justificativa = form['justificativa']
        id_maquina = form['id_maquina']
        dt = datetime.now()
        dtstring = dt.strftime ('%Y/%m/%d %H:%M:%S')

        if justificativa != None :
            
            databaseOBJ.writeRaw("  update parada SET (estado, fim_parada, justificativa, tempo) = \
                                    (FALSE, '" + dtstring +"','" + justificativa + "', ('" + dtstring +"' - inicio_parada)) from \
                                    (select id from parada where id_maquina= '" + id_maquina +"' order by id DESC limit 1) as subquery\
                                    where parada.id=subquery.id and estado=TRUE")
            
            print('Finalizada parada')
            return flask.make_response({'updated': 1})
                
        else: flask.abort(400)

    else:
        flask.abort(405)

@app.route('/parada-fim', methods=['GET'])
@flask_login.login_required
def parada_fim():
    global databaseOBJ
    form = flask.request.form
    args = flask.request.args

    if flask.request.method == 'GET':
        dt = datetime.now()
        dtstring = dt.strftime ('%Y/%m/%d %H:%M:%S')
        id_maquina = str(args.get('id-maquina'))
        return {'data': databaseOBJ.readRaw("select parada.id, cadastro_motivos.motivo, \
                                            to_char(parada.inicio_parada  , 'DD/MM/YY HH24:MI:SS'),  \
                                            to_char(parada.fim_parada  , 'DD/MM/YY HH24:MI:SS'), \
                                            to_char(parada.fim_parada  - parada.inicio_parada  , 'HH24:MI:SS'), \
                                            justificativa\
                                            from parada inner join cadastro_motivos on parada.id_motivo=cadastro_motivos.id \
                                            inner join maquina on maquina.id=parada.id_maquina \
                                            where parada.inicio_parada > (current_timestamp - '01 day'::interval) and parada.estado = FALSE and parada.id_maquina='" + id_maquina + "' order by parada.id DESC;")}

@app.route('/tabelahistorico', methods=['GET'])
@flask_login.login_required
def tabelahistorico():
    global databaseOBJ
    form = flask.request.form
    args = flask.request.args
         
    if flask.request.method == 'GET':
        dt_inicio = str(args.get('inicial', default='today'))
        dt_fim = str(args.get('final', default='tomorrow'))
        return flask.make_response({'all': databaseOBJ.readRaw("select producao.id, maquina.nome, to_char(producao.dt_inicio, 'DD/MM/YY HH24:MI:SS'), \
                                                                to_char(producao.dt_fim, 'DD/MM/YY HH24:MI:SS'), producao.qtde_coletada,\
                                                                case when producao.estado=TRUE then 'Rodando' when producao.estado=FALSE then 'Parado' end, \
                                                                coalesce (temp_refugo_total.total_refugo::int, 0), coalesce (to_char(temp_parada_total.total_parada, 'HH24:MI:SS'),'00:00:00')\
                                                                from producao inner join maquina on producao.id_maquina=maquina.id \
                                                                inner join usuarios on producao.id_usuario=usuarios.id \
                                                                inner join (select producao.id, sum(refugo.quantidade) as total_refugo from producao \
                                                                FULL OUTER JOIN refugo on refugo.id_producao=producao.id group by producao.id) as temp_refugo_total \
                                                                on temp_refugo_total.id=producao.id\
                                                                inner join (select producao.id, sum(parada.tempo) as total_parada from producao \
                                                                FULL OUTER JOIN parada on parada.id_producao=producao.id group by producao.id) as temp_parada_total \
                                                                on temp_parada_total.id=producao.id\
                                                                where producao.dt_inicio >= '"+dt_inicio +"' and producao.dt_inicio <= '"+ dt_fim + "' order by producao.id DESC; ")})

@app.route('/dadosoee', methods=['GET'])
def dados_oee1():
    global databaseOBJ
    args = flask.request.args
    dt = datetime.now()
    dtstring = dt.strftime ('%Y/%m/%d %H:%M:%S')
    dia = dt.strftime ('%Y-%m-%d')

    if flask.request.method == 'GET':
        id_maquina = str(args.get('id-maquina'))

        qtde = databaseOBJ.readRaw("select count(*) from pecas where data_inicio>=(select dt_inicio from producao where id_maquina='" + id_maquina + "' and producao.estado = true order by id DESC limit 1 ) and data_fim < '" + dtstring +"' and id_maquina ='" + id_maquina + "' ")
        coletado = str(qtde[0][0])

        st1 = databaseOBJ.readRaw("select case when producao.estado = TRUE then '1'WHEN producao.estado = FALSE then '0' END,\
                        to_char((extract(epoch from '" + dtstring + "' - producao.dt_inicio - ((case when temp_parada_total.total_parada isnull then '0' else temp_parada_total.total_parada end)+ (case when temp_parada_programada_total.total_parada_programada isnull then '0' else temp_parada_programada_total.total_parada_programada end)))/3600), '990.9999') as intervalo,\
                        coalesce (temp_refugo_total.total_refugo::int,'0') as Refugo, temp_parada_total.total_parada,\
                        to_char(case when temp_parada_total.total_parada > '00:00:00' then (((extract(epoch from '" + dtstring + "' - producao.dt_inicio)/3600) - (extract(epoch from temp_parada_total.total_parada)/3600))/\
                        (extract(epoch from '" + dtstring + "' - producao.dt_inicio)/3600))*100::real else '100'::real end, '990.00') disponibilidade,\
                        to_char(producao.dt_inicio, 'YYYY-MM-DD HH24:MI:SS'), producao.id, to_char(producao.dt_inicio, 'DD/MM/YYYY HH24 : MI : SS'), t_padrao, p_ciclo\
                        from producao inner join maquina on producao.id_maquina=maquina.id \
                        inner join usuarios on producao.id_usuario=usuarios.id \
                        inner join (select producao.id, sum(refugo.quantidade) as total_refugo from producao\
                        FULL OUTER JOIN refugo on refugo.id_producao=producao.id group by producao.id) as temp_refugo_total\
                        on temp_refugo_total.id=producao.id\
                        inner join (select producao.id, sum(parada.tempo) as total_parada from producao\
                        FULL OUTER JOIN parada on parada.id_producao=producao.id group by producao.id) as temp_parada_total\
                        on temp_parada_total.id=producao.id\
                        inner join (select producao.id, sum(parada_programada.tempo) as total_parada_programada from producao \
                        FULL OUTER JOIN parada_programada on parada_programada.id_producao=producao.id group by producao.id) as temp_parada_programada_total \
                        on temp_parada_programada_total.id=producao.id\
                        where id_maquina = '" + id_maquina + "' and producao.estado = true order by producao.id desc limit 1")

        estado = databaseOBJ.readRaw("select case when parada.estado = true then 'parada' else 'funcionando' end as estado_parada, cadastro_motivos.motivo, \
                                                                to_char((EXTRACT(EPOCH from ('" + dtstring + "' - parada.inicio_parada ))/60),'990.0')\
                                                                from parada inner join cadastro_motivos on cadastro_motivos.id = parada.id_motivo \
                                                                where parada.id_maquina = '" + id_maquina +"' and parada.estado = true order by parada.id DESC limit 1;")

        turn1 = databaseOBJ.readRaw("select count(*) from pecas where data_inicio > '" + dia + " 06:05:00' and data_inicio <= '" + dia + " 07:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + dia + " 07:00:00' and data_inicio <= '" + dia + " 08:00:00' and id_maquina = '" + id_maquina + "' \
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + dia + " 08:00:00' and data_inicio <= '" + dia + " 09:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + dia + " 09:00:00' and data_inicio <= '" + dia + " 10:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + dia + " 10:00:00' and data_inicio <= '" + dia + " 11:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + dia + " 11:00:00' and data_inicio <= '" + dia + " 12:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + dia + " 12:00:00' and data_inicio <= '" + dia + " 13:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + dia + " 13:00:00' and data_inicio <= '" + dia + " 14:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + dia + " 14:00:00' and data_inicio <= '" + dia + " 15:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + dia + " 15:00:00' and data_inicio <= '" + dia + " 15:48:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + dia + " 18:30:00' and data_inicio <= '" + dia + " 19:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + dia + " 19:00:00' and data_inicio <= '" + dia + " 20:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + dia + " 20:00:00' and data_inicio <= '" + dia + " 21:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + dia + " 21:00:00' and data_inicio <= '" + dia + " 22:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + dia + " 22:00:00' and data_inicio <= '" + dia + " 23:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + dia + " 23:00:00' and data_inicio <= '" + dia + " 00:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + dia + " 00:00:00' and data_inicio <= '" + dia + " 01:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + dia + " 01:00:00' and data_inicio <= '" + dia + " 02:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + dia + " 02:00:00' and data_inicio <= '" + dia + " 03:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + dia + " 03:00:00' and data_inicio <= '" + dia + " 03:42:00' and id_maquina = '" + id_maquina + "'\
                                    ")

        # calculo maquina 1
        try:
            estado1 =st1[0][0]
        except IndexError:
            estado1 = '0'
        
        if estado1=='1':
            qtprod1=int(coletado)*int(st1[0][9])
            pefm1 = (float(qtprod1))/(st1[0][8]*float(st1[0][1]))*100
            pfv1=str("{:4.1f}".format(pefm1))
            if float(qtprod1) > 0:
                qual1 = str("{:4.1f}".format ((((float(qtprod1))-(float(st1[0][2])))/float(qtprod1))*100))
            else:
                qual1 = '0.0'

            disp1=str("{:4.1f}".format(float(st1[0][4])))
            oee1=str("{:.0f}".format((((float(pfv1))*(float(qual1)))*(float(st1[0][4])))/10000))
            prodp1=st1[0][8]
            dtinicio=st1[0][5]
            opinicio=st1[0][7]

            qtde_refugo = databaseOBJ.readRaw("select to_char(sum(quantidade),'900') from refugo\
                                            where data>= '" + dtinicio +"'and data < (date '" + dtinicio +"' + interval '01 day') and id_maquina = '" + id_maquina + "'\
                                            ")
        
            qtde_parada = databaseOBJ.readRaw("select to_char((EXTRACT(EPOCH from sum(tempo))/60),'900.0') from parada\
                                        where inicio_parada>= '" + dtinicio +"'and inicio_parada < (date '" + dtinicio +"' + interval '01 day') and id_maquina = '" + id_maquina + "'\
                                        ")
            
            try:
                parada = estado[0][0]
                motivo = str(estado[0][1])
                periodo = str(estado[0][2])
            except IndexError:
                parada = 'funcionando'
                motivo = ''
                periodo = ''

        else:
            qtprod1='Parada'
            pfv1=''
            disp1=''
            qual1=''
            oee1='Parada'
            prodp1='-'
            dtinicio=''
            opinicio=''
            qtde_refugo=0
            qtde_parada=0
            parada = ''
            motivo = ''
            periodo = ''
        
        return flask.make_response({"all": [[str(qtprod1), (pfv1), (disp1), (qual1), (oee1), str(estado1), (prodp1), (turn1), (dtinicio), (qtde_refugo), (qtde_parada), (opinicio), str(parada), str(motivo), str(periodo)]]})

@app.route('/relatoriooee', methods=['GET'])
def relatorio_oee1():
    global databaseOBJ
    args = flask.request.args
    form = flask.request.form
    dt = datetime.now()
    dtstring = dt.strftime ('%Y/%m/%d %H:%M:%S')

    if flask.request.method == 'GET':
        timebase = str(args.get('base-tempo', default='today'))
        id_maquina = str(args.get('id-maquina'))
        date = datetime.strptime(timebase, "%Y-%m-%d")
        modified_date = date + timedelta(days=1, hours=6, minutes=42)
        inicio = str(timebase + ' 06:00:00')
        final_turno = str(modified_date)

        oee=databaseOBJ.readRaw("select to_char(avg(disponibilidade),'999.9'), to_char(avg(perfomance),'999.9'), to_char(avg(qualidade),'999.9'), to_char(avg(oee),'990.9 %') from oee\
                                WHERE dtoee > '" + inicio +"' AND dtoee <='" + final_turno +"' and maquina = '" + id_maquina + "' ")

        qtde = databaseOBJ.readRaw("select count(*) from pecas where data_inicio>='" + timebase +"' and data_fim < (date '" + timebase +"' + interval '01 day') and id_maquina = '" + id_maquina + "' ")
        #pecasciclo = databaseOBJ.readRaw("select  p_ciclo, t_padrao  from producao where dt_inicio>='" + timebase +"' and dt_fim < (date '" + timebase +"' + interval '01 day') id DESC limit 1")
        coletado = str((qtde[0][0]))

        qtde_refugo = databaseOBJ.readRaw("select to_char(sum(quantidade),'900') from refugo\
                                            where data>= '" + timebase +"'and data < (date '" + timebase +"' + interval '01 day') and id_maquina = '" + id_maquina + "'\
                                            ")
        
        qtde_parada = databaseOBJ.readRaw("select to_char((EXTRACT(EPOCH from sum(tempo))/60),'990.0') from parada\
                                        where inicio_parada>= '" + timebase +"'and inicio_parada < (date '" + timebase +"' + interval '01 day') and id_maquina = '" + id_maquina + "'\
                                        ")

        turn1 = databaseOBJ.readRaw("select count(*) from pecas where data_inicio > '" + timebase +" 06:00:00' and data_inicio <= '" + timebase +" 07:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + timebase +" 07:00:00' and data_inicio <= '" + timebase +" 08:00:00' and id_maquina = '" + id_maquina + "' \
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + timebase +" 08:00:00' and data_inicio <= '" + timebase +" 09:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + timebase +" 09:00:00' and data_inicio <= '" + timebase +" 10:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + timebase +" 10:00:00' and data_inicio <= '" + timebase +" 11:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + timebase +" 11:00:00' and data_inicio <= '" + timebase +" 12:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + timebase +" 12:00:00' and data_inicio <= '" + timebase +" 13:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + timebase +" 13:00:00' and data_inicio <= '" + timebase +" 14:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + timebase +" 14:00:00' and data_inicio <= '" + timebase +" 15:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + timebase +" 15:00:00' and data_inicio <= '" + timebase +" 15:48:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + timebase +" 18:30:00' and data_inicio <= '" + timebase +" 19:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + timebase +" 19:00:00' and data_inicio <= '" + timebase +" 20:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + timebase +" 20:00:00' and data_inicio <= '" + timebase +" 21:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + timebase +" 21:00:00' and data_inicio <= '" + timebase +" 22:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + timebase +" 22:00:00' and data_inicio <= '" + timebase +" 23:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + timebase +" 23:00:00' and data_inicio <= '" + timebase +" 00:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + timebase +" 00:00:00' and data_inicio <= '" + timebase +" 01:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + timebase +" 01:00:00' and data_inicio <= '" + timebase +" 02:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + timebase +" 02:00:00' and data_inicio <= '" + timebase +" 03:00:00' and id_maquina = '" + id_maquina + "'\
                                    union all\
                                    select count(*) from pecas where data_inicio > '" + timebase +" 03:00:00' and data_inicio <= '" + timebase +" 03:42:00' and id_maquina = '" + id_maquina + "'\
                                    ")

        return flask.make_response({"all": [[coletado,(oee[0][3]),(oee[0][0]),(oee[0][1]),(oee[0][2]), turn1, qtde_refugo, qtde_parada ]]})

@app.route('/relatorio-takt', methods=['GET'])
def relatorio_takt():
    global databaseOBJ

    args = flask.request.args
    form = flask.request.form

    if flask.request.method == 'GET':
        timebase = str(args.get('base-tempo', default='today'))
        id_maquina = str(args.get('id-maquina'))
        result = {
                        'ciclo': databaseOBJ.readRaw("select extract(epoch from(data_fim - data_inicio)) as y, id as t from pecas where data_inicio >'" + timebase +"' and id_maquina = '" + id_maquina + "' order by id DESC limit 20 ;",realdict=True),
                        'media': databaseOBJ.readRaw("select to_char(avg(extract(epoch from(data_fim - data_inicio))),'9999.9') from pecas where data_inicio >'" + timebase +"' and id_maquina = '" + id_maquina + "' limit 20;", realdict=False) 
                }
        result_dict = result
    return flask.make_response(result_dict)

@app.route('/relatorio-parada', methods=['GET'])
def relatorio_parada():
    global databaseOBJ

    args = flask.request.args
    form = flask.request.form

    if flask.request.method == 'GET':
        timebase = str(args.get('base-tempo', default='today'))
        id_maquina = str(args.get('id-maquina'))
        result = {
                        'tempo': databaseOBJ.readRaw("select to_char((EXTRACT(EPOCH from sum(tempo))/60),'990.0') from parada\
                                        inner join cadastro_motivos  on parada.id_motivo=cadastro_motivos.id\
                                        where inicio_parada >= '" + timebase +"'and inicio_parada  < (date '" + timebase +"' + interval '01 day') and id_maquina = '" + id_maquina + "'\
                                        group by cadastro_motivos.id",realdict=False),
                        'motivo': databaseOBJ.readRaw("select cadastro_motivos.motivo from parada\
                                        inner join cadastro_motivos  on parada.id_motivo=cadastro_motivos.id\
                                        where inicio_parada >= '" + timebase +"'and inicio_parada  < (date '" + timebase +"' + interval '01 day') and id_maquina = '" + id_maquina + "'\
                                        group by cadastro_motivos.id",realdict=False)
                }
        result_dict = result
    return flask.make_response(result_dict)

@app.route('/relatorio-refugo', methods=['GET'])
def relatorio_refugo():
    global databaseOBJ

    args = flask.request.args
    form = flask.request.form

    if flask.request.method == 'GET':
        timebase = str(args.get('base-tempo', default='today'))
        id_maquina = str(args.get('id-maquina'))
        result = {
                        'refugos': databaseOBJ.readRaw("select to_char(sum(quantidade),'900') from refugo\
                                        inner join cadastro_motivos  on refugo.id_motivo=cadastro_motivos.id\
                                        where data>='" + timebase +"' and data < (date '" + timebase +"' + interval '01 day') and id_maquina = '" + id_maquina + "'\
                                        group by cadastro_motivos.id",realdict=False),
                        'motivo': databaseOBJ.readRaw("select cadastro_motivos.motivo from refugo\
                                        inner join cadastro_motivos  on refugo.id_motivo=cadastro_motivos.id\
                                        where data>='" + timebase +"' and data < (date '" + timebase +"' + interval '01 day') and id_maquina = '" + id_maquina + "'\
                                        group by cadastro_motivos.id",realdict=False)
                }
        result_dict = result
    return flask.make_response(result_dict)

######################################################## VIEWS ########################################################
@app.route('/autenticacao', methods=['GET'])
def autenticacao():
    if flask_login.current_user.is_authenticated:
        return flask.redirect(flask.url_for('index'))
    else:
        return flask.render_template('autenticacao.html')


@app.route('/cadastro_producao_1')
@flask_login.login_required
def cadastro_producao_1():
    global databaseOBJ
    machine_names = databaseOBJ.readRaw("select id, nome, fabricante, ano from maquina where id > 0 and id < 9 order by id asc;")
    motivos = databaseOBJ.readRaw("select id, tipo, motivo from cadastro_motivos order by id ASC;")
    componentes = databaseOBJ.readRaw("select id, cod, descricao from componentes order by id ASC;")
    produtos = databaseOBJ.readRaw("select id, nome, pecas_ciclo, t_padrao from produtos order by id ASC;")

    return flask.render_template('producao_1.html', machine_names=machine_names, motivos=motivos, componentes=componentes, produtos=produtos)

@app.route('/cadastro_producao_2')
@flask_login.login_required
def cadastro_producao_2():
    global databaseOBJ
    machine_names = databaseOBJ.readRaw("select id, nome, fabricante, ano from maquina where id > 0 and id < 9 order by id asc;")
    motivos = databaseOBJ.readRaw("select id, tipo, motivo from cadastro_motivos order by id ASC;")
    componentes = databaseOBJ.readRaw("select id, cod, descricao from componentes order by id ASC;")
    produtos = databaseOBJ.readRaw("select id, nome, pecas_ciclo, t_padrao from produtos order by id ASC;")

    return flask.render_template('producao_2.html', machine_names=machine_names, motivos=motivos, componentes=componentes, produtos=produtos)

@app.route('/cadastro_producao_3')
@flask_login.login_required
def cadastro_producao_3():
    global databaseOBJ
    machine_names = databaseOBJ.readRaw("select id, nome, fabricante, ano from maquina where id > 0 and id < 9 order by id asc;")
    motivos = databaseOBJ.readRaw("select id, tipo, motivo from cadastro_motivos order by id ASC;")
    componentes = databaseOBJ.readRaw("select id, cod, descricao from componentes order by id ASC;")
    produtos = databaseOBJ.readRaw("select id, nome, pecas_ciclo, t_padrao from produtos order by id ASC;")

    return flask.render_template('producao_3.html', machine_names=machine_names, motivos=motivos, componentes=componentes, produtos=produtos)

@app.route('/cadastro_motivos')
@flask_login.login_required
def cadastro_motivos():
    global databaseOBJ
    machine_names = databaseOBJ.readRaw("select id, nome, fabricante, ano from maquina where id>0 and id <9 order by id ASC;")
    return flask.render_template('cadastro.html', machine_names=machine_names)

@app.route('/cadastro_produtos')
@flask_login.login_required
def cadastro_produtos():
    global databaseOBJ
    machine_names = databaseOBJ.readRaw("select id, nome, fabricante, ano from maquina where id>0 and id <9 order by id ASC;")
    return flask.render_template('cadastro_produtos.html', machine_names=machine_names)

@app.route('/cadastro_componentes')
@flask_login.login_required
def cadastro_componentes():
    global databaseOBJ
    machine_names = databaseOBJ.readRaw("select id, nome, fabricante, ano from maquina where id>0 and id <9 order by id ASC;")

    return flask.render_template('cadastro_componentes.html', machine_names=machine_names)

@app.route('/cadastro_moldes')
@flask_login.login_required
def cadastro_moldes():
    return flask.render_template('moldes.html')

################################ Render - monitoramento ################################################

@app.route('/monitoramento_1')
@flask_login.login_required
def monitoramento_1():
    global databaseOBJ
    machine_names = databaseOBJ.readRaw("select id, nome, fabricante, ano from maquina where id>0 and id <9 order by id ASC;")

    return flask.render_template('monitoramento_1.html', machine_names=machine_names)

@app.route('/monitoramento_2')
@flask_login.login_required
def monitoramento_2():
    global databaseOBJ
    machine_names = databaseOBJ.readRaw("select id, nome, fabricante, ano from maquina where id>0 and id <9 order by id ASC;")

    return flask.render_template('monitoramento_2.html', machine_names=machine_names)

@app.route('/monitoramento_3')
@flask_login.login_required
def monitoramento_3():
    global databaseOBJ
    machine_names = databaseOBJ.readRaw("select id, nome, fabricante, ano from maquina where id>0 and id <9 order by id ASC;")

    return flask.render_template('monitoramento_3.html', machine_names=machine_names)

@app.route('/monitoramento_geral')
@flask_login.login_required
def monitoramento_geral():
    global databaseOBJ
    machine_names = databaseOBJ.readRaw("select id, nome, fabricante, ano from maquina where id>0 and id <9 order by id ASC;")

    return flask.render_template('monitoramento_geral.html', machine_names=machine_names)

@app.route('/cadastro_usuarios')
@flask_login.login_required
def cadastro_usuarios():
    global databaseOBJ
    machine_names = databaseOBJ.readRaw("select id, nome from maquina where id >0 and id <9 order by id ASC;")

    return flask.render_template('usuarios.html', machine_names=machine_names)

@app.route('/relatorio')
@flask_login.login_required
def relatorio():
    global databaseOBJ

    machine_names = databaseOBJ.readRaw("select id, nome from maquina where id >0 and id <9 order by id ASC;")

    return flask.render_template('relatorio.html', machine_names= machine_names)

@app.route('/historico')
@flask_login.login_required
def historico():
    machine_names = databaseOBJ.readRaw("select id, nome, fabricante, ano from maquina where id>0 and id <9 order by id ASC;")
    return flask.render_template('historico.html', machine_names=machine_names)

# Database connection parameters
DB_HOST = 'localhost'
DB_NAME = 'ub_natts'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'

# Connect to the PostgreSQL database
def connect_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

# Fetch workstation status
def fetch_workstation_status():
    conn = connect_db()
    if not conn:
        return []

    cursor = conn.cursor()
    try:
        query = """
        SELECT w.workstation_id, w.name AS workstation_name,
               op.name AS operator_name, ws.start_time, ws.end_time,
               CASE WHEN ws.end_time IS NULL THEN true ELSE false END AS active
        FROM Workstations w
        LEFT JOIN WorkSessions ws ON w.workstation_id = ws.workstation_id AND ws.is_done = FALSE
        LEFT JOIN Operators op ON ws.operator_id = op.operator_id
        WHERE ws.is_done = FALSE
        ORDER BY w.workstation_id;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append({
                'workstation_id': row[0],
                'workstation_name': row[1],
                'operator_name': row[2] if row[2] else 'None',
                'start_time': row[3].strftime('%Y-%m-%d %H:%M:%S') if row[3] else 'N/A',
                'active': row[5]
            })
        return result
    except Exception as e:
        print(f"Error fetching workstation status: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

# Fetch all workstations
def fetch_all_workstations():
    conn = connect_db()
    if not conn:
        return []
    
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Workstations")
        workstations = cursor.fetchall()
        return workstations
    except Exception as e:
        print(f"Error fetching workstations: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

# Fetch a single workstation by ID
def fetch_workstation_by_id(workstation_id):
    conn = connect_db()
    if not conn:
        return None
    
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Workstations WHERE workstation_id = %s", (workstation_id,))
        workstation = cursor.fetchone()
        return workstation
    except Exception as e:
        print(f"Error fetching workstation: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

# Add a new workstation
def add_workstation(name, location):
    conn = connect_db()
    if not conn:
        return False
    
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Workstations (name, location) VALUES (%s, %s)", (name, location))
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print(f"Error adding workstation: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

# Update a workstation
def update_workstation(workstation_id, name, location):
    conn = connect_db()
    if not conn:
        return False
    
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE Workstations SET name = %s, location = %s WHERE workstation_id = %s", (name, location, workstation_id))
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print(f"Error updating workstation: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

# Delete a workstation
def delete_workstation(workstation_id):
    conn = connect_db()
    if not conn:
        return False
    
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Workstations WHERE workstation_id = %s", (workstation_id,))
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print(f"Error deleting workstation: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

@app.route('/add_workstation', methods=['POST'])
def add_workstation_route():
    name = request.form['name']
    location = request.form['location']
    if add_workstation(name, location):
        return redirect(url_for('manage_workstations'))
    else:
        return "Error adding workstation", 500

@app.route('/update_workstation', methods=['POST'])
def update_workstation_route():
    workstation_id = request.form['workstation_id']
    name = request.form['name']
    location = request.form['location']
    if update_workstation(workstation_id, name, location):
        return redirect(url_for('manage_workstations'))
    else:
        return "Error updating workstation", 500

@app.route('/delete_workstation', methods=['POST'])
def delete_workstation_route():
    workstation_id = request.form['workstation_id']
    if delete_workstation(workstation_id):
        return redirect(url_for('manage_workstations'))
    else:
        return "Error deleting workstation", 500

# Fetch all operators
def fetch_all_operators():
    conn = connect_db()
    if not conn:
        return []

    cursor = conn.cursor()
    try:
        cursor.execute("""SELECT 
                                o.operator_id, 
                                o.name AS operator_name, 
                                o.employee_number, 
                                o.workstation_id, 
                                w.name AS name
                            FROM 
                                public.operators o
                            LEFT JOIN 
                                public.workstations w 
                            ON 
                                o.workstation_id = w.workstation_id
                            ORDER BY 
                                o.operator_id ASC;
                            """)
        operators = cursor.fetchall()
        
        # Obter estações de trabalho
        cursor.execute("SELECT workstation_id, name FROM Workstations order by workstation_id ASC")
        workstations = cursor.fetchall()
        
        return operators, workstations
    except Exception as e:
        print(f"Error fetching operators: {e}")
        return [], []
    finally:
        cursor.close()
        conn.close()

# Add a new operator
def add_operator(name, employee_number, workstation):
    conn = connect_db()
    if not conn:
        return False

    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Operators (name, employee_number, workstation_id) VALUES (%s, %s, %s)", (name, employee_number, workstation))
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print(f"Error adding operator: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

# Update an operator
def update_operator(operator_id, name, employee_number, workstation):
    conn = connect_db()
    if not conn:
        return False

    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE Operators SET name = %s, employee_number = %s, workstation_id = %s WHERE operator_id = %s", (name, employee_number, workstation, operator_id))
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print(f"Error updating operator: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

# Delete an operator
def delete_operator(operator_id):
    conn = connect_db()
    if not conn:
        return False

    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Operators WHERE operator_id = %s", (operator_id,))
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print(f"Error deleting operator: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

@app.route('/add_operator', methods=['POST'])
def add_operator_route():
    name = request.form['name']
    employee_number = request.form['employee_number']
    workstation = request.form['workstation']
    if add_operator(name, employee_number, workstation):
        return redirect(url_for('manage_operators'))
    else:
        return "Error adding operator", 500

@app.route('/update_operator', methods=['POST'])
def update_operator_route():
    operator_id = request.form['operator_id']
    name = request.form['name']
    employee_number = request.form['employee_number']
    workstation = request.form['workstation']
    if update_operator(operator_id, name, employee_number, workstation):
        return redirect(url_for('manage_operators'))
    else:
        return "Error updating operator", 500

@app.route('/delete_operator', methods=['POST'])
def delete_operator_route():
    operator_id = request.form['operator_id']
    if delete_operator(operator_id):
        return redirect(url_for('manage_operators'))
    else:
        return "Error deleting operator", 500

@app.route('/api/worksessions')
def worksessions_data():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM public.worksessions')
    worksessions = cur.fetchall()
    cur.close()
    conn.close()
    
    # Convertendo para um formato que o DataTables possa utilizar
    data = []
    for session in worksessions:
        data.append({
            'session_id': session[0],
            'operator_id': session[1],
            'workstation_id': session[2],
            'start_time': session[3].strftime('%Y-%m-%d %H:%M:%S'),
            'end_time': session[4].strftime('%Y-%m-%d %H:%M:%S') if session[4] else None,
            'is_done': session[5]
        })
    
    return jsonify({'data': data})

@app.route('/hystoric')
def hystoric():
    machine_names = databaseOBJ.readRaw("select id, nome, fabricante, ano from maquina where id>0 and id <9 order by id ASC;")
    operators = fetch_all_operators()
    return flask.render_template('hystoric.html',  operators=operators, machine_names=machine_names)

@app.route('/status')
@flask_login.login_required
def status():
    status = fetch_workstation_status()
    return jsonify(status)

@app.route('/')
@app.route('/index')
@flask_login.login_required
def index():
    machine_names = databaseOBJ.readRaw("select id, nome, fabricante, ano from maquina where id>0 and id <9 order by id ASC;")

    return flask.render_template('index.html', machine_names=machine_names)

@app.route('/manage_workstations')
@flask_login.login_required
def manage_workstations():
    machine_names = databaseOBJ.readRaw("select id, nome, fabricante, ano from maquina where id>0 and id <9 order by id ASC;")
    workstations = fetch_all_workstations()
    return flask.render_template('manage_workstations.html', workstations=workstations, machine_names=machine_names)

@app.route('/manage_operators')
def manage_operators():
    machine_names = databaseOBJ.readRaw("select id, nome, fabricante, ano from maquina where id>0 and id <9 order by id ASC;")
    operators, workstations = fetch_all_operators()
    
    return flask.render_template('manage_operators.html', operators=operators, machine_names=machine_names, workstations=workstations)