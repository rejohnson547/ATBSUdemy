class House:

    num_of_people = 0
    def __init__(self, name, relation, age, gender):
        self.name = name
        self.relation = relation
        self.age = age
        self.gender = gender

        House.num_of_people += 1

temp = House('Tempest, Davis', 'Roommate', 24, 'Female')
gina = House('Algene, Hines', 'Mother', 52, 'Female')
ej = House('Robert, Johnson', 'Myself', 29, 'Male')
morg = House('Mogan, Watkins', 'Niece', 2, 'Female')
Leah = House('Leah, Watkins', 'Niece', 6, 'Female')
lex = House('Alexis, Watkins', 'Sister', 31, 'Female')

print(temp.age, temp.name)
print(House.num_of_people)
