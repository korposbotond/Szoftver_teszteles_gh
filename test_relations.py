import datetime
import pytest
from relations_manager import RelationsManager

@pytest.fixture
def rm():
    return RelationsManager()

def test_john_doe_data(rm):
    """
    Check if there is a team leader called John Doe whose birthdate is 31.01.1970.
    """
    john = next((e for e in rm.get_all_employees() if e.first_name == "John" and e.last_name == "Doe"), None)
    
    assert john is not None
    assert john.birth_date == datetime.date(1970, 1, 31)
    assert rm.is_leader(john) is True

def test_john_doe_team_members(rm):
    """
    Check if John Doe’s team members are Myrta Torkelson and Jettie Lynch.
    +
    Make sure that Tomas Andre is not John Doe’s team member.
    """
    john = next(e for e in rm.get_all_employees() if e.id == 1)
    team_ids = rm.get_team_members(john)
    
    team_names = [f"{e.first_name} {e.last_name}" for e in rm.get_all_employees() if e.id in team_ids]
    
    assert "Myrta Torkelson" in team_names
    assert "Jettie Lynch" in team_names
    assert "Tomas Andre" not in team_names

def test_gretchen_salary(rm):
    """
    Check if Gretchen Walford’s base salary equals 4000$.
    """
    gretchen = next(e for e in rm.get_all_employees() if e.first_name == "Gretchen")
    assert gretchen.base_salary == 4000

def test_tomas_not_leader(rm):
    """
    Make sure Tomas Andre is not a team leader. Check what happens if you try to retrieve his team members.
    """

    tomas = next(e for e in rm.get_all_employees() if e.first_name == "Tomas")
    assert rm.is_leader(tomas) is False
    
    assert rm.get_team_members(tomas) is None

def test_jude_not_exists(rm):
    """
    Make sure that Jude Overcash is not stored in the database.
    """
    all_names = [f"{e.first_name} {e.last_name}" for e in rm.get_all_employees()]
    assert "Jude Overcash" not in all_names