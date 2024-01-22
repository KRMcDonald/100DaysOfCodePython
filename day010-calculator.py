from replit import clear

#Add
def add(n1,n2):
  return n1 + n2

#Subtract
def subtract(n1,n2):
  return n1 - n2

#Multiply
def multiply(n1,n2):
  return n1 * n2

#Divide
def divide(n1,n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

#This is an infinite while loop. Exit with control-C
while True:
  n1 = float(input("What's the first number? "))

  for symbol in operations:
    print(symbol)

  operation_symbol = input("Pick an operation from the lines above: ")

  n2 = float(input("What's the second number? "))

  calculation_function = operations[operation_symbol]
  result = calculation_function(n1,n2)
  print(f"{n1} {operation_symbol} {n2} = {result}")

  cont_with_same_number = input("Do you want to continue this calculation? y/n ")
  while cont_with_same_number == "y":
    next_operation = input("What is the next operation? ")
    next_number = float(input("What is the next number? "))
    calculation_function = operations[next_operation]
    new_result = calculation_function(result,next_number)
    print(f"{result} {next_operation} {next_number} = {new_result}")
    cont_with_same_number = input("Do you want to continue this calculation? y/n ")
    result = new_result

  clear()