# Exercise 9-3: Users Class
class User:
    def __init__(self):

        self.First_Name = input("Enter your First Name:")
        self.Last_Name = input("Enter your Last Name:")
        self.age = int(input("Enter your age:"))
        self.Email = input("Enter your Email:")
        self.Location = input("Enter your Location:")
    
    def describe_user(self):
        print(f"\nUser Profile:")
        print(f"First Name: {self.First_Name}")
        print(f"Last Name: {self.Last_Name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.Email}")
        print(f"Location: {self.Location}")
    
    def greet_user(self):
        print(f"Hello {self.First_Name} {self.Last_Name}, welcome back!")



# Create several instances of User
# Call methods for each user

user1 = User()
user1.describe_user()
user1.greet_user()

print()
print()
print("Enther the Second User")

user2 = User()
user2.describe_user()
user2.greet_user()


print()
print()
print("Enther the Third User")

user3 = User()
user3.describe_user()
user3.greet_user()








