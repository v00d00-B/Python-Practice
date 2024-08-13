import random

numberOfStreaks = 0
htList = []
Heads = 0
Tails = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails values.
    heads = 0
    tails = 11
    toss = random.randint(0,1)
    toss
    if toss == heads:
        Heads += 1 and Tails == 0
        htList.append(toss)
        if Heads == 6:
            numberOfStreaks += 1
        continue
    else:
        Tails += 1 and Heads == 0
        htList.append(toss)
        if Tails == 6:
            numberOfStreaks += 1
        continue

# Code that checks if there is a streak of 6 heads or tails in a row.
print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
