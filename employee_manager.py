import datetime
from employee import Employee
from relations_manager import RelationsManager


class EmployeeManager:
    yearly_bonus = 100
    leader_bonus_per_member = 200

    def __init__(self, relations_manager: RelationsManager):
        self.relations_manager = relations_manager

    def calculate_salary(self, employee: Employee) -> int:
        salary = employee.base_salary

        years_at_company = datetime.date.today().year - employee.hire_date.year

        salary += years_at_company * EmployeeManager.yearly_bonus

        if self.relations_manager.is_leader(employee):
            team_members_count = len(self.relations_manager.get_team_members(employee))
            salary += team_members_count * EmployeeManager.leader_bonus_per_member

        return salary

    def calculate_salary_and_send_email(self, employee: Employee) -> None:
        salary = self.calculate_salary(employee)

        print(f"{employee.first_name} {employee.last_name} your salary: {salary} has been transferred to you.")
        pass


if __name__ == '__main__':
    rm = RelationsManager()
    print(f"All team members: {rm.get_all_employees()}")

    e1 = Employee(id=1, first_name="John", last_name="Doe", base_salary=3000,
                  birth_date=datetime.date(1970, 1, 31), hire_date=datetime.date(1990, 10, 1))
    print(f"Team members for e1: {rm.get_team_members(e1)}")

    em = EmployeeManager(rm)
    em.calculate_salary_and_send_email(e1)
