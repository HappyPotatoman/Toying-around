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
            if l[2] == '..':
              self.path.pop()
            elif l[2] == '/':
              self.path = ['/']
            else:
              self.path.append(l[2] + "/")
          
          if l[1] == 'ls':
            self.listing = True
        
        elif self.listing:
          if l[0] == 'dir':
            pass
          else:
            path = []
            for p in self.path:
              path.append(p)
              relative_path = ''.join(path)
              if relative_path not in self.root:
                self.root[relative_path] = int(l[0])
              else:
                self.root[relative_path] += int(l[0])

    small_directories = [val for val in self.root.values() if val <= 100_000]
    print(f'Sum of all directories: {sum(small_directories)}')

if __name__ == '__main__':
  fs = FilingSystem('input.txt')