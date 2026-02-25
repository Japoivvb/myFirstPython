#  arithmetic +, -, *, /, //
#  comparation >, <, == , !=
# logic and, or, not

# exercise race
# first car
distance_car_1 = 250
time_car_1 =  5
# second car
distance_car_2 = 180
time_car_2 =  3
# calculate speed v = d * t
speed_car_1 =  distance_car_1 / time_car_1
speed_car_2 =  distance_car_2 / time_car_2
print("speed1" , speed_car_1)
print("speed2" , speed_car_2)
# speed difference
print("difference", speed_car_2 - speed_car_1)
# get faster car
if speed_car_1 > speed_car_2:
    print("car 1 is faster")

else:
    print("car 2 is faster")

