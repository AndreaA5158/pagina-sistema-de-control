from re import template
from flask import Flask, render_template, request, redirect, url_for
import mariadb

app = Flask(__name__)
app.secret_key = 'mysecretkey'

#A qui se indca que es la pagina principal
@app.route('/') 

# Es lo que va ver el usuario en esta funcion
def inicio(): 
    return render_template('Login.html')

@app.route('/iniciar_menu',methods=['POST'] )
def iniciar_menu():
    if request.method == 'POST':
       
        a = render_template('Menu.html')
        
        return a


#######################################################################################################
@app.route('/Menu')
def menu():
    return render_template('Menu.html')

#######################################################################################################

@app.route('/darDealtaUsuario')
def darDeAltaUsuario():

    conexion = mariadb.connect(host="127.0.0.1",port=3306,user="root",password="omarfco2",database="Sistema_De_Control")
    cur = conexion.cursor()
    # Declaracion en donde invocamos la funcion de consultaDeMariadb en donde los parametros pasamos la consulta
    # para obtener el usuario y contraseña y todo esto se guarda en la variable cur
    cur.execute("SELECT ID_usuario, CONCAT_WS(' ',Nombres_del_usuario ,Apellidos_del_usuario) AS Nombre, Turno, Numero_celular_del_usuario FROM usuario")
    dato = cur.fetchall()
    return render_template('darDealtaAusuarios.html',datos=dato)
    
@app.route('/AgregarUsuario', methods=['POST'])
def agregarDatos():
    if request.method == 'POST':
        nc = request.form['NumeroDeControl']
        nom = request.form['Nombre']
        apell = request.form['Apellido']
        tur = request.form['Turno']
        cel = request.form['Celular']
        
        try:
            conexion = mariadb.connect(host="127.0.0.1",port=3306,user="root",password="omarfco2",database="Sistema_De_Control")
            cur = conexion.cursor()
            # Declaracion en donde invocamos la funcion de consultaDeMariadb en donde los parametros pasamos la consulta
            # para obtener el usuario y contraseña y todo esto se guarda en la variable cur
            cur.execute('INSERT INTO usuario (ID_usuario,Nombres_del_usuario,Apellidos_del_usuario,Turno,Numero_celular_del_usuario) VALUES (?,?,?,?,?)',
            (nc,nom,apell,tur,cel))
            conexion.commit()
            conexion.close()
        except mariadb.Error as e:
            print(e)
        return redirect(url_for('darDeAltaUsuario'))

@app.route('/eliminarUsuario/<string:id>')
def eliminarUs(id):
    try:
        conexion = mariadb.connect(host="127.0.0.1",port=3306,user="root",password="omarfco2",database="Sistema_De_Control")
        cur = conexion.cursor()
        # Declaracion en donde invocamos la funcion de consultaDeMariadb en donde los parametros pasamos la consulta
        # para obtener el usuario y contraseña y todo esto se guarda en la variable cur
        cur.execute('DELETE FROM usuario WHERE usuario.ID_usuario  = ?',(id,))
        conexion.commit()
        conexion.close()
    except mariadb.Error as e:
            print(e)
    return redirect(url_for('darDeAltaUsuario'))



@app.route('/actualizarUsuarios/<string:id>')
def actualizarUs(id):
    conexion = mariadb.connect(host="127.0.0.1",port=3306,user="root",password="omarfco2",database="Sistema_De_Control")
    cur = conexion.cursor()
    # Declaracion en donde invocamos la funcion de consultaDeMariadb en donde los parametros pasamos la consulta
    # para obtener el usuario y contraseña y todo esto se guarda en la variable cur
    cur.execute('SELECT ID_usuario, Nombres_del_usuario ,Apellidos_del_usuario, Turno, Numero_celular_del_usuario FROM usuario where ID_usuario =?', (id,))
    dato = cur.fetchall()
    return render_template('editarUsuario.html',datos=dato[0])

@app.route('/actus', methods=['POST'])
def actualizarUsua():
    if request.method == 'POST':
        nc = request.form['NumeroDeControl']
        nom = request.form['Nombre']
        apell = request.form['Apellido']
        tur = request.form['Turno']
        cel = request.form['Celular']
        
        try:
            conexion = mariadb.connect(host="127.0.0.1",port=3306,user="root",password="omarfco2",database="Sistema_De_Control")
            cur = conexion.cursor()
            # Declaracion en donde invocamos la funcion de consultaDeMariadb en donde los parametros pasamos la consulta
            # para obtener el usuario y contraseña y todo esto se guarda en la variable cur
            cur.execute('UPDATE usuario SET ID_usuario = ?,Nombres_del_usuario = ?, Apellidos_del_usuario = ?,Turno = ?, Numero_celular_del_usuario = ? WHERE ID_usuario = ?',(nc,nom,apell,tur,cel,nc))
            conexion.commit()
            conexion.close()
        except mariadb.Error as e:
            print(e)
        return redirect(url_for('darDeAltaUsuario'))

##########################################################################################################
#Dar de alta vehiculo

@app.route('/darDeraltaVehiculo')
def darDeHaltaVehi():
    

    conexion = mariadb.connect(host="127.0.0.1",port=3306,user="root",password="omarfco2",database="Sistema_De_Control")
    cur = conexion.cursor()
    # Declaracion en donde invocamos la funcion de consultaDeMariadb en donde los parametros pasamos la consulta
    # para obtener el usuario y contraseña y todo esto se guarda en la variable cur
    cur.execute("SELECT ID_Placas, Tipo_de_vehiculo, Modelo, Uso FROM vehiculo")
    dato = cur.fetchall()
    return render_template('darDeAlthaVehiculos.html', datos=dato)
  
@app.route('/AgregarVehiculo', methods=['POST'])
def agregarvehiculosd():
    if request.method == 'POST':
        pl = request.form['Placas']
        tpv = request.form['Tipo de vehiculo']
        modulo = request.form['Modulo']
        uso = request.form['Uso']
        
        try:
            conexion = mariadb.connect(host="127.0.0.1",port=3306,user="root",password="omarfco2",database="Sistema_De_Control")
            cur = conexion.cursor()
            # Declaracion en donde invocamos la funcion de consultaDeMariadb en donde los parametros pasamos la consulta
            # para obtener el usuario y contraseña y todo esto se guarda en la variable cur
            cur.execute('INSERT INTO vehiculo VALUES (?,?,?,?)',(pl,tpv,modulo,uso))
            conexion.commit()
            conexion.close()
        except mariadb.Error as e:
            print(e)
        return redirect(url_for('darDeHaltaVehi'))

@app.route('/eliminarVehiculo/<string:id>')
def eliminarVe(id):
    try:
        conexion = mariadb.connect(host="127.0.0.1",port=3306,user="root",password="omarfco2",database="Sistema_De_Control")
        cur = conexion.cursor()
        # Declaracion en donde invocamos la funcion de consultaDeMariadb en donde los parametros pasamos la consulta
        # para obtener el usuario y contraseña y todo esto se guarda en la variable cur
        cur.execute('DELETE FROM vehiculo WHERE ID_Placas = ?',(id,))
        conexion.commit()
        conexion.close()
    except mariadb.Error as e:
            print(e)
    return redirect(url_for('darDeHaltaVehi'))

@app.route('/actualizarVehiculosvista/<string:id>')
def actualizarVe(id):
    conexion = mariadb.connect(host="127.0.0.1",port=3306,user="root",password="omarfco2",database="Sistema_De_Control")
    cur = conexion.cursor()
    # Declaracion en donde invocamos la funcion de consultaDeMariadb en donde los parametros pasamos la consulta
    # para obtener el usuario y contraseña y todo esto se guarda en la variable cur
    cur.execute('SELECT ID_Placas, Tipo_de_vehiculo, Modelo, Uso FROM vehiculo where ID_Placas = ?', (id,))
    dato = cur.fetchall()
    return render_template('ActualizarVehiculo.html',datos=dato[0])

@app.route('/ActualizarVehiculo2', methods=['POST'])
def ActualizarVehiculo2():
    if request.method == 'POST':
        pl = request.form['Placas']
        tpv = request.form['Tipo de vehiculo']
        modulo = request.form['Modulo']
        uso = request.form['Uso']
        pl9 = request.form['Placas']
        
        try:
            conexion = mariadb.connect(host="127.0.0.1",port=3306,user="root",password="omarfco2",database="Sistema_De_Control")
            cur = conexion.cursor()
            # Declaracion en donde invocamos la funcion de consultaDeMariadb en donde los parametros pasamos la consulta
            # para obtener el usuario y contraseña y todo esto se guarda en la variable cur
            cur.execute('UPDATE vehiculo set ID_Placas = ?, Tipo_de_vehiculo = ?, Modelo = ?, Uso = ? WHERE ID_Placas = ?',(pl,tpv,modulo,uso,pl9,))
            conexion.commit()
            conexion.close()
        except mariadb.Error as e:
            print(e)
        return redirect(url_for('darDeHaltaVehi'))

if __name__ == '__main__':
    app.run(debug=True) 