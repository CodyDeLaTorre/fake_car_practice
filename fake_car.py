
class Car:
    def __init__(self):
        self.on = False
        self.speed = 0
        self.gas_pedal = False
        self.steering_wheel = 0
        self.gear = "P"

    def start(self):
        self.on = True
    
    def stop(self):
        self.off = False

    def gas_pedal_down(self):
        self.gas_pedal = True
    
    def accelerate(self):
        while self.gas_pedal == True:
            self.speed += 1
            print("car is accelerating!")

    def decelerate(self):
        if self.speed == 0:
            return
        while self.gas_pedal == False:
            self.speed -= 1
            print("car is decelerating!")


car = Car()

choice = input("Start the car? Y or N: ")

if choice == 'Y':
    car.start
    print(f"You car is on and in {car.gear}")
    gear_selection = input("what gear do you want to be in? P = Park, R = Reverse, N = Neatral, D = Drive, L = Low ")
    car.gear = gear_selection
    if car.gear == "D":
        car.accelerate

else:
    car.stop

