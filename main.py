from recordclass import recordclass
import jinja2 as jinja

# https://jinja.palletsprojects.com/en/2.11.x/
# https://jinja.palletsprojects.com/en/2.11.x/templates/

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
pp = [Person(*r) for r in data]

with open("templates/people.html") as file:
    template = jinja.Template(file.read())

html = template.render(people=pp)

with open("out/people.html", "w") as file:
    file.write(html)
