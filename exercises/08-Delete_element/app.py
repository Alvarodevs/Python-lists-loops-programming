people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:

def deletePerson(person_name):
    new_people_list = []
    for x in people:
        if x != person_name:
            new_people_list.append(x)
    return new_people_list
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))