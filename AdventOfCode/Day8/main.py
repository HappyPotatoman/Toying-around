def main(input):
  with open(input) as f:
    matrix = []
    for lines in f:
      l = lines.rstrip()
      matrix.append([int(tree) for tree in l])

  seen = set()
  visible = 0
  def dfs(r, c, d, org):
    nonlocal visible
    if (r == len(matrix) - 1 or c == len(matrix[0]) - 1 or r == 0 or c == 0) and org not in seen:
      seen.add(org)
      visible += 1
      return 1
    elif d == 0:
      if matrix[r][c] > matrix[r-1][c]:dfs(r-1, c, 'up', (r,c))
      if matrix[r][c] > matrix[r][c-1]:dfs(r, c-1, 'left', (r,c))
      if matrix[r][c] > matrix[r+1][c]:dfs(r+1, c, 'down', (r,c))
      if matrix[r][c] > matrix[r][c+1]:dfs(r, c+1, 'right', (r,c))
    elif d == 'up' and matrix[org[0]][org[1]] > matrix[r-1][c] and org not in seen:
      dfs(r-1, c, 'up', org)
    elif r + 1 < len(matrix) and d == 'down' and matrix[org[0]][org[1]] > matrix[r+1][c] and org not in seen:
      dfs(r+1, c, 'down', org)
    elif c+1 < len(matrix[0]) and d == 'right' and matrix[org[0]][org[1]] > matrix[r][c+1] and org not in seen:
      dfs(r, c+1, 'right', org)
    elif d == 'left' and matrix[org[0]][org[1]] > matrix[r][c-1] and org not in seen:
      dfs(r, c-1, 'left', org)

  for row in range(len(matrix)):
    for col in range(len(matrix[0])):
      dfs(row, col, 0, (row, col))
  return visible

if __name__ == '__main__':
  print(main('input.txt'))
