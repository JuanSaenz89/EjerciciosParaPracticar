# 9) Escribir un programa que almacene el abecedario en una lista, 
# elimine de la lista las letras que ocupen posiciones múltiplos de 3,
#  y muestre por pantalla la lista resultante.

letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def abecedario(lista):
  for letra in lista:
    if (lista.index(letra))%2 == 0 and (lista.index(letra)) > 0: 
      lista.remove(letra)
  print(lista)