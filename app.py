from flask import Flask, request, jsonify, render_template, redirect, url_for
import sql

app = Flask(__name__)

def get_last_user_id():
    usuarios = sql.get_usuarios()
    last_user = usuarios[-1] if usuarios else None
    return int(last_user['id_user']) if last_user else 0


@app.route('/usuarios', methods=['GET'])
def usuarios():
    usuarios = sql.get_usuarios()
    return render_template('usuariosMostrar.html', usuarios=usuarios)

@app.route('/personalRegistro')
def personalRegistro():
    return render_template('personalRegistro.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/contactenos')
def contactenos():
    return render_template('contactenos.html')

@app.route('/administrativoSalud')
def administrativoSalud():
    return render_template('administrativoSalud.html')

@app.route('/dosisVacunacion')
def dosisVacunacion():
    return render_template('dosisVacunacion.html')

@app.route('/enfermero01')
def enfermero01():
    return render_template('enfermero01.html')

@app.route('/nuevoReporte')
def nuevoReporte():
    return render_template('nuevoReporte.html')

@app.route('/registroVacuVisual')
def registroVacuVisual():
    return render_template('registroVacuVisual.html')

@app.route('/turnosEnfermeros')
def turnosEnfermeros():
    return render_template('turnosEnfermeros.html')

@app.route('/usuario01')
def usuario01():
    return render_template('usuario01.html')

@app.route('/guardar_usuario', methods=['POST'])
def guardar_usuario():
    next_id = get_last_user_id() + 1

    usuario = {
        'id_user':str(next_id),
        'dni': request.form['dni'],
        'firstName': request.form['firstName'],
        'secondName': request.form['secondName'],
        'firstLastName': request.form['firstLastName'],
        'secondLastName': request.form['secondLastName'],
        'genero': request.form['genero'],
        'mail': request.form['mail'],
        'phone': request.form['phone'],
        'birthDate': request.form['birthDate'],
        'password': request.form['password'],
        'id_Tipo': request.form['id_Tipo']
    }
    sql.guardar_usuario(usuario)
    return render_template('personalRegistro.html')

@app.route('/usuarios/<int:id>', methods=['GET', 'PUT'])
def editar_usuario(id):
    if request.method == 'GET':
        usuario = sql.get_usuario_by_id(id)
        if usuario:
            return render_template('editarUsuario.html', usuario=usuario)
        else:
            return "Usuario no encontrado"

    elif request.method == 'PUT':
        usuario = {
            'id_user':str(id),
            'dni': request.form['dni'],
            'firstName': request.form['firstName'],
            'secondName': request.form['secondName'],
            'firstLastName': request.form['firstLastName'],
            'secondLastName': request.form['secondLastName'],
            'genero': request.form['genero'],
            'mail': request.form['mail'],
            'phone': request.form['phone'],
            'birthDate': request.form['birthDate'],
            'password': request.form['password'],
            'id_Tipo': request.form['id_Tipo']
        }
        sql.actualizar_usuario(usuario)
        return "Usuario actualizado"

if __name__ == '__main__':
    app.run()
