import random
from words import group

#chooses one word for both instances of print coming up
chosen = random.choice(group)

# shows the word of the random choice
print('what is the meaning of:', chosen['word'])

#input creates a pause
print(input('Press Enter...'))

# shows the meaning to the ramdom choice
print(chosen['meaning'])