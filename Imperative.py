def find_empty_tile(state):
    for r in range(len(state)):
        for c in range(len(state[r])):
            if state[r][c] == 0:
                return r, c

def is_valid_move(r, c, size):
    return 0 <= r < size and 0 <= c < size

def swap_and_copy(state, r1, c1, r2, c2):
    new_state = []
    for row in state:
        new_state.append(row[:])  # Manual copying of the matrix
    new_state[r1][c1], new_state[r2][c2] = new_state[r2][c2], new_state[r1][c1]
    return new_state

def calculate_heuristic(state, goal):
    size = len(state)
    distance = 0
    for r in range(size):
        for c in range(size):
            value = state[r][c]
            if value == 0:
                continue
            # Manually calculate the target position without using divmod
            goal_r = (value - 1) // size
            goal_c = (value - 1) % size
            distance += abs(r - goal_r) + abs(c - goal_c)
    return distance

def a_star(start, goal):
    size = len(start)
    open_set = [(0, start, [])]  # (priority, state, path)
    visited = []

    while len(open_set) > 0:
        # Manually find the element with the highest priority
        current_index = 0
        for i in range(len(open_set)):
            if open_set[i][0] < open_set[current_index][0]:
                current_index = i
        
        _, current, path = open_set.pop(current_index)

        # Check if the current state is the goal
        if current == goal:
            return path + [current]

        # Prevent revisiting the same state
        current_tuple = tuple(tuple(row) for row in current)
        if current_tuple in visited:
            continue
        visited.append(current_tuple)

        # Generate new states
        empty_r, empty_c = find_empty_tile(current)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Directions: up, down, left, right

        for dr, dc in directions:
            new_r, new_c = empty_r + dr, empty_c + dc
            if is_valid_move(new_r, new_c, size):
                neighbor = swap_and_copy(current, empty_r, empty_c, new_r, new_c)
                new_path = path + [current]
                cost = len(new_path) + calculate_heuristic(neighbor, goal)
                open_set.append((cost, neighbor, new_path))

    return None  # No solution found

def print_puzzle(state):
    for row in state:
        row_str = ""
        for val in row:
            row_str += str(val).rjust(2, " ") + " "
        print(row_str)
    print()

if __name__ == "__main__":
    # Puzzle example
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6],
    ]
    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0],
    ]

    print("Initial state:")
    print_puzzle(initial_state)

    print("Goal state:")
    print_puzzle(goal_state)

    print("Solving the puzzle...")
    solution = a_star(initial_state, goal_state)

    if solution:
        print(f"Solution found in {len(solution) - 1} steps:")
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            print_puzzle(state)
    else:
        print("No solution found.")
