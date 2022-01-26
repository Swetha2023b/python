lower=int(input("Enter the lower limit:"))
upper=int(input("Enter the upper limit:"))
list=[x for x in range(lower,upper+1) if x**0.5==int(x**0.5)]
print(list)
