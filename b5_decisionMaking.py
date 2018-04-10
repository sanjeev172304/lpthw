#  decision making statements
a=int(input("Enter a number:"))
b=int(input("Enter another Number:"))
#if else decision making statements
if a > b:
    print("First number is greater than second number")
else:
    print("second number is greater than first number")

#Nasted if condition

c=a
d=b
if c>d:
    print("First number is greater than second number")
elif c==d:
    print("both number is equal")
else:
    print("second number is greater than first number")


#looping statements
#1. while loop-repeats a statements while giving condition is true
print("while loop statements")
print("print hello 10 time from the help of while loop")
a=int(1) #variable defined befor but it not taking before declered variable values. current va
while a<=10:
    print("Hello",+a)
    a=a+1
# for loop- execute a sequence of statement multiple times and abbreviates the code that  manage variables
print("for loop statements")
for i in range(1,5):
   print(i)
   print("\n")

#nested loop

for i in range(1,5):
    for j in range(i,5):
        print(i);
    print("\n")



