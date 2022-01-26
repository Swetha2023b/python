num=int(input("Enter the limit="))
def fact(x):
    fact=1
    for i in range(x,0,-1):
        fact=fact*i
    print("factorial=",fact)
fact (num)