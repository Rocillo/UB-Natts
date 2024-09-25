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


######################################################## VIEWS ########################################################
@app.route('/autenticacao', methods=['GET'])
def autenticacao():
    if flask_login.current_user.is_authenticated:
        return flask.redirect(flask.url_for('index'))
    else:
        return flask.render_template('autenticacao.html')

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
DB_HOST = '192.168.86.89'
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