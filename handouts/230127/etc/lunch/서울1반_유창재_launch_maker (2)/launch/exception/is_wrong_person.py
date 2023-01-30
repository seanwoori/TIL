def is_wrong_person(person_lst, launch_person_lst):
    for person in person_lst:
        if person not in launch_person_lst:
            return True
    else:
        return False
        