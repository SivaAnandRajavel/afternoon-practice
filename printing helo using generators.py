def unique_letters(my_str):


   unique_characters =""

   for character in my_str:
       if character not in unique_characters:
            unique_characters+=character

   yield unique_characters


for letter in unique_letters('hello'):
   print(letter, end=' ')
