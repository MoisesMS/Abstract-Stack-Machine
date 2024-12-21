import argparse

# ADD Añade un numero a la pila.
# SUM Suma los dos últimos numeros de la pila. El resultado lo devuelve a la pila.
# GET Obtiene el último número de la pila.

var_values = {}
var_name = ""

# Pila de memoria
stack = []
msg_less_two_numbers = "No hay suficientes números en la pila."
msg_empty_stack = "Empty stack"

def compiler(order):
  global var_name
  global var_values
  global stack

  if order == "EXIT":
    exit()

  if order.startswith("METE"):
    try:
      number = int(order[5:])
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
  elif order.startswith("ASIGNA"):
    var_values[var_name] = stack[-1]
    stack.pop()
  elif order.startswith("VALORI"):
    var_name = order[7:]
  elif order.startswith("VALORD"):
    stack.append(var_values[order[7:]])
  elif order.startswith("DEL"):
    if len(stack) == 0:
      print(msg_empty_stack)
    else:
      stack.pop()
  else:
    print(order)
    print("El comando no existe.")


def mathematic_operations(operator):
  if operator == "SUM":
    sum = stack[-2] + stack[-1]
    add_result(sum)
  elif operator == "SUB":
    sub = stack[-2] - stack[-1]
    add_result(sub)
  elif operator == "MUL":
    div = stack[-2] * stack[-1]
    add_result(div)
  elif operator == "DIV":
    if stack[-1] == 0:
      print("No se puede dividir por cero.")
    else:
      div = stack[-2] / stack[-1]
      add_result(div)

# Elimina los dos últimos elementos de la pila y añade el resultado
def add_result(data):
  stack.pop()
  stack.pop()
  stack.append(data)

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
  elif operator == "DIV":
    if len(stack) < 2:
      print(msg_less_two_numbers)
    else:
      mathematic_operations("DIV")


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