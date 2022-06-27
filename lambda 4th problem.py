prog_lang = [('Python', 3.8),
            ('Java', 13),
            ('JavaScript', 2019),
            ('Scala', 2.13)]
res = list(filter(lambda x: type(x[1])==int,prog_lang))
print(""+str(res))
