# Exercise 9-1: Restaurant Class
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Create an instance of Restaurant
# restaurant = Restaurant("Pasta Palace", "Italian")
restaurant = Restaurant(input("Enter the Restaurant_Name:"), input("Enter the Cuisine_Type:"))

# Call the methods
restaurant.describe_restaurant()
restaurant.open_restaurant()




# Exercise 9-2: Three Restaurants
# Create three instances of Restaurant
restaurant1 = Restaurant("Pasta Palace", "Italian")
restaurant2 = Restaurant("Sushi Spot", "Japanese")
restaurant3 = Restaurant("Taco Town", "Mexican")

# Call describe_restaurant for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
