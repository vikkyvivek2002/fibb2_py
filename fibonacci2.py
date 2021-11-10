x = int(input("enter a number"))
a=0
b=1
temp =a+b
print(a)
print(b)
while(temp<=x):
    print(temp)
    a = b
    b = temp
    temp = a+b
