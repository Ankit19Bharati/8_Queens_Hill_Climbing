---

# 8-Queens Problem Solver using Hill-Climbing

This project implements the **8-queens problem** using three variations of the **Hill-Climbing algorithm** in Python. The 8-queens problem is a classic chess puzzle where the objective is to place eight queens on a chessboard such that no two queens can attack each other. Queens can attack along rows, columns, and diagonals.

## Algorithms Implemented:
1. **Basic Hill-Climbing**
2. **Hill-Climbing with Sideways Moves**
3. **Hill-Climbing with Random Restarts**

---

## 1. **Basic Hill-Climbing**
In this variation:
- Start with a random configuration of queens.
- Find the best neighboring configuration (one queen moved to a different row in the same column).
- If the new configuration has fewer conflicts than the current one, move to the new state.
- If no better state is found, the search stops, indicating a local minimum.

**Limitations**: 
- May get stuck in a local minimum, where no improvements can be made.

### Code Example:
```python
def hill_climb(self, max_steps=1000):
    current_state = self.state[:]
    current_conflicts = self.calculate_conflicts(current_state)
    
    steps = 0
    while steps < max_steps:
        next_state, next_conflicts = self.get_best_successor(current_state)
        if next_conflicts >= current_conflicts:
            break
        current_state = next_state
        current_conflicts = next_conflicts
        steps += 1
    
    return current_state, current_conflicts, steps
```

---

## 2. **Hill-Climbing with Sideways Moves**
In this variation:
- Like basic Hill-Climbing, but allows "sideways moves" when the number of conflicts doesn't decrease but remains the same.
- Sideways moves prevent getting stuck in flat local minima.
- There is a limit to the number of sideways moves allowed to avoid infinite loops.

### Code Example:
```python
def hill_climb_with_sideways_moves(self, max_sideways=100, max_steps=1000):
    current_state = self.state[:]
    current_conflicts = self.calculate_conflicts(current_state)
    
    steps = 0
    sideways_moves = 0
    while steps < max_steps:
        next_state, next_conflicts = self.get_best_successor(current_state)
        
        if next_conflicts < current_conflicts:
            current_state = next_state
            current_conflicts = next_conflicts
            sideways_moves = 0
        elif next_conflicts == current_conflicts and sideways_moves < max_sideways:
            current_state = next_state
            sideways_moves += 1
        else:
            break
        steps += 1
    
    return current_state, current_conflicts, steps
```

---

## 3. **Random Restart Hill-Climbing**
In this variation:
- After getting stuck in a local minimum, the algorithm restarts with a new random configuration.
- It repeats this process a limited number of times to try to find a solution with zero conflicts.
- Useful when the problem space has many local minima.

### Code Example:
```python
def random_restart_hill_climb(self, max_restarts=100):
    best_state = self.state[:]
    best_conflicts = self.calculate_conflicts(best_state)
    
    for restart in range(max_restarts):
        state, conflicts, _ = self.hill_climb()
        if conflicts < best_conflicts:
            best_state = state[:]
            best_conflicts = conflicts
        
        if best_conflicts == 0:
            break
    
    return best_state, best_conflicts, restart
```

---

## How the Board is Represented:
- The board is represented as a list of integers, where each index represents a column and the value at that index represents the row in which the queen is placed.
  - Example: `[0, 4, 7, 5, 2, 6, 1, 3]` places a queen in the first column at row 0, in the second column at row 4, and so on.

---

## Running the Code:
To run the code, you can use the following steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the directory:
   ```bash
   cd 8-queens-hills-prob
   ```

3. Run the Python script:
   ```bash
   python main.py
   ```

### Example Output:
The output will display the initial random board, and after applying the different Hill-Climbing algorithms, it will show the final board configurations along with the number of conflicts and the number of steps taken to reach the solution.

---

## Requirements:
- Python 3.x

Make sure you have all the necessary Python packages installed by running:
```bash
pip install -r requirements.txt
```

---

## Author:
- Ankit Kumar Bharati


---