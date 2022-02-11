import matplotlib.pyplot as plt
import random

total = 0
N = 10000


freqs = {}
money = []
trials = []

for i in range(N):
    dice = random.randint(1,6)
    
    if dice in freqs:
        freqs[dice] += 1
    else:
        freqs[dice] = 1
        
    
    if dice in (1, 2, 3):
        total += 2
    elif dice in (4, 5):
        total += 4
    else:
        total -= 6
        
    money.append(total)
    trials.append(i)
        
faces = list(freqs.keys())
freq  = list(freqs.values())

plt.figure(1)
plt.bar(faces, freq)
#plt.show()
plt.figure(2)
plt.plot(trials, money)
plt.show()
print(f'Total: ${total}')

