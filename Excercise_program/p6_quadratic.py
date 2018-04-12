import cmath
Qua_a=float(input("Enter Value of a="))
Qua_b=float(input("Enter value of b="))
Qua_c=float(input("Enter value of c="))

Qua_d=(Qua_b**2)-(4*Qua_a*Qua_c)

Sol1=(-Qua_b-cmath.sqrt(Qua_d))/(2*Qua_a)
Sol2=(-Qua_b+cmath.sqrt(Qua_d))/(2*Qua_a)

print('the aolution are {0} and {1}'.format(Sol1,Sol2))

