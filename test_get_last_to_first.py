"""A3. Test cases for function get_last_to_first from club_functions
"""

from club_functions import get_last_to_first

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
    """Test get_last_to_first with empty dictionary."""

    param = {}
    actual = get_last_to_first(param)
    expected = {}
    assert actual == expected


def test_one_person_one_friend_same_last() -> None:
    """Test get_last_to_first with one person who has one friend that shares
    the same last name as them."""

    param = {'Clare Dunphy': ['Phil Dunphy']}
    actual = get_last_to_first(param)
    expected = {'Dunphy': ['Clare', 'Phil']}
    assert actual == expected

def test_1() -> None:
    actual = get_last_to_first(P2F_1)
    expected = {'Katsopolis': ['Jesse'],
    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'],
    'Gladstone': ['Joey'],
    'Donaldson-Katsopolis': ['Rebecca'],
    'Gibbler': ['Kimmy'],
    'Tanner-Fuller': ['DJ']}
    assert actual == expected

def test_2() -> None:
    actual = get_last_to_first(P2F_2)
    expected = {'D-Cat': ['Chairman', 'Gilbert'],
     'D-Money': ['Dylan'],
     'Delgado': ['Manny'],
     'Dunphy': ['Alex', 'Claire', 'Haley Gwendolyn', 'Luke', 'Phil'],
     'Pritchett': ['Gloria', 'Jay', 'Mitchell'],
     'Tucker': ['Cameron']}
    assert actual == expected

if __name__ == '__main__':
    import pytest
    pytest.main(['test_get_last_to_first.py'])
