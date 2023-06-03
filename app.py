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

@app.route('/formNuevoReg')
def formNuevoReg():
    return render_template('usuariosRegistrar.html')

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
    return "Nuevo usuario"

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
