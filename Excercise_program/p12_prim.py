prim_num=int(input("Enter the number to check the prim number"))

if prim_num > 1:
   for i in range(2,prim_num):
       if (prim_num%i)==0:
          print(prim_num, "is not a prime number")
          print(i,"times",prim_num//i,"is", prim_num)
          break;
       else:
          print(prim_num, "is a prime number")
else:
   print(prim_num, "is not a prime number")
