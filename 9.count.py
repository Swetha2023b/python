def x_count(str):

    counts = dict()
    words = str.split()

    for x in words:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts
string = input("Please enter sentence: ")


print( x_count(string))