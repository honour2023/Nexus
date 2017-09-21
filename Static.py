# Mr. Todd has bought Andrew a new weave, so now MEST is on a hiring freeze.
# We can only afford to pay for 4 fellows at a time.
# Use a static field to keep track of how many Fellows have been created
# If  a user tries to construct a fifth Fellow, raise an exception
class Mest:
    fellow_created = 0

    def __init__(self, name, country, fun_facts,):
        self.country = country
        self.fun_facts = fun_facts
        self.name = name
        Mest.fellow_created += 1

for i in range(10):
    Mest("name", "country", "fun_facts")
    if Mest.fellow_created <= 4:
        name = input("Enter the name of the fellow you want to hire: ").split()
        country = input("Enter ya country: ").split()
        fun_facts = input("Enter ya mutherfucking fun_facts: ").split()
        print(Mest.fellow_created)

    else:
        print(Mest.fellow_created)
        raise Exception("404,Error you can't add another fellow")

print(Mest.fellow_created)






