class Vehicle:

    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        return "filling up!"

    pass

subaru = Vehicle(10,20)
print(subaru.wheel_number)
print(subaru.wheel_size)
print(subaru.fill_up_tank())