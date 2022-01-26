current=int(input("enter the current year:"))
final=int(input("enter the final year:"))
for year in(range(current,final)):
    if(year%4)==0:
      print year,"is a leap year"
