""" CSC108 Assignment 3: Club Recommendations - Starter code.

This code is provided solely for the personal and private use of students 
taking the CSC108 course at the University of Toronto. Copying for purposes 
other than this use is expressly prohibited. All forms of distribution of 
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2025 CSC108H1 Teaching Team
"""

from typing import TextIO

import club_example_data

### SAMPLE DATA TO USE IN DOCSTRING EXAMPLES ####

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

## Helper functions

def update_dict(key: str, value: str, 
                key_to_values: dict[str, list[str]]) -> None:
    """Update key_to_values with key/value. If key is in key_to_values,
    and value is not already in the list associated with key,
    append value to the list. Otherwise, add the pair key/[value] to
    key_to_values.

    >>> d = {'1': ['a', 'b']}
    >>> update_dict('2', 'c', d)
    >>> d == {'1': ['a', 'b'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    """

    if key not in key_to_values:
        key_to_values[key] = []

    if value not in key_to_values[key]:
        key_to_values[key].append(value)


## Required functions


def load_profiles(profiles_file: TextIO) -> tuple[dict[str, list[str]],
                                                  dict[str, list[str]]]:
    """Return a two-item tuple containing a "person to friends" dictionary
    and a "person_to_clubs" dictionary with the data from
    profiles_file. 

    >>> data = club_example_data.create_profiles_file_1()
    >>> result = load_profiles(data)
    >>> result == (P2F_1, P2C_1)
    True
    >>> data = club_example_data.create_profiles_file_2()
    >>> result = load_profiles(data)
    >>> result == (P2F_2, P2C_2)
    True
    """
    friends_dict = {}
    clubs_dict = {}
    txt = profiles_file.read().strip()
    blocks = txt.split('\n\n')
    for block in blocks:
        lines = block.split('\n')
        name = lines[0]
        name = ' '.join([sp.strip() for sp in name.split(', ')[::-1]])
        friends = []
        clubs = []
        for i in range(1, len(lines)):
            if ',' in lines[i]:
                subname = lines[i]
                sps = [sp.strip() for sp in subname.split(', ')[::-1]]
                subname = ' '.join(sps)
                friends.append(subname)
            else:
                clubs.append(lines[i])
        friends_dict[name] = sorted(friends)
        clubs_dict[name] = sorted(clubs)
    friends_dict = {friends_dict_key: friends_dict[friends_dict_key]
                    for friends_dict_key in friends_dict
                    if len(friends_dict[friends_dict_key]) > 0}
    clubs_dict = {clubs_dict_key: clubs_dict[clubs_dict_key]
                  for clubs_dict_key in clubs_dict
                  if len(clubs_dict[clubs_dict_key]) > 0}
    return friends_dict, clubs_dict



def get_average_club_count(person_to_clubs: dict[str, list[str]]) -> int:
    """Return the average number of clubs that a person in person_to_clubs
    belongs to, rounded down to the nearest integer (i.e. use // instead of /).

    >>> get_average_club_count(P2C_1)
    1
    >>> get_average_club_count(P2C_2)
    1
    """
    total = 0
    for name in person_to_clubs:
        total += len(person_to_clubs[name])
    if total == 0:
        return 0
    return total // len(person_to_clubs)


def get_last_to_first(
        person_to_friends: dict[str, list[str]]) -> dict[str, list[str]]:
    """Return a "last name to first name(s)" dictionary with the people from the
    "person to friends" dictionary person_to_friends.

    >>> get_last_to_first(P2F_1) == {
    ...    'Katsopolis': ['Jesse'],
    ...    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'],
    ...    'Gladstone': ['Joey'],
    ...    'Donaldson-Katsopolis': ['Rebecca'],
    ...    'Gibbler': ['Kimmy'],
    ...    'Tanner-Fuller': ['DJ']}
    True
    >>> get_last_to_first(P2F_2) == {
    ...     'Pritchett': ['Gloria', 'Jay', 'Mitchell'],
    ...     'Dunphy': ['Alex', 'Claire', 'Haley Gwendolyn', 'Luke', 'Phil'],
    ...     'Delgado': ['Manny'],
    ...     'Tucker': ['Cameron'],
    ...     'D-Money': ['Dylan'],
    ...     'D-Cat': ['Chairman', 'Gilbert']
    ... }
    True
    """
    res = {}
    for name in person_to_friends:
        sp = name.split()
        first = ' '.join(sp[:-1])
        last = sp[-1]
        update_dict(last, first, res)
        for subname in person_to_friends[name]:
            sp = subname.split()
            first = ' '.join(sp[:-1])
            last = sp[-1]
            update_dict(last, first, res)
    for name in res:
        res[name] = sorted(set(res[name]))
    return res


def invert_and_sort(key_to_value: dict[object, object]) -> dict[object, list]:
    """Return key_to_value inverted so that each key in the returned dict
    is a value from the original dict (for non-list values) or each item from a
    value (for list values), and each value in the returned dict
    is a list of the corresponding keys from the original key_to_value.
    The value lists in the returned dict are sorted.

    >>> invert_and_sort(P2C_1) == {
    ...  'Comet Club': ['Michelle Tanner'],
    ...  'Parent Council': ['Danny R Tanner', 'Jesse Katsopolis',
    ...                     'Joey Gladstone'],
    ...  'Rock N Rollers': ['Jesse Katsopolis', 'Kimmy Gibbler'],
    ...  'Comics R Us': ['Joey Gladstone'],
    ...  'Smash Club': ['Kimmy Gibbler']}
    True
    >>> club_to_score = {'Parent Council': 3, 'Smash Club': 2, 'Orchestra': 2}
    >>> invert_and_sort(club_to_score) == {
    ...  3: ['Parent Council'], 2: ['Orchestra', 'Smash Club']}
    True
    """
    res = {}
    for key in key_to_value:
        if type(key_to_value[key]) == list:
            for value in key_to_value[key]:
                update_dict(value, key, res)
        else:
            value = key_to_value[key]
            update_dict(value, key, res)
    for key in res:
        res[key].sort()
    return res



def get_clubs_of_friends(person_to_friends: dict[str, list[str]],
                         person_to_clubs: dict[str, list[str]],
                         person: str) -> list[str]:
    """Return a list, sorted in alphabetical order, of the clubs in
    person_to_clubs that person's friends from person_to_friends
    belong to, excluding the clubs that person belongs to.  Each club
    appears in the returned list once per each of the person's friends
    who belong to it.

    >>> get_clubs_of_friends(P2F_1, P2C_1, 'Danny R Tanner')
    ['Comics R Us', 'Rock N Rollers']
    >>> get_clubs_of_friends(P2F_1, P2C_1, 'Stephanie J Tanner')
    ['Comet Club', 'Rock N Rollers', 'Smash Club']
    """
    res = []
    if person not in person_to_friends:
        return []
    for name in person_to_friends[person]:
        if name in person_to_clubs:
            for club in person_to_clubs[name]:
                res.append(club)
    if person in person_to_clubs:
        res = [subclub for subclub in res
               if subclub not in person_to_clubs[person]]
    res.sort()
    return res


def add_to_clubs(person_to_clubs: dict, clubs: dict, subperson: str) -> None:
    '''
    Increment the count in clubs for each club that subperson belongs to,
    only if that club already exists in clubs.

    person_to_clubs: maps people to the list of clubs they are in.
    clubs: maps club names to integer counts.
    subperson: the person whose clubs should be counted.

    >>> p2c = {'Alice': ['Chess Club', 'Book Club'], 'Bob': ['Book Club', 'Math Club']}
    >>> c = {'Book Club': 0, 'Math Club': 2}
    >>> add_to_clubs(p2c, c, 'Bob')
    >>> c
    {'Book Club': 1, 'Math Club': 3}

    >>> c = {'Chess Club': 5}
    >>> add_to_clubs(p2c, c, 'Bob')
    >>> c
    {'Chess Club': 5}
    '''
    for subclub in person_to_clubs[subperson]:
        if subclub in clubs:
            clubs[subclub] += 1

def recommend_clubs_rule1_branch(person_to_clubs: dict[str, list[str]],
        club_to_persons: dict[str, list[str]],
        clubs: dict, club: str) -> None:
    '''
    For each person in the given club, add to the count in clubs
    the clubs that person belongs to (if person is in person_to_clubs).
    Only clubs already existing in the clubs dict will be incremented.

    person_to_clubs: maps a person to the list of clubs they are in.
    club_to_persons: maps a club to the list of its members.
    clubs: a dictionary mapping club names to integer counts.
    club: the club whose members' other clubs are being counted.

    >>> ptc = {'Alice': ['Book Club', 'Math Club'], 'Bob': ['Book Club'], 'Eve': ['Dance Club']}
    >>> ctp = {'Science Club': ['Alice', 'Eve'], 'Book Club': ['Bob', 'Alice']}
    >>> clubs = {'Math Club': 0, 'Dance Club': 1}
    >>> recommend_clubs_rule1_branch(ptc, ctp, clubs, 'Science Club')
    >>> clubs
    {'Math Club': 1, 'Dance Club': 2}

    >>> clubs = {'Book Club': 0}
    >>> recommend_clubs_rule1_branch(ptc, ctp, clubs, 'Book Club')
    >>> clubs
    {'Book Club': 2}
    '''
    for subperson in club_to_persons[club]:
        if subperson in person_to_clubs:
            add_to_clubs(person_to_clubs, clubs, subperson)

def recommend_clubs_rule1(person_to_clubs: dict[str, list[str]],
        person: str, club_to_persons: dict[str, list[str]],
        clubs: dict) -> None:
    '''
    Apply Rule 1 to recommend clubs: for the given person, look at all the
    clubs they are currently in, find the other people in those clubs, and 
    count how many of those people are in each club (accumulate in clubs dict).

    Only clubs that already exist in the clubs dictionary will be counted.

    person_to_clubs: maps each person to the list of clubs they are in.
    person: the person we are recommending clubs for.
    club_to_persons: maps each club to the list of its members.
    clubs: a dictionary (club name → int) to accumulate scores in-place.

    >>> ptc = {'Alice': ['Book Club', 'Science Club'],
    ...        'Bob': ['Book Club'],
    ...        'Eve': ['Science Club', 'Dance Club']}
    >>> ctp = {'Book Club': ['Alice', 'Bob'],
    ...         'Science Club': ['Alice', 'Eve'],
    ...         'Dance Club': ['Eve']}
    >>> club_counts = {'Dance Club': 0}
    >>> recommend_clubs_rule1(ptc, 'Alice', ctp, club_counts)
    >>> club_counts
    {'Dance Club': 1}

    >>> club_counts = {'Book Club': 0}
    >>> recommend_clubs_rule1(ptc, 'Bob', ctp, club_counts)
    >>> club_counts
    {'Book Club': 2}
    '''
    if person in person_to_clubs:
        for club in person_to_clubs[person]:
            if club in club_to_persons:
                recommend_clubs_rule1_branch(person_to_clubs,
                                             club_to_persons, clubs, club)

def recommend_clubs_rule2(person_to_clubs: dict[str, list[str]],
        person: str, person_to_friends: dict[str, list[str]],
        clubs: dict) -> None:
    '''
    Apply Rule 2 to recommend clubs: for the given person, count the clubs
    that their friends are in (excluding the person's own clubs), and update
    the count in clubs if the club is already in the clubs dictionary.

    person_to_clubs: maps each person to the list of clubs they are in.
    person: the person for whom clubs are being recommended.
    person_to_friends: maps each person to a list of their friends.
    clubs: a dictionary (club name → int) to accumulate scores in-place.

    >>> ptc = {
    ...     'Alice': ['Math Club'],
    ...     'Bob': ['Math Club', 'Book Club'],
    ...     'Eve': ['Book Club', 'Dance Club']
    ... }
    >>> ptf = {
    ...     'Alice': ['Bob', 'Eve']
    ... }
    >>> club_counts = {'Book Club': 0, 'Dance Club': 0}
    >>> recommend_clubs_rule2(ptc, 'Alice', ptf, club_counts)
    >>> club_counts
    {'Book Club': 2, 'Dance Club': 1}

    >>> club_counts = {'Book Club': 0}
    >>> recommend_clubs_rule2(ptc, 'Eve', ptf, club_counts)
    >>> club_counts
    {'Book Club': 0}
    '''
    for club in get_clubs_of_friends(person_to_friends,
                                     person_to_clubs, person):
        if club in clubs:
            clubs[club] += 1

def recommend_clubs(
        person_to_friends: dict[str, list[str]],
        person_to_clubs: dict[str, list[str]],
        person: str, ) -> list[tuple[str, int]]:
    """Return a list of club recommendations for person based on the
    "person to friends" dictionary person_to_friends and the "person
    to clubs" dictionary person_to_clubs using the specified
    recommendation system.

    >>> recommend_clubs(P2F_1, P2C_1, 'Stephanie J Tanner',)
    [('Comet Club', 1), ('Rock N Rollers', 1), ('Smash Club', 1)]
    >>> recommend_clubs(P2F_1, P2C_1, 'Joey Gladstone')
    [('Rock N Rollers', 1)]
    """
    club_to_persons = invert_and_sort(person_to_clubs)
    clubs = {}
    for club in club_to_persons:
        clubs[club] = 0

    recommend_clubs_rule1(person_to_clubs,
                          person, club_to_persons, clubs)

    recommend_clubs_rule2(person_to_clubs,
                          person, person_to_friends, clubs)

    lst = []
    for key in clubs:
        if clubs[key] > 0:
            if (person not in person_to_clubs or
                    key not in person_to_clubs[person]):
                lst.append((-clubs[key], key, clubs[key]))
    lst.sort()
    result = [(key2, value2) for pvalue, key2, value2 in lst]
    return result




# As we learned in class, this is the main block. By guarding the code 
# in this if statement, we make sure these lines are only 
# executed if you run this file directly, but not when this file is 
# imported from another file. More details are on PCRS.

if __name__ == '__main__':
    pass

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    #import doctest
    #doctest.testmod()
