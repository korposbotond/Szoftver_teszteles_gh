import datetime
from employee import Employee


class RelationsManager:
    def __init__(self):
        self.employee_list = [
            Employee(id=1, first_name="John", last_name="Doe", base_salary=3000,
                     birth_date=datetime.date(1970, 1, 31), hire_date=datetime.date(1990, 10, 1)),

            Employee(id=2, first_name="Myrta", last_name="Torkelson", base_salary=1000,
                     birth_date=datetime.date(1980, 1, 1), hire_date=datetime.date(2000, 1, 1)),

            Employee(id=3, first_name="Jettie", last_name="Lynch", base_salary=1500,
                     birth_date=datetime.date(1987, 1, 1), hire_date=datetime.date(2015, 1, 1)),

            Employee(id=4, first_name="Gretchen", last_name="Watford", base_salary=4000,
                     birth_date=datetime.date(1960, 1, 1), hire_date=datetime.date(1990, 1, 1)),

            Employee(id=5, first_name="Tomas", last_name="Andre", base_salary=1600,
                     birth_date=datetime.date(1995, 1, 1), hire_date=datetime.date(2015, 1, 1)),

            Employee(id=6, first_name="Scotty", last_name="Bomba", base_salary=1300,
                     birth_date=datetime.date(1977, 1, 1), hire_date=datetime.date(2008, 1, 1))
        ]

        # Employee.ID=1 is a team lead and 2, 3 are part of the team
        self.teams = {
            1: [2, 3],
            4: [5, 6]
        }

    def is_leader(self, employee) -> bool:
        return employee.id in self.teams

    def get_all_employees(self) -> list:
        return self.employee_list

    def get_team_members(self, employee: Employee) -> list:
        if self.is_leader(employee):
            member_ids = self.teams[employee.id]
            members = [e.id for e in self.employee_list if e.id in member_ids]

            return members
