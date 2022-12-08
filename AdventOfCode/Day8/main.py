def main(input):
  with open(input) as f:
    matrix = []
    for lines in f:
      l = lines.rstrip()
      matrix.append([int(tree) for tree in l])

  counts = {}
  for row in range(len(matrix)):
    for col in range(len(matrix[0])):
      org = (row, col)
      counts[org] = list()
      # UP
      count = 1
      while row >= 0:
        if row == 0:
          counts[org].append(count - 1)
          break
        row -= 1
        if matrix[org[0]][org[1]] > matrix[row][col]:
          count += 1
        else:
          counts[org].append(count)
          break
      # DOWN
      row, col = org[0], org[1]
      count = 1
      while row <= len(matrix) - 1:
        if row == len(matrix) - 1:
          counts[org].append(count - 1)
          break
        row += 1
        if matrix[org[0]][org[1]] > matrix[row][col]:
          count += 1
        else:
          counts[org].append(count)
          break
      # LEFT
      row, col = org[0], org[1]
      count = 1
      while col >= 0:
        if col == 0:
          counts[org].append(count - 1)
          break
        col -= 1
        if matrix[org[0]][org[1]] > matrix[row][col]:
          count += 1
        else:
          counts[org].append(count)
          break
      # RIGHT
      row, col = org[0], org[1]
      count = 1
      while col <= len(matrix[0]) - 1:
        if col == len(matrix[0]) - 1:
          counts[org].append(count - 1)
          break
        col += 1
        if matrix[org[0]][org[1]] > matrix[row][col]:
          count += 1
        else:
          counts[org].append(count)
          break

  highestScore = 0
  for _, value in counts.items():
    score = 1
    for v in value:
      score *= v
    if score > highestScore:
      highestScore = score
  return highestScore
    

if __name__ == '__main__':
  print(f'Highest score:', main('input.txt'))
