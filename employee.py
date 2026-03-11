from dataclasses import dataclass
import datetime


@dataclass
class Employee:
    id: int
    first_name: str
    last_name: str
    birth_date: datetime.date
    base_salary: int
    hire_date: datetime.date
