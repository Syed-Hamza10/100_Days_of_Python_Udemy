#Write your code below this row 👇
count = 0
for i in range(2,101,2):
    count+=i

print(count)   


count2 = 0
for i in range(1,101):
    if i % 2 == 0:
        count+=i

print(count)   
