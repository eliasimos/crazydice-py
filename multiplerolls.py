import random

die1 = (random.randint(1,6)) #print outcome
die2 = (random.randint(1,6)) #print outcome
num_games = 2
die1_list = []
die2_list = []
results = []

# 3 rolls of dice
for i in range(num_games):
  die1_list.append(random.randint(1,6))
  die2_list.append(random.randint(1,6))

print ('*** Welcome to CRAZY DICE! ***')
print (' ')
print ('Roll the dice and win special prizes!')
print ('The rules are simple; roll doubles and WIN! The higher the doubles, the bigger the prize!')
print (' ')

# game logic / sequence
for i in range(num_games):
    die1 = die1_list[i]
    die2 = die2_list[i]
    you_rolled = 'Roll #{}: You rolled {} and {}'.format (i+1, die1, die2)
    print (you_rolled)

    # result if game [i]
    if die1 == die2 and die1+die2 == 10:
      results.append(2)
    elif die1 == die2 and die1+die2 == 12:
      results.append(3)
    elif die1 == die2:
      results.append(1)
    else:
      results.append(0)

max_value = max(results)

# payouts
if max_value == 2:
  outcome = 'Bravo! You won $100!'
elif max_value == 3:
  outcome = 'Bravo! You won 1,000,000 XRP! It will soon be worth nothing, so hurry up and cash out!'
elif max_value == 1:
  outcome = 'You win $1 - but you can do better!'
else:
  outcome = 'Not this time...try again!'

print (' ')
print (outcome)
