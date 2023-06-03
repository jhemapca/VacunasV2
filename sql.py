#----------------------
import pyodbc
from flask import jsonify
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-ETC7CAN;DATABASE=Vacunas;Trusted_Connection=yes')
cursor = conn.cursor()

def get_usuarios():
    cursor = conn.cursor()
    sql = "select * from Usuarios"
    cursor.execute(sql)
    rows = cursor.fetchall()

    usuarios = []
    for row in rows:
        usuario = {
            'id_user': row[0],
            'dni': row[1],
            'firstName': row[2],
            'secondName': row[3],
            'firstLastName': row[4],
            'secondLastName': row[5],
            'genero': row[6],  # Convertir a cadena UTF-8
            'mail': row[7],
            'phone': row[8],
            'birthDate': row[9].isoformat(),
            'password': row[10],
            'id_Tipo': row[11]
        }
        usuarios.append(usuario)

    return usuarios

def guardar_usuario(usuario):
    cursor = conn.cursor()
    sql = """
    INSERT INTO Usuarios (id_user, dni, firstName, secondName, firstLastName, secondLastName, genero, mail, phone, birthDate, password, id_Tipo)
    VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    params = (
        usuario['id_user'],
        usuario['dni'],
        usuario['firstName'],
        usuario['secondName'],
        usuario['firstLastName'],
        usuario['secondLastName'],
        usuario['genero'],
        usuario['mail'],
        usuario['phone'],
        usuario['birthDate'],
        usuario['password'],
        usuario['id_Tipo']
    )
    cursor.execute(sql, params)
    conn.commit()

def actualizar_usuario(usuario):
    cursor = conn.cursor()
    query = "UPDATE usuarios SET dni=?, firstName=?, secondName=?, firstLastName=?, secondLastName=?, genero=?, mail=?, phone=?, birthDate=?, password=?, id_Tipo=? WHERE id_user=?"
    values = (
        usuario['dni'],
        usuario['firstName'],
        usuario['secondName'],
        usuario['firstLastName'],
        usuario['secondLastName'],
        usuario['genero'],
        usuario['mail'],
        usuario['phone'],
        usuario['birthDate'],
        usuario['password'],
        usuario['id_Tipo'],
        usuario['id_user']
    )
    cursor.execute(query, values)
    
    conn.commit()

def get_usuario_by_id(id):
    cursor = conn.cursor()
    query = "SELECT * FROM usuarios WHERE id_user = ?"
    cursor.execute(query, (id,))
    
    row = cursor.fetchone()
    
    if row:
        usuario = {
            'id_user': str(row[0]),
            'dni': row[1],
            'firstName': row[2],
            'secondName': row[3],
            'firstLastName': row[4],
            'secondLastName': row[5],
            'genero': row[6],
            'mail': row[7],
            'phone': row[8],
            'birthDate': row[9],
            'password': row[10],
            'id_Tipo': row[11]
        }
        return usuario
    else:
        return None