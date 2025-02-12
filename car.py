car_speed = 60  # speed in km/h
road_condition = "smooth"
car_position = 0  # starting at position 0

# Simulate the car driving down the road
while car_position < 100:  # car will drive until position 100
    car_position += car_speed / 60  # update position every minute
    print(f"Car is at position {car_position:.2f} km on a {road_condition} road.")
