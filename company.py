#!/usr/bin/python3

''' Creates a python script for new employees '''

class Employee:
	raise_amt = 1.04
	def __init__(self, first_name, last_name, salary):
		self.first_name = first_name
		self.last_name = last_name
		self.salary = salary
		full_name = first_name + ' ' + last_name
		self.full_name = full_name
		self.email = first_name[:1].lower() + last_name.lower() +"@ideo.com"

	def print_name(self):
		return '{} {}'.format(self.first_name, self.last_name)

	def print_email(self):
		return self.email

	def print_salary(self):
		return self.salary

	def increase_salary(self, by_amnt=raise_amt):
		new_sal = self.salary * by_amnt
		self.salary = new_sal
		return new_sal

class Developer(Employee):
	raise_amt = 1.07
	def __init__(self, first_name, last_name, salary, prog):
		super().__init__(first_name, last_name, salary)
		self.prog = prog

class Manager(Employee):
	raise_amt = 1.10
	def __init__(self, first_name, last_name, salary, employees=None):
		super().__init__(first_name, last_name, salary)
		if not employees:
			employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in employees:
			employees.append(emp)

	def remove_emp(self, emp):
		if emp in employees:
			employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print(emp.print_name())



emp1 = Employee("Austin", "Harshberger", 100000)
dev1 = Developer("Mitali", "Sengupta", 80000, "Python")
mgr1 = Manager("Sidney", "Burkett", 110000, [emp1, dev1])

print('Manager:', mgr1.print_name())
print('Employees: ')
mgr1.print_emps()

