# this code is defined for car details
cars =100 #variable declared with integer number
space_in_a_car =4.0 #variable declared with float number
drivers=30
passengers=90
cars_not_driven= cars - drivers #here substracting from defined variable
cars_driven=drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car=passengers/cars_driven

#now print statement

print(" there are",cars,"cars available.")
print("There are only",drivers,"drivers available")
print("there will be",cars_not_driven,"empaty cars today.")
print("we can transport",carpool_capacity,"people today.")
print("we have",passengers,"to carpool today")
print("we need to put about",average_passengers_per_car,"in each car.")


