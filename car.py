car_speed = 60  # Speed in km/h
road_condition = "smooth"
car_position = 0  # Starting at 0.

# Simulating the car driving down the road
while car_position < 100:  # Car will drive until position reaches 100
    car_position += car_speed / 60  # Update position every minute
    print(f"Car is at position {car_position:.2f} km on a {road_condition} road.")
