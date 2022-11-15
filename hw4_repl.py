import json
import sys
from hw4 import Group

#Task 4-A

#NOTE: When creating path, do not use .\hw4_repl - use python hw4_repl.py example_data.json

#Task 4-B

#for line in sys.argv[1:]:
#    print(line)

#Task 4-C

group_list = []

for arg in sys.argv[1:]:
#for arg in range(1, len(sys.argv)):

    try:
        with open(arg, "r") as json_file:
            person_json = json.load(json_file)
            my_group = Group(person_json) # does not print anything, but runs successfully
            group_list.append(my_group)
    except:
        pass

print(group_list)
#print(group_list[0].people_with_skill)

#Task 4-D

def names_list(skill: str):

    name_list = []

    for group in group_list:
        name_list = name_list + group.people_with_skill(skill)
    
    return set(name_list)

def find_skills():

    skill_name = input("Select a skill ")

    if skill_name == "quit":
        pass

    else:
        try:    
            print(names_list(skill_name))
        except:
            print("Skill not found")
            find_skills()


find_skills()