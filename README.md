## 🎰 Python Slot Machine Game

A simple, interactive command-line slot machine game written in Python.
Players can deposit money, choose how many lines to bet on, place their bets, spin the machine, and win based on matching symbols across rows.

This project demonstrates Python fundamentals such as functions, loops, validation,<br>
randomization, and simple game logic.


## 🕹️ Features

- 💰 Deposit system to set your starting balance

- 🎯 Betting on 1–3 lines

- 🎞️ Randomly generated 3×3 slot machine grid

- 🏆 Winnings calculated based on matching symbols

- 📉 Automatic balance updates after each game

- 🔁 Play as many rounds as you want

- ❌ Quit anytime by pressing q


### 📦 Requirements

- Python 3.x
- No external libraries required (uses only built-in modules)


## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/slot-machine-game.git
cd slot-machine-game
```

2. Run the game:
```bash
python slot_machine.py
```
## 🎮 Game Rules
#### 1. Deposit

You start by choosing how much money to deposit into your balance.

#### 2. Choose Lines

You can bet on 1 to 3 horizontal lines.

#### 3. Place Bet

You choose how much money to bet per line
(min: $1, max: $100).

#### 4. Spin!

The machine generates random symbols in a 3×3 grid.
If all symbols in a chosen line match, you win:

| Symbol | Count in Pool | Value (Multiplier) |
| ------ | ------------- | ------------------ |
| A      | 2             | 5×                 |
| B      | 4             | 4×                 |
| C      | 6             | 3×                 |
| D      | 8             | 2×                 |

#### 5. Winnings

Your winnings are added to your balance automatically.


## 🧠 Code Structure

- The project is organized into functions:

- deposite() — get starting balance

- get_lines_of_bet() — choose number of lines

- bet_lines() — choose bet amount

- get_slot_machin_spin() — generate the slot columns

- check_winnings() — check for matches & calculate payout

- spin() — one round of the game

- main() — game loop

### 📸 Example Gameplay
```bash
What amount Would You like to set as your balance? $50
Your current balance is $50
Press any key to play (q to quit):

Enter the lines would you like to bet on? 1-3: 3
How many dollars do you want to bet on the lines? $5
Your betting 5 on 3 lines, total bet is $15

A|C|B
A|A|A
D|C|D

You won 15$
You won on lines: 1
```

### 🤝 Contributing

Pull requests are welcome!
If you'd like to fix bugs or add improvements (like animations or color), feel free to contribute.


### 📄 License

This project is open-source under the MIT License.















