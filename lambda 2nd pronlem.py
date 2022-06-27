pro_lang = [("python", 3.8),
           ("Java", 13),
           ("JavaScript", 2019),
           ("scala", 2.13)]
pro_lang.sort(key=lambda a: len(a[0]),reverse=True)
print(pro_lang)
