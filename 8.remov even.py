list = [11, 22,41, 3, 99, 100]
print "Original list:"
print list
for i  in list:
	if(i%2 == 0):
	    list.remove(i)
print "list after removing EVEN numbers:"
print list
