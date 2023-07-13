# This is a goofin version of the Game of Life. Will see where it goes!

1. Open terminal in directory containing main.py
2. Run command: uvicorn main:app --reload

# Build with docker
1. docker build -t game-of-life-app .
2. docker run -d -p 8000:8000 game-of-life-app