# Write your code here :-)
import random
import sys


htList = []
for experimentNumber in range(10):
    # Code that creates a list of 100 'heads' or 'tails values.
    heads = 0
    tails = 1
    toss = random.randint(0,1)
    if toss == heads:
        htList.append(toss)
        print(htList)
        experimentNumber += 1
        continue
    else:
        htList.append(toss)
        print(htList)
        experimentNumber += 1
        continue

# Code that checks if there is a streak of 6 heads or tails in a row.
print(len(htList))
