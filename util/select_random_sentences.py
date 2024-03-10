import random

text_file = open("resources/data.txt", "r")
lines = text_file.readlines()

random_list = random.sample(range(0, 999), 10)

# store the following output in resources/data.txt
for i in random_list:
    line = " ".join(lines[i].split())
    print(line)
