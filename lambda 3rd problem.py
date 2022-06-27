prog_lang = [('Python', 3.8),
             ('Java', 13),
             ('JavaScript', 2019),
             ('Scala', 2.13)]
print(list(filter(lambda x :'a' in x[0],prog_lang)))
