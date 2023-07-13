from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List
import random
import json
import asyncio

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class Game_of_Life:
  def __init__(self, n: int, rounds: int) -> None:
    self.n = n
    self.arr = [[0 if random.randint(1,100) >= 70 else 1 for _ in range(n)] for __ in range(n)]
    self.rounds = rounds
    self.dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]

  def simulate(self):
    newArr = [[0 for _ in range(self.n)] for __ in range(self.n)]
    
    for i in range(self.n):
      for j in range(self.n):
        num_neighbours = self.count_neighbours(i, j)
        if self.arr[i][j] and num_neighbours < 2:
          newArr[i][j] = 0
        elif self.arr[i][j] and 2 <= num_neighbours <= 3:
          newArr[i][j] = 1
        elif self.arr[i][j] and num_neighbours > 3:
          newArr[i][j] = 0
        elif not self.arr[i][j] and num_neighbours == 3:
          newArr[i][j] = 1
    
    self.arr = newArr
        
  def count_neighbours(self, r, c):
    count = 0
    for dr, dc in self.dirs:
      row = r + dr
      col = c + dc

      if 0 <= row < self.n and \
      0 <= col < self.n and \
      self.arr[row][col] == 1:
        count += 1
    
    return count
  
  def display(self):
    for row in self.arr:
      print(''.join('O' if cell else '.' for cell in row))
    print("\n===\n")

@app.websocket("/ws/{grid_size}")
async def websocket_endpoint_without_rounds(websocket: WebSocket, grid_size: int):
    await websocket.accept()
    GoL = Game_of_Life(grid_size, 1)
    while True:
        GoL.simulate()
        await websocket.send_json(GoL.arr)
        await asyncio.sleep(0.001)


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("game.html", {"request": request})
