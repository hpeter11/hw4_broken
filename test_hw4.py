import pytest
import copy

import hw4 as h4

#Task 1-B

example_person_list = [
    {"name": "Spongebob", "time in group": 2.3, "skills": ["jellyfishing", "frycooking"]},
    {"name": "Sandy", "time in group": 0.2, "skills": ["karate", "science", "breathing"]},
    {"name": "Patrick", "time in group": 2.3, "skills": ["eating", "jellyfishing"]}
]

empty = []

missing_values = [
    {"name": "Spongebob", "time in group": 2.3, "skills": ["jellyfishing", "frycooking"]},
    {"name": "kyle", "time in group": 0, "skills": [""]},
    {"name": "carl", "time in group": 0.4, "skills": []}
]

person1 = {"name": "Todd", "time in group": 5, "skills": ["mayonaise"]}

'''
Similar to @Before in junit, pytest runs this before every test method
'''
def setup_function():
    # set test_group as global so that other methods can find it
    global test_group
    global test_empty1
    global test_empty2
    global test_group_list
    global empty2_list
    global person_list
    global skill_dict
    global empty_person_list

    # copy.deepcopy makes a brand-new copy of example_person_list
    # and every piece of data contained in it on the heap
    test_group = h4.Group(copy.deepcopy(example_person_list))
    # now we can refer to test_group in any test function in this file
    test_empty1 = h4.Group(copy.deepcopy(empty))
    test_empty2 = h4.Group(copy.deepcopy(missing_values))
    test_group_list = copy.deepcopy(test_group.person_list)
    empty2_list = h4.Group(copy.deepcopy(missing_values)).person_list
    person_list = test_group.person_list
    skill_dict = test_group.skill_dict
    empty_person_list = test_empty1.person_list

'''
pytest assertions simply check if boolean expressions evaluate to true
Make sure ALL of your testing functions start with test_ and are in a file that starts with test_!!
'''

def test_add_person():
    '''Tests all edge cases for add person'''
    assert len(person_list) == 3
    test_group.add_person("Todd", 5, ["mayonaise"])
    assert person1 in person_list
    assert len(person_list) == 4
    assert len(empty_person_list) == 0
    test_empty1.add_person("Todd", 5, ["mayonaise"])
    assert empty_person_list[0] == person1
    assert person1 in test_empty1.person_list
    assert len(test_empty1.person_list) == 1

def test_add_skill():
    '''Tests all edge cases for add skill'''
    assert len(person_list[0]["skills"]) == 2
    test_group.add_skill("Spongebob", "yelling")
    assert len(person_list[0]["skills"]) == 3
    assert "yelling" in skill_dict.keys()
    assert len(skill_dict) == 7
    test_group.add_skill("spongebob", "smiling")
    assert test_group.person_has_skill("Spongebob", "smiling") == False
    assert len(person_list[0]["skills"]) == 3
    assert "smiling" not in skill_dict.keys()
    test_group.add_skill("Spongebob", "yelling")
    assert len(person_list[0]["skills"]) == 3
    #assert test_group[0]["skills"] == ["jellyfishing", "frycooking", "yelling"]
    #assert len(test_group_list[0]["skills"]) == 3;
    #test_group.add_skill("Spongebob", "frycooking")
    #assert len(test_group_list[0]["skills"]) == 3;
    #test_group.add_skill("spongebob", "frycooking")
    #assert len(test_group) == 3
    #assert len(test_group_list[0]["skills"]) == 3;

def test_person_has_skill():
    '''Tests all edge cases for add skill'''
    assert test_group.person_has_skill("Spongebob", "frycooking") == True
    assert test_group.person_has_skill("spongebob", "frycooking") == False
    assert test_group.person_has_skill("Spongebob", "Frycooking") == False
    #assert test_group.person_has_skill("Spongebob", "frycooking") == False
    assert test_group.person_has_skill("Spongebob", "fighting") == False
    test_group.add_skill("Spongebob", "fighting")
    #assert test_group.person_has_skill("Spongebob", "fighting") == True

def test_average_length_of_membership():
    '''Tests all edge cases for avg membership'''
    assert test_group.average_length_of_membership() == pytest.approx(4.8 / 3)
    assert test_empty2.average_length_of_membership() == pytest.approx(2.7 / 3)
    assert test_empty1.average_length_of_membership() == 0

def test_measure_progress():
    '''Tests all edge cases for measure progress'''
    assert test_group.measure_progress("Sandy") == 15
    with pytest.raises(LookupError):
        test_group.measure_progress("sandy")
    assert test_empty2.measure_progress("carl") == 0.0
    with pytest.raises(ZeroDivisionError):
        test_empty2.measure_progress("kyle")

def test_n_person_subgroup():
    '''Tests all edge cases for n person subgroup'''
    assert len(test_group.n_person_subgroup(3)) == 3
    assert len(test_group.n_person_subgroup(2)) == 2
    assert len(test_group.n_person_subgroup(0)) == 0
    assert len(test_group.n_person_subgroup(0)) == len([])
    assert len(test_empty1.n_person_subgroup(2)) == 0

def test_people_with_skill():
    '''Tests all edge cases for ppl with skill'''
    assert test_empty1.people_with_skill("Patrick") == []
    test_empty1.add_person("Patrick", 0.0, ["mayonaise"])
    assert "Patrick" in test_empty1.people_with_skill("mayonaise")\

def test_validate_data():
    '''Tests all edge cases for validate data'''
    with pytest.raises(ValueError):
        h4.Group([{"nam": "", "time in group": 0.0, "skills": [""]}])
    with pytest.raises(ValueError):
        h4.Group([{"name": "", "time in grou": 0.0, "skills": [""]}])
    with pytest.raises(ValueError):
        h4.Group([{"name": "", "time in group": 0.0, "skill": [""]}])
    with pytest.raises(ValueError):
        h4.Group([{"name": 10, "time in group": 0.0, "skills": [""]}])
    with pytest.raises(ValueError):
        h4.Group([{"name": "", "time in group": "five", "skills": [""]}])
    with pytest.raises(ValueError):
        h4.Group([{"name": "", "time in group": 0.0, "skills": [1, 2]}])
    