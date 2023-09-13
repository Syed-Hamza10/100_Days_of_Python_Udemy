from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

dictionary = {}

output = True

def find_highest_bidder(dictionary):
  max = 0
  winner = ''
  for key in dictionary:
    if dictionary[key] > max:
      max = dictionary[key]
      winner = key
  print(f"The Winner is {winner} with bid {max}")    



while output:
  name = input("Enter your name\n")
  bid = int(input("Enter your Bid $\n"))
  dictionary[name] = bid

  bidders = input("Are there any more bidders? yes/no\n")
  if bidders.lower() == 'no':
    output = False
    find_highest_bidder(dictionary)
  if bidders.lower() == 'yes':
    clear()

print()

      
  
    
  
    

