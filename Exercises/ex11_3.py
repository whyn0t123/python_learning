class Employee:
    def __init__(self, first_name, last_name, package):
        self.first_name = first_name
        self.last_name = last_name
        self.package = package

    def give_raise(self, amount=5000):
        self.package += amount