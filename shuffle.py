import random
txt1 = []
txt2 = []

with open("AggressiveDetection_train.txt","r") as t1, open("AggressiveDetection_train_solution.txt","r") as t2:
    txt1 = t1.read().splitlines()
    txt2 = t2.read().splitlines()
    key = 12345678901234567890
    random.Random(key).shuffle(txt1)
    random.Random(key).shuffle(txt2)


with open("At.txt","w") as t1, open("As.txt","w") as t2:
    for it in txt1: t1.write(it+'\n')
    for it in txt2: t2.write(it+'\n')


