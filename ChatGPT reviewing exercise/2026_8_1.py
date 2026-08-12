from pathlib import Path

class PasswordChecker:
    def __init__(self, password):
        self.password = password

    def check_length(self):
        if len(self.password) >= 8:
            return True
        else:
            return False

    def has_number(self):
        for char in self.password:
            if char.isdigit():
                return True
        return False
    
    def has_uppercase(self):
        for char in self.password:
            if char.isupper():
                return True
        return False
    
    def has_special(self):
        return any(char in "!@#$%^" for char in self.password)
    
    def check_strength(self):
        score = 0
        if self.check_length():
            score += 1
        if self.has_number():
            score += 1
        if self.has_uppercase():
            score += 1
        if self.has_special():
            score += 1

        if score == 4:
            return "Strong"
        elif score == 3:
            return "Medium"
        else:
            return "Weak"

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self):
        checker = PasswordChecker(self.password)
        return checker.check_strength()

class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self):
        user = PasswordChecker(self.password)
        safety = user.check_strength()
        if safety == "Weak":
            print("Password is too weak!")
        else:
            self.users[self.username] = self.password

    def save_users(self):
        path = Path('users.txt')
        contents = ''

        for username, password in self.users.items():
            contents += (f"{username}, {password}\n")

        path.write_text(contents, encoding="utf-8")

        print("User saved.")