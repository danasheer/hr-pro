from datetime import date

class Employee:
    def __init__(self, name, age, salary, year,):
          self.name = name
          self.age = age 
          self.salary= salary
          self.year = year
        
    def get_working_years(self ):
        employment_year=( date.today() - date(year=self.year,month=1,day=1))/365
        return employment_year
    
    def __str__(self) :
        return (self.name, self.age, self.salary, self.year)
         
         
class Manager(Employee):
    def __init__(self, name, age, salary, year, bonus):
         self.name = name 
         self.age = age 
         self.salary = salary
         self.year = year
         self.bonus = bonus
    
    def get_bonus(self, salary,bonus):
        bonus = salary*bonus
        return bonus

print( Employee("dana",27,1000,2019))
def main():
    employees = [
        Employee('dana',27,1000, 2019),
        Employee('sara',28,1000, 2020),
        Employee('nada',27,1000, 2023),
        
    ]

    # print((Employee.get_working_years()))

if __name__ == '__main__':
	main()
