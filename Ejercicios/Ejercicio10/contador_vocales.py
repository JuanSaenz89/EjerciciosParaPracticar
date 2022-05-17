# 10)Escribir un programa que pida al usuario una palabra 
# y muestre por pantalla el número de veces que contiene cada vocal.

def contador_vocales(palabra):
  a = palabra.count("a")
  e = palabra.count("e")
  i = palabra.count("i")
  o = palabra.count("o")
  u = palabra.count("u")

  print(f"En, {palabra}, puede encontrarse {a} veces la vocal a")
  print(f"En, {palabra}, puede encontrarse {e} veces la vocal e")
  print(f"En, {palabra}, puede encontrarse {i} veces la vocal i")
  print(f"En, {palabra}, puede encontrarse {o} veces la vocal o")
  print(f"En, {palabra}, puede encontrarse {u} veces la vocal u")