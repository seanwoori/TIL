SELECT eat, AVG(weight) FROM practice_orms_zoo GROUP BY eat;

def get_zoo_data():

    pets = Pet.objects.all():
    for pet in pets:
        print(pet.eat, pet.weight)