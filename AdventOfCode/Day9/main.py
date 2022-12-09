def move(x, direction):
  if direction == 'R':
    x[0] += 1
  elif direction == 'L':
    x[0] -= 1
  elif direction == 'U':
    x[1] += 1
  elif direction == 'D':
    x[1] -= 1

def evaluate_tail_position(front_knot, back_knot):
  if front_knot[0] > back_knot[0] + 1:
    move(back_knot, 'R')
    if front_knot[1] > back_knot[1]:
      move(back_knot,'U')
    elif front_knot[1] < back_knot[1]:
      move(back_knot, 'D')

  elif front_knot[0] < back_knot[0] - 1:
    move(back_knot, 'L')
    if front_knot[1] > back_knot[1]:
      move(back_knot, 'U')
    elif front_knot[1] < back_knot[1]:
      move(back_knot, 'D')
  
  elif front_knot[1] > back_knot[1] + 1:
    move(back_knot, 'U')
    if front_knot[0] > back_knot[0]:
      move(back_knot, 'R')
    elif front_knot[0] < back_knot[0]:
      move(back_knot, 'L')
  
  elif front_knot[1] < back_knot[1] - 1:
    move(back_knot, 'D')
    if front_knot[0] > back_knot[0]:
      move(back_knot, 'R')
    elif front_knot[0] < back_knot[0]:
      move(back_knot, 'L')

  # add tail position to set
  if (head[-1][0], head[-1][1]) not in tail_trail: 
    tail_trail.add((head[-1][0], head[-1][1]))

# Starting position
head = [[0,0] for _ in range(10)]
tail_trail = set()

with open('input.txt') as f:
  for line in f:
    l = line.rstrip().split(" ")
    direction, steps = l[0], int(l[1])
    for i in range(steps):
      move(head[0], direction)
      for x in range(len(head)-1):
        evaluate_tail_position(head[x], head[x+1])

print(f'The tail of the rope has visited: {len(tail_trail)} unique positions.')