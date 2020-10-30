from recordclass import recordclass
import jinja2

# https://jinja.palletsprojects.com/en/2.11.x/

fields = "id cognome nome".split()

data = """
10 manini luca
15 voltolini francesca
20 serafini maria
"""
data = [s.split()
        for s in data.split("\n")
        if s.strip()]

Person = recordclass("Person", fields)

people = [Person(*r) for r in data]
for p in people:
    print(p)
