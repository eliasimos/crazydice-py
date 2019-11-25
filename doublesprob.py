## find the probability of rolling doubles and rolling sixes empirically

import random
import decimal

rolls = {}
roll_num = 1000000
counter_doubles = 0
counter_double_six = 0

for i in range(roll_num):
  die1 = (random.randint(1,6))
  die2 = (random.randint(1,6))
  rolls[i] = (die1, die2)
  if die1 == die2:
    counter_doubles += 1
    if die1 == 6:
      counter_double_six += 1

#print (rolls)
print (" ")
rolls_num = 'The dice were cast {} times'.format(roll_num)
print (rolls_num)
print (" ")
doubles_num = 'There are {} doubles in the sample'.format(counter_doubles)
print (doubles_num)
doublesix_num = 'There are {} double sixes in the sample'.format(counter_double_six)
print (doublesix_num)
