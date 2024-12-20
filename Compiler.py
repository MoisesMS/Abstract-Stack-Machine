import argparse

# ADD Añade un numero a la pila.
# SUM Suma los dos últimos numeros de la pila. El resultado lo devuelve a la pila.
# GET Obtiene el último número de la pila.

# Pila de memoria
stack = []
msg_less_two_numbers = "No hay suficientes números en la pila."
msg_empty_stack = "Empty stack"

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
      print(msg_empty_stack)
    else:
      print(stack[-1])
  elif order.startswith("SUM"):
    operations("SUM")
  elif order.startswith("SUB"):
    operations("SUB")
  elif order.startswith("MUL"):
    operations("MUL")
  elif order.startswith("DEL"):
    if len(stack) == 0:
      print(msg_empty_stack)
    else:
      stack.pop()
  else:
    print("El comando no existe.")


def mathematic_operations(operator):
  if operator == "SUM":
    sum = stack[-2] + stack[-1]
    stack.pop()
    stack.pop()
    stack.append(sum)
  elif operator == "SUB":
    sum = stack[-2] - stack[-1]
    stack.pop()
    stack.pop()
    stack.append(sum)
  elif operator == "MUL":
    sum = stack[-2] * stack[-1]
    stack.pop()
    stack.pop()
    stack.append(sum)


def operations(operator):
  if operator == "SUM":
    if len(stack) < 2:
      print(msg_less_two_numbers)
    else:
      mathematic_operations("SUM")
  elif operator == "SUB":
    if len(stack) < 2:
      print(msg_less_two_numbers)
    else:
      mathematic_operations("SUB")
  elif operator == "MUL":
    if len(stack) < 2:
      print(msg_less_two_numbers)
    else:
      mathematic_operations("MUL")


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