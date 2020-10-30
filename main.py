import jinja2

# https://jinja.palletsprojects.com/en/2.11.x/

data = """
id cognome nome
10 manini luca
15 voltolini francesca
20 serafini maria
"""
data = [s.split()
        for s in data.split("\n")
        if s.strip()]

for r in data:
    print(r)
