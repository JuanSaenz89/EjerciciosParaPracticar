# 4) Una juguetería tiene mucho éxito en dos de sus productos:payasos y muñecas.
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
# así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. 
# Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido 
# y calcule el peso total del paquete que será enviado.
from contadorMunecas import *
from contadorPayasos import *

def peso_total(numero1,numero2):
  print(f"El peso total de envio seria: {contador_payasos(numero1) + contador_munecas(numero2)}g")