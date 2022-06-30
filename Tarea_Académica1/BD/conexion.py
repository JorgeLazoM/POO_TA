import mysql.connector

from mysql.connector import Error

class DAO():

    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='biblioteca'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def listarUsuarios(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM usuarios")
                resultados=cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    
    def registrarUsuario(self, usuarios):
        if self.conexion.is_connected:
            try:
                cursor=self.conexion.cursor()
                sql= "INSERT INTO usuarios (user, nombre, apellido, dni) VALUES ('{0}', '{1}', '{2}', {3})"
                cursor.execute(sql.format(usuarios[0], usuarios[1], usuarios[2], usuarios[3]))
                self.conexion.commit()
                print("Usuario registrado")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))