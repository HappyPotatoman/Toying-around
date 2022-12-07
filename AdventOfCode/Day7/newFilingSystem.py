class FilingSystem:
  def __init__(self, input):
    self.input = input
    self.root = {}
    self.listing = False
    self.path = []

    with open(self.input) as f:
      for line in f:
        l = line.rstrip().split()

        if l[0] == '$':
          self.listing = False
          if l[1] == 'cd':
            if l[2] == '..': self.path.pop()
            elif l[2] == '/': self.path = ['/']
            else: self.path.append(l[2] + "/")
          
          elif l[1] == 'ls': self.listing = True
        
        elif self.listing:
          if l[0] == 'dir': pass
          else:
            path = []
            for p in self.path:
              path.append(p)
              relative_path = ''.join(path)
              if relative_path not in self.root:
                self.root[relative_path] = int(l[0])
              else:
                self.root[relative_path] += int(l[0])

    # Task one - sum of all directories with less than 100,000 bytes
    small_directories = [val for val in self.root.values() if val <= 100_000]
    print(f'Sum of all directories: {sum(small_directories)}')
    
    # Task two - smallest directory that can be deleted to free up 30,000,000 bytes
    sortedDirectories = sorted(self.root.values())
    freeSpace = 70_000_000 - self.root["/"]
    requiredSpace = 30_000_000
    minimumReqSpace = abs(freeSpace - requiredSpace)
    print(f'Minimum required space: {minimumReqSpace} bytes')

    for dir in sortedDirectories:
      if dir >= minimumReqSpace:
        print(f'The smallest directory that you can delete to free up enough space is {dir} bytes')
        break

if __name__ == '__main__':
  fs = FilingSystem('input.txt')