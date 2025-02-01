# PongMaster

A simple **Ping Pong (Pong) Game** developed using Python's **Turtle Graphics** module. This game can be played by two players, where each player controls a paddle to bounce a ball back and forth, trying to prevent the ball from passing their side.

---

## Features
- **Two-player Mode**: Control the left and right paddles.
- **Score System**: Tracks the score of both players.
- **Game Over**: The game ends when a player reaches 5 points.
- **Responsive Controls**: Arrow keys for the right paddle, and 'W'/'S' keys for the left paddle.

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/PongMaster.git
   ```

2. **Install Python (if not already installed)**:  
   [Download and install Python](https://www.python.org/downloads/)

3. **Run the Game**:  
   Navigate to the game directory and run:
   ```bash
   python main.py
   ```

---

## Controls
- **Right Paddle**:  
  - Move Up: `Up Arrow`
  - Move Down: `Down Arrow`
  
- **Left Paddle**:  
  - Move Up: `W`
  - Move Down: `S`

---

## Game Rules
1. The game is played between two players.
2. Players control their paddles using the specified keys.
3. The ball bounces off the walls and paddles.
4. If the ball passes a player's paddle, the opponent earns a point.
5. The first player to score 5 points wins the game.

---

## Game Over
- The game ends when one of the players reaches 5 points.
- A **Game Over** message is displayed with the winner.

---

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
- Python and the Turtle module for making this game possible.
- Inspired by classic Pong games!

---

### Example Structure:

```bash
PongMaster/
│
├── main.py          # The main game file
├── scoreboard.py    # The scoreboard logic
├── paddle.py        # Paddle class for player controls
├── ball.py          # Ball class and behavior
└── README.md        # This file
```

---

