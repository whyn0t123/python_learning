class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attemps = 0

    def describe_user(self):
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()}.")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attemps(self):
        self.login_attemps += 1

    def reset_login_attemps(self):
        self.login_attemps = 0

user = User('zhiyuan', 'nie')

user.describe_user()
user.greet_user()

user.increment_login_attemps()
user.increment_login_attemps()
user.increment_login_attemps()

print(user.login_attemps)

user.reset_login_attemps()

print(user.login_attemps)