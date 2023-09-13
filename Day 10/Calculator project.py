from art import logo

def add(n1, n2):
  return n1 + n2
  
def sub(n1, n2):
  return n1 - n2

def mul(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2  


operations = {'+' : add,
              '-' : sub,
              '*' : mul,
              '/' : div,
              
             }
def calculator():
  print(logo)
  num1 = float(input("Enter 1st number. "))
  
  
  for key in operations:
    print(key)
  
  should_continue = True
  while should_continue:
  
    symbol = input("\nPick an operation from above: ")
    num2 = float(input("What' the next number? "))
    function = operations[symbol]
    result = function(num1,num2)
    print(f"Result for {num1} {symbol} {num2} is {result}")
    output = input("Type y to continue calculating with {result}, or type n to start a new calcuation \n")
    
    if output.lower() == 'n':
      should_continue = False
      calculator()
    if output.lower() == 'y':
      num1 = result
calculator()    
    

  





