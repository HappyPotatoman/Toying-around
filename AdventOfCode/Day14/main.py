from itertools import pairwise

data = []
x_min, x_max, y_max = float('inf'), 0, 0
with open('input.txt') as f:
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
  matrix = [['.' for i in range((x_max - x_min + 1))] for j in range(y_max + 1)]
  

  # insert rock positions
  for l in data:
    for i, j in pairwise(l):
      xi, xj, yi, yj = int(i[0]), int(j[0]), int(i[1]), int(j[1])
      if xi == xj:
        if yi <= yj:
          for y in range(yi, yj + 1):
            matrix[y][xi - x_min] = '#'
        else:
          for y in range(yi, yj - 1, -1):
            matrix[y][xi - x_min] = '#'
      if yi == yj:
        if xi <= xj:
          for x in range(xi, xj + 1):
            matrix[yi][x - x_min] = '#'
        else:
          for x in range(xi, xj - 1, -1):
            matrix[yi][x - x_min] = '#'



m, n = len(matrix), len(matrix[0])
count = 0
def pouringSand(x, y):
  if 0 > x or x >= m - 1 or 0 > y or y >= n - 1:
    return 'OOB'
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

for _ in range(10000):
  if pouringSand(0, 500 - x_min) == 'OOB':
    break
  else:
    pouringSand(0, 500 - x_min)

for row in matrix:
  print(''.join(row))

print(count)