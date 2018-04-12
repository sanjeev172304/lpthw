Area1=int(input("Enter the side Area1="))
Area2=int(input("Enter the side of Area2="))
Area3=int(input("Enter the side of area3="))

Area_s=(Area1+Area2+Area3)/2

Cal_Area=(Area_s*(Area_s-Area1)*(Area_s-Area2)*(Area_s-Area3))**0.5

print('The area of the triangle is %0.2f' %Cal_Area)
