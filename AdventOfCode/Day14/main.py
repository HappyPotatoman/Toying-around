from itertools import pairwise

task = 2
data = []
x_min, x_max, y_max = float('inf'), 0, 0
with open('test.txt') as f:
  for line in f:
    l = line.rstrip().split(' -> ')
    l = [l.split(',') for l in l]
    data.append(l)
    
    # find boundaries
    for x, y in l:
      x, y = int(x), int(y)
      if x < x_min:
        x_min = x
      if x > x_max:
        x_max = x
      if y > y_max:
        y_max = y
        
  # normalize matrix size in regard to boundaries
  if task != 2:
    tilt = 0
    matrix = [['.' for i in range((x_max - x_min + 1))] for j in range(y_max + 1)]
  else:
    # this is an arbitrary value to make the matrix wider, could be improved
    tilt = 20
    matrix = [['.' for i in range((x_max - x_min + 1) + tilt * 2)] for j in range(y_max + 1 + 2)]
  

  # insert rock positions
  for l in data:
    for i, j in pairwise(l):
      xi, xj, yi, yj = int(i[0]), int(j[0]), int(i[1]), int(j[1])
      if xi == xj:
        if yi <= yj:
          for y in range(yi, yj + 1):
            matrix[y][xi - x_min + tilt] = '#'
        else:
          for y in range(yi, yj - 1, -1):
            matrix[y][xi - x_min + tilt] = '#'
      if yi == yj:
        if xi <= xj:
          for x in range(xi, xj + 1):
            matrix[yi][x - x_min + tilt] = '#'
        else:
          for x in range(xi, xj - 1, -1):
            matrix[yi][x - x_min + tilt] = '#'

  if task == 2:
    for i, _ in enumerate(matrix[-1]):
      matrix[-1][i] = '#'



m, n = len(matrix), len(matrix[0])
count = 0
def pouringSand(x, y, task = 1):
  if 0 > x or x >= m - 1 or 0 > y or y >= n - 1 and task == 1:
    return 'OOB'
  if x == 0 and matrix[x][y] == 'o':
    return 'FULL'
  elif matrix[x + 1][y] == '.':
    pouringSand(x + 1, y)
  elif matrix[x + 1][y] != '.' and matrix[x + 1][y + 1] != '.' and matrix[x + 1][y-1] != '.':
    matrix[x][y] = 'o'
    global count
    count += 1
  elif matrix[x + 1][y] != '.' and matrix[x + 1][y - 1] == '.':
    pouringSand(x + 1, y - 1)
  elif matrix[x + 1][y] != '.' and matrix[x + 1][y + 1] == '.':
    pouringSand(x + 1, y + 1)

run = True
while run:
  if pouringSand(0, 500 - x_min + tilt) == 'OOB':
    run = False
  elif pouringSand(0, 500 - x_min + tilt) == 'FULL':
    run = False
  else:
    pouringSand(0, 500 - x_min + tilt)

for row in matrix:
  print(''.join(row))

print(count)