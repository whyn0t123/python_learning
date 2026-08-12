from random import choice

lottery = ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

prizes = [3, 'b', 8, 'd']

average = 65323

print("If you can win the prize numbers or letters quicker than the average 65323," 
      "you can win a icecream!")

active = True
times = 0

while active:
    my_ticket = []

    for i in range(4):
        random = choice(lottery)    
        my_ticket.append(random)

    times += 1
    
    if my_ticket == prizes:
        active = False

if times < average:
    print(f"It takes you {times} times to win,"
          "less than the average,"
          "so you win a icecream!")
else:
    print(f"It takes you {times} times to win,"
          "more than the average,"
          "so you can't win a icecream.")