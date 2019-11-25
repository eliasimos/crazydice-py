# Random number generator and game with prizes

import random

die1 = (random.randint(1,6)) #print outcome
die2 = (random.randint(1,6)) #print outcome

you_rolled = 'You rolled {} and {}'.format (die1, die2)

if die1 == die2 and die1+die2 == 10:
  result = 'Bravo! You won $100!'
elif die1 == die2 and die1+die2 == 12:
  result = 'Bravo! You won 1,000,000 XRP! It will soon be worth nothing, so hurry up and cash out!'
elif die1 == die2:
  result = 'You win $1 - but you can do better!'
else:
  result = 'Not this time...try again!'

print ('*** Welcome to CRAZY DICE! ***')
print (' ')
print ('Roll the dice and win special prizes!')
print ('The rules are simple; roll doubles and WIN! The higher the doubles, the bigger the prize!')
print (' ')
print (you_rolled)
print (' ')
print (result)
