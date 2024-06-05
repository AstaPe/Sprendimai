from paskaita_18.abstraktus2 import Employee


class Vadybininkas(Employee):
    def __init__(self, base_salary: object, bonus: object) -> object:
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_pay(self):
        return self.base_salary + self.bonus

    def get_role(self):
        return "Vadybininkas"


class Inzinierius(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

    def get_role(self):
        return "Inzinierius"


class Stazuotojas(Employee):
    def __init__(self, stipend):
        self.stipend = stipend

    def calculate_pay(self):
        return self.stipend

    def get_role(self):
        return "Stazuotojas"
