# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

total_true = name1.count('t')
total_true +=name1.count('r')
total_true +=name1.count('u')
total_true +=name1.count('e')

total_love = name1.count('l')
total_love +=name1.count('o')
total_love +=name1.count('v')
total_love +=name1.count('e')

total_true += name2.count('t')
total_true += name2.count('r')
total_true += name2.count('u')
total_true += name2.count('e')
total_love += name2.count('l')
total_love += name2.count('o')
total_love += name2.count('v')
total_love += name2.count('e')

total = str(total_true) + str(total_love)
total = int(total)
if total< 10 or total > 90:
    print(f'Your score is {total}, you go together like coke and mentos.')
elif total >=40 and total <= 50:
    print(f'Your score is {total}, you are alright together.') 
else:
    print(f'Your score is {total}')     

