first=float(input("Enter first Number:"))
second=float(input("Enter second Number"))
third= float(input("Enter third number"))

if(first>=second) and (first>=third):
   largest=first
elif (second>=first) and (second>=third):
   largest=second
else:
   largest=third

print("The largest number between ", first,",",second,",",third,"is", largest)

