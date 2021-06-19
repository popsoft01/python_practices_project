class Restaurant():
    def __init__(self, restaurant_name, cuisine_type,number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant serve all local and forign food")
        print("The best place to enjoy with friend")

    def open_restuarant(self):
        print("we are open for business")

    def set_customer_served(self):
       print(f"The number of customer served {self.number_served}")

    def increment_nuber_served(self):
        self.number_served += 1


tolu = Restaurant("toluBlass", 'africa dish')
print(tolu.restaurant_name, tolu.cuisine_type)
tolu.describe_restaurant()


class users():
    def __init__(self, first, last, DOB, state):
        self.first = first
        self.last = last
        self.DOB = DOB
        self.state = state

    def describe_restaurant(self):
        print(f'{self.last} {self.last} born on {self.DOB} from {self.state}')

    def greet_user(self):
        print()
