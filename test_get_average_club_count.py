"""A3. Test cases for function get_average_club_count from club_functions
"""

from club_functions import get_average_club_count

P2F_1 = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                            'Rebecca Donaldson-Katsopolis'],
       'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
       'Stephanie J Tanner': ['Kimmy Gibbler', 'Michelle Tanner'],
       'Danny R Tanner': ['DJ Tanner-Fuller', 'Jesse Katsopolis',
                          'Joey Gladstone']}

P2C_1 = {'Michelle Tanner': ['Comet Club'],
       'Danny R Tanner': ['Parent Council'],
       'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
       'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
       'Joey Gladstone': ['Comics R Us', 'Parent Council']}


P2F_2 = {
    'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado'],
    'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy'],
    'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'],
    'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy', 'Luke Dunphy'],
    'Alex Dunphy': ['Luke Dunphy'],
    'Cameron Tucker': ['Gloria Pritchett', 'Mitchell Pritchett'],
    'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'],
    'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'],
    'Dylan D-Money': ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'],
    'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', 'Manny Delgado'],
    'Luke Dunphy':
    ['Alex Dunphy', 'Manny Delgado', 'Mitchell Pritchett', 'Phil Dunphy']}

P2C_2 = {'Claire Dunphy': ['Parent Teacher Association'],
         'Manny Delgado': ['Chess Club'],
         'Mitchell Pritchett': ['Law Association'],
         'Alex Dunphy': ['Chess Club', 'Orchestra'],
         'Cameron Tucker': ['Clown School', 'Wizard of Oz Fan Club'],
         'Phil Dunphy': ['Real Estate Association'],
         'Gloria Pritchett': ['Parent Teacher Association']}


def test_empty() -> None:
    """Test get_average_club_count with empty dict"""

    param = {}
    actual = get_average_club_count(param)
    expected = 0
    assert actual == expected


def test_one_person_one_club() -> None:
    """Test get_average_club_count with one person who is in one club."""

    param = {'Claire Dunphy': ['Parent Teacher Association']}
    actual = get_average_club_count(param)
    expected = 1
    assert actual == expected

def test_1() -> None:
    actual = get_average_club_count(P2C_1)
    expected = 1
    assert actual == expected

def test_2() -> None:
    actual = get_average_club_count(P2C_2)
    expected = 1
    assert actual == expected

if __name__ == '__main__':
    import pytest
    pytest.main(['test_get_average_club_count.py'])
