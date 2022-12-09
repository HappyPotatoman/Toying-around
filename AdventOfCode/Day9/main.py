
def move(x, direction):
  if direction == 'R':
    x[0] += 1
  elif direction == 'L':
    x[0] -= 1
  elif direction == 'U':
    x[1] += 1
  elif direction == 'D':
    x[1] -= 1

def evaluate_tail_position():
  if head[0] > tail[0] + 1:
    move(tail, 'R')
    if head[1] > tail[1]:
      move(tail,'U')
    elif head[1] < tail[1]:
      move(tail, 'D')

  elif head[0] < tail[0] - 1:
    move(tail, 'L')
    if head[1] > tail[1]:
      move(tail, 'U')
    elif head[1] < tail[1]:
      move(tail, 'D')
  
  elif head[1] > tail[1] + 1:
    move(tail, 'U')
    if head[0] > tail[0]:
      move(tail, 'R')
    elif head[0] < tail[0]:
      move(tail, 'L')
  
  elif head[1] < tail[1] - 1:
    move(tail, 'D')
    if head[0] > tail[0]:
      move(tail, 'R')
    elif head[0] < tail[0]:
      move(tail, 'L')

  # add tail position to set
  if (tail[0], tail[1]) not in tail_trail: 
    tail_trail.add((tail[0], tail[1]))

# Starting position
head = [0,0]
tail = [0,0]
tail_trail = set()

with open('input.txt') as f:
  for line in f:
    l = line.rstrip().split(" ")
    direction, steps = l[0], int(l[1])
    for i in range(steps):
      move(head, direction)
      evaluate_tail_position()

print(f'The tail of the rope has visited: {len(tail_trail)} unique positions.')