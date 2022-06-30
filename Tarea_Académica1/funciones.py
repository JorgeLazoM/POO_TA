def listarUsuarios(usuario):
    print("Usuarios: ")
    contador=1
    for usr in usuario:
        datos="{0}. User: {1}   Nombre: {2}    Apellido: {3}    DNI: {4}"
        print(datos.format(contador,usr[0],usr[1],usr[2],usr[3]))
        contador=contador+1
    print(" ")

def pedirDatosRegistro():
    dnicorrecto=False
    user=input("Ingrese usuario: ")
    nombre=input("Ingrese nombre: ")
    apellido=input("ingrese apellido: ")
    while(not dnicorrecto):
        dni=(input("Ingrese DNI: "))
        if len(dni)==8:
            dnicorrecto=True
        else:
            print("DNI incorrecto")
    usuarios=(user,nombre,apellido,dni)
    return usuarios