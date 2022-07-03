
print("Ingrese su nombre de usuario: ")
usuario = (input())

if usuario == ["root"]:
    print("Usuario correcto... \n Ahora ingrese su contraseña")
    contraseña = (input())

    if contraseña == "toor":
        print("¡Bienvenido!")
    else:
        print("contraseña incorrecta")

else:
    print("Acceso fallido")
