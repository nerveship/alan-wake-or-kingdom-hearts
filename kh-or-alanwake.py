import os
import sys
import random

with open(os.path.join(sys.path[0], "alanwake.txt"), "r", encoding='utf8') as txt1:
    wake = []
    for line in txt1:
        wake.append(line)

with open(os.path.join(sys.path[0], "kh.txt"), "r", encoding='utf8') as txt2:
    kh = []
    for line in txt2:
        kh.append(line)

random_kh = random.choice(kh)
random_wake = random.choice(wake)
choices = [random_kh, random_wake]
quote = random.choice(choices)

print(quote)
print("Is this quote from Kingdom Hearts or Alan Wake?")
inp = input().lower()

if quote == choices[0] and inp == "kingdom hearts":
    print("Correct!")
elif quote == choices[1] and inp == "alan wake":
    print("Correct!")
else:
    print("Incorrect!")