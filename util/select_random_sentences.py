import random

text_file = open("resources/data.txt", "r")
lines = text_file.readlines()

random_list = random.sample(range(0, 10267), 100)

for i in random_list:
    print(lines[i], end='')
