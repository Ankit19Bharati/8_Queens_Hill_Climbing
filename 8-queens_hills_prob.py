import random

class Board:
    def __init__(self, N=8):
        # N is the number of queens (also the size of the board)
        self.N = N
        self.state = self.generate_random_state()
    
    def generate_random_state(self):
        # Generates a random state (placement of queens in one row each)
        return [random.randint(0, self.N-1) for _ in range(self.N)]
    
    def calculate_conflicts(self, state):
        # Calculates the number of attacking pairs of queens
        conflicts = 0
        for i in range(self.N):
            for j in range(i+1, self.N):
                if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                    conflicts += 1
        return conflicts
    
    def get_best_successor(self, state):
        # Generates successors and returns the one with the least conflicts
        best_state = state[:]
        best_conflicts = self.calculate_conflicts(state)
        
        for i in range(self.N):
            for j in range(self.N):
                if state[i] == j:
                    continue
                new_state = state[:]
                new_state[i] = j
                new_conflicts = self.calculate_conflicts(new_state)
                
                if new_conflicts < best_conflicts:
                    best_state = new_state[:]
                    best_conflicts = new_conflicts
        
        return best_state, best_conflicts
    
    def hill_climb(self, max_steps=1000):
        # Basic Hill-Climbing method
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
    
    def hill_climb_with_sideways_moves(self, max_sideways=100, max_steps=1000):
        # Hill-Climbing with sideways moves (allows some moves with equal conflict scores)
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
    
    def random_restart_hill_climb(self, max_restarts=100):
        # Hill-Climbing with random restarts
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


def print_board(state):
    N = len(state)
    board = [["."] * N for _ in range(N)]
    for i in range(N):
        board[state[i]][i] = "Q"
    for row in board:
        print(" ".join(row))
    print()


# Example Usage
if __name__ == "__main__":
    board = Board(N=8)
    
    print("Initial board:")
    print_board(board.state)
    
    print("Running basic Hill-Climbing...")
    final_state, conflicts, steps = board.hill_climb()
    print(f"Final state with {conflicts} conflicts after {steps} steps:")
    print_board(final_state)
    
    print("Running Hill-Climbing with sideways moves...")
    final_state, conflicts, steps = board.hill_climb_with_sideways_moves()
    print(f"Final state with {conflicts} conflicts after {steps} steps:")
    print_board(final_state)
    
    print("Running Hill-Climbing with random restarts...")
    final_state, conflicts, restarts = board.random_restart_hill_climb()
    print(f"Final state with {conflicts} conflicts after {restarts} restarts:")
    print_board(final_state)
