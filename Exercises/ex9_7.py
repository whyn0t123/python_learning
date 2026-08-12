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

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privilege = Privileges()

class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("The admin has the following privileges:")
        for privilege in self.privileges:
            print(f"-{privilege}")