class Car():

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " mile on it")

    def fill_gas_tank(self):
        print("the gas need refill")


class Battery:

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def get_range(self):
        """Print a statement about the range this battery provides."""

        global range

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()
my_tesla.battery.get()
print(my_tesla.get_descriptive_name())

# my_new_car = Car('audi', 'a4', 2016)
# my_new_car.odometer_reading = 48
# my_new_car.read_odometer()
# print(my_new_car.get_descriptive_name())
