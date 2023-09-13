#Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    i = 2
    while i<number:
        if number%i == 0:
            is_prime = False
        i+=1    
    if is_prime is False:
        print("It's not a prime number.")                 
    else:
        print("It's a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
