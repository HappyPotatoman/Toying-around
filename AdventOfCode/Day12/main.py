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
  matrix, start = read('input.txt', [])
  m, n = len(matrix), len(matrix[0])
  q = [(start, 1)]
  visited = set()
  while q:
    coords, s = q.pop(0)
    r, c = coords
    currentElevation = matrix[r][c]
    for dr, dc in directions:
      nr, nc = r + dr, c + dc
      if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] == 'E' and (currentElevation == 'z' or currentElevation == 'y'):
        print(s)
        return
      elif 0 <= nr < m and 0 <= nc < n and ord(matrix[nr][nc]) <= ord(currentElevation) + 1 and (nr, nc) not in visited:
        visited.add((nr, nc))
        q.append(((nr, nc), s + 1))
      
if __name__ == '__main__':
  main()