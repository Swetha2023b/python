a=input("Enter the word=")
def word(wrd):
    wrd1=wrd[-3:]
    if wrd1 != "ing":
        print("adding 'ing'=",wrd+"ing")
    else:
        print("adding 'ly'=",wrd+"ly")
word(wrd=a)