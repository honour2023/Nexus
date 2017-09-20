class School:

    def __init__(self, eits, fellows):
        self.__eits = eits
        self.__fellows = fellows

class Person:

    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Eit(Person):

    def __init__(self, name, nationality, fun_facts):
        super().__init__(name,nationality)
        self.__name = name
        self.__nationality = nationality
        self.__fun_facts = fun_facts

class Fellow(Person):

    def __init__(self, name, nationality, happiness_level = 5):
        super().__init__(name, nationality)
        self.__happiness_level = happiness_level


    def eat(self,happiness_level):
        happiness_level += 1

    def teach(self,happiness_level):
        happiness_level -= 1

eit = Fellow("ibrahim", "NG")
eit.name = input("what is your name: ")
eit.nationality = input("which country do you come from: ")
print(eit.name + " is an EIT from" + eit.nationality)