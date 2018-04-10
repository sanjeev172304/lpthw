# empty tuple
#output:()
my_tuple=()
print(my_tuple)

#tuple having integers
#output: (1,2,3)

my_tuple=(1,2,3)
print(my_tuple)


#tuple with mis=xed datatypes
#output (1, "hello",3.4 )

my_tuple=(1,"hello",3.4)
print(my_tuple)

#nested tuple
#output ("mouse",[8,4,6],(1,2,3))
print(my_tuple)

#tuple can be created without paranthesis
#also called tuple packing
#output: 3, 4.6, "dog"

my_tuple=3,4.6,"dog"

#tuple unpacking is possible
#output
#3
#4.6
#dog
a,b,c=my_tuple
print(a)
print(b)
print(c)
