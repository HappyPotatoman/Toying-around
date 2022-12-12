def read(input, output):
  with open(input) as f:
    for line in f:
      l = line.rstrip()
      row = []
      for i, ch in enumerate(l):
        row.append(ch)
        if ch == 'S':
          # swap 'S' for 'a' and save the starting position
          row[i] = 'a'
          start = (len(output), i)
      output.append(row)
  return output, start

def main():
  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  matrix, _ = read('input.txt', [])
  m, n = len(matrix), len(matrix[0])
  possibleRoutes = []
  # BFS for each possible starting position 'a'
  for i in range(m):
    for j in range(n):
      visited = set()
      if matrix[i][j] == 'a':
        q = [((i, j), 1)] # initialize queue as (coords, steps)
        while q:
          coords, s = q.pop(0)
          r, c = coords
          currentElevation = matrix[r][c]
          for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] == 'E' and (currentElevation == 'z' or currentElevation == 'y'):
              possibleRoutes.append(s)
            elif 0 <= nr < m and 0 <= nc < n and ord(matrix[nr][nc]) <= ord(currentElevation) + 1 and (nr, nc) not in visited:
              visited.add((nr, nc))
              q.append(((nr, nc), s + 1))

  print(min(possibleRoutes))
      
if __name__ == '__main__':
  main()