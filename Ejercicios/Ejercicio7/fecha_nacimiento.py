# 7) Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa 
# y muestra por pantalla, el día, el mes y el año. 
# Adaptar el programa anterior para que también funcione cuando el día o el mes
# se introduzcan con un solo carácter. 

def fecha_nacimiento(fecha):
  dia = fecha[:fecha.find("/")]
  mes = fecha[fecha.find("/")+1:fecha.find("/",3,6):]
  año = fecha[fecha.find("/",3,10)+1:]
  print(dia)
  print(mes)
  print(año)