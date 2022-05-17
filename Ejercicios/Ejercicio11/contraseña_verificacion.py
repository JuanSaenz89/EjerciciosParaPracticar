# 11)Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña e imprima por pantalla
# si la contraseña introducida por el usuario coincide con la guardada en la variable
#  sin tener en cuenta mayúsculas y minúsculas.

def contraseña_verificacion(contraseña):
    if contraseña.lower() == "contraseña":
      print("la contraseña ingresada es correcta")
    else:
      print("la contraseña ingresada no es correcta")