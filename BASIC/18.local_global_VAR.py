
# Globla Variable: Variable Which declared outside the functions.
#                  it can accessed inside as well as outside of 
#                 the functions


# Local Variable: Variable which are declared inside the functions.
#                 it can be accessed inside of the function


x = 20             #local

def var1():
    x = 10        #global
    print("local variable is:", x)

def var2():
    var1()
    print("Global variable is:", x)  
    var1()

# main
var2()  



# REAL WORLD EXAMLES
total_no_seats = 4
fixed_rate_km  = 4
fixed_rate_hour = 1.2

def share_trip(person_id, distance, hours):    #formal prameters
    distance = distance
    hours = hours
    amt = (distance * fixed_rate_km) + (hours * fixed_rate_km)
    global total_no_seats
    total_no_seats -= 1

    bon = bonus_cal(distance)
    print("Driver Bonous is: ", bon)
    return amt


# for driver bonus
def bonus_cal(distance):
    bonus = distance*fixed_rate_hour/5
    return bonus 

# 1st person book ticket 
amt = share_trip(7000000000001,5,1)           #actual parameter
print("Total amount paid by customer", amt)
print("Total number of seats remaining: ",total_no_seats) 


# 2nd person book ticket at the same time
amt = share_trip(7000000000001,4,1)
print("Total amount paid by customer", amt)
print("Total number of seats remaining: ",total_no_seats) 





