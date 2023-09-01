class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"员工{self.name}的工号是{self.id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def calculate(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, working_day):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.working_day = working_day

    def calculate(self):
        return self.working_day*self.daily_salary

