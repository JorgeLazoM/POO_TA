from BD.conexion import DAO
import funciones

def menuPrincipal():
    continuar=True
    while(continuar):
        opcionCorrecta=False
        while(not opcionCorrecta):
            print("======================MENÚ PRINCIPAL======================")
            print("1.-Listar usuarios")
            print("2.-Registrar usuario")
            print("3.-Actualizar usuario")
            print("4.-Eliminar usuario")
            print("5.-Salir")
            print("===========================================================")
            opcion=int(input("Seleccione una opción: "))

            if opcion <1 or opcion >5:
                print("Opción incorrecta, ingrese nuevamente")
            elif opcion ==5:
                continuar=False
                print("Gracias por usar este sistema")
                break
            else:
                opcionCorrecta=True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    dao=DAO()

    if opcion == 1:
        try:
            usuarios=dao.listarUsuarios()
            if len(usuarios)>0:
                funciones.listarUsuarios(usuarios)
            else:
                print("No se encontraron usuarios")
        except:
            print("Ocurrió un error")
    elif opcion == 2:
        usuarios= funciones.pedirDatosRegistro()
        try:
            dao.registrarUsuario(usuarios)
        except:
            print("Ocurrió un error")
    elif opcion == 3:
        print("Actualización")
    elif opcion == 4:
        print("Eliminación")

menuPrincipal()        