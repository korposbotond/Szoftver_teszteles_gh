import datetime
import pytest
from unittest.mock import MagicMock, patch
from employee import Employee
from employee_manager import EmployeeManager

@pytest.fixture
def mock_rm():
    return MagicMock()

@pytest.fixture
def manager(mock_rm):
    return EmployeeManager(mock_rm)

def test_salary_non_leader(manager, mock_rm):
    """Check an employee’s salary who is not a team leader 
    whose hire date is 10.10.1998 and his base salary is 1000$. 
    Make sure the returned value is 3000$ (1000$ + 20 X 100$).
    """
    base_salary = 1000
    hire_date = datetime.date(1998, 10, 10)
    
    emp = Employee(id=10, first_name="Test", last_name="User",
                   birth_date=datetime.date(1970, 1, 1),
                   base_salary=base_salary,
                   hire_date=hire_date)

    mock_rm.is_leader.return_value = False

    
    current_year = datetime.date.today().year
    expected_years = current_year - hire_date.year
    expected_salary = base_salary + (expected_years * 100)

    result = manager.calculate_salary(emp)
    
    assert result == expected_salary

def test_salary_leader_with_team(manager, mock_rm):
    """Check an employee’s salary who is a team leader 
    and his team consists of 3 members. 
    She was hired on 10.10.2008 and has a base salary of 2000$. 
    Validate if the returned value is 3600$ (2000$ + 10 X 100$ + 3 X 200$).
    """

    base_salary = 2000
    hire_date = datetime.date(2008, 10, 10)
    team_count = 3
    
    emp = Employee(id=11, first_name="Leader", last_name="User",
                   birth_date=datetime.date(1970, 1, 1),
                   base_salary=base_salary,
                   hire_date=hire_date)

    mock_rm.is_leader.return_value = True
    mock_rm.get_team_members.return_value = [1, 2, 3]

    current_year = datetime.date.today().year
    expected_years = current_year - hire_date.year
    expected_salary = base_salary + (expected_years * 100) + (team_count * 200)

    result = manager.calculate_salary(emp)
    
    assert result == expected_salary

def test_email_sending(manager, mock_rm):
    """
    Make sure that when you calculate the salary and send an email notification, 
    the respective email sender service is used with the correct information (name and message). 
    You can use the setup from the previous test for the employee.
    """
    emp = Employee(id=1, first_name="John", last_name="Doe", 
                   birth_date=datetime.date(1970, 1, 1), base_salary=3000, 
                   hire_date=datetime.date(2010, 1, 1))
    
    mock_rm.is_leader.return_value = False

    with patch('builtins.print') as mock_print:
        manager.calculate_salary_and_send_email(emp)

        mock_print.assert_called()

        args, kwargs = mock_print.call_args
        actual_message = args[0]

        assert "John Doe" in actual_message
        assert "your salary" in actual_message
        
        salary = manager.calculate_salary(emp)
        assert str(salary) in actual_message