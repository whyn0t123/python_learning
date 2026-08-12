class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name.title()}.")
        print(f"The restaurant provides {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self,number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

restaurant = Restaurant('KFC', 'fast food')

restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"The restaurant has served {restaurant.number_served} customers.")

restaurant.number_served = 20
print(f"The restaurant has served {restaurant.number_served} customers.")

restaurant.set_number_served(50)
print(f"The restaurant has served {restaurant.number_served} customers.")

restaurant.increment_number_served(200)
print(f"The restaurant has served {restaurant.number_served} customers.")