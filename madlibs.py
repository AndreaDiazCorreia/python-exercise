# This code is creating a Mad Libs game using Python. It prompts the user to enter an adjective, two
# verbs, and a famous person's name. Then, it uses these inputs to create a sentence using string
# interpolation. Finally, it prints out the completed Mad Libs sentence.

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("famous person: ")

madlib= f"Computer programming is son {adj}! It make me so excited all the time because \ I love to {verb1}. Stay hydrated and {verb2} like you ar {famous_person}!"

print(madlib)