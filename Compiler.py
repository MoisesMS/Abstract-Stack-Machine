import argparse

# ADD Añade un numero a la pila.
# SUM Suma los dos últimos numeros de la pila. El resultado lo devuelve a la pila.
# GET Obtiene el último número de la pila.

# Pila de memoria
stack = []

def compiler(order):
  if order == "EXIT":
    exit()

  if order.startswith("ADD"):
    try:
      number = int(order[4:])
      stack.append(number)
    except ValueError:
      print("El dato insertado no es válido.")
  elif order.startswith("GET"):
    if len(stack) == 0:
      print("La pila está vacía.")
    else:
      print(stack[-1])
  elif order.startswith("SUM"):
    if len(stack) < 2:
      print("No hay suficientes elementos para sumar")
    else:
      sum = stack.pop() + stack.pop()
      stack.append(sum)
  else:
    print("El comando no existe.")

parser = argparse.ArgumentParser(description="Recibe un archivo por parametro")
parser.add_argument("file", type=str, nargs="?", help="Archivo con el código")

arg = parser.parse_args()
    

if arg.file:

  #Leer archivo
  with open(arg.file, "r") as file:
    lines = file.readlines()

    for line in lines:
      compiler(line)
else:
  while True:
    compiler(input(">>> "))