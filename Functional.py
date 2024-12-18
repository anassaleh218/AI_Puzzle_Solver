from copy import deepcopy

def manhattan_distance(state, goal, i=0, j=0, total=0):
    """
    Recursive Manhattan distance calculator without loops or conditions.
    """
    if i == len(state):  
        return total
    
    value = state[i][j]
    goal_index = goal.index(value) if value != 0 else -1

    new_total = total + (abs(i - goal_index // 3) + abs(j - goal_index % 3)) if value != 0 else total

    return manhattan_distance(state, goal, i + 1, 0, new_total) if j == len(state[i]) - 1 \
           else manhattan_distance(state, goal, i, j + 1, new_total)



def find_empty_tile(state, i=0):
    """
    Recursively find the position of the empty tile (0).
    """
    return (i, state[i].index(0)) if 0 in state[i] else find_empty_tile(state, i + 1)



def move_tile(state, x, y, dx, dy):
    """
    Pure function to move a tile and return a new state.
    """
    new_state = deepcopy(state)
    new_state[x][y], new_state[x + dx][y + dy] = new_state[x + dx][y + dy], new_state[x][y]
    return new_state


def generate_new_states(state, moves=None, index=0, result=None):
    """
    Recursively generate new puzzle states by moving tiles.
    """
    if moves is None:
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if result is None:
        result = []
    
    if index == len(moves):  
        return result
    
    x, y = find_empty_tile(state)
    dx, dy = moves[index]
    if 0 <= x + dx < 3 and 0 <= y + dy < 3:
        result.append(move_tile(state, x, y, dx, dy))
    
    return generate_new_states(state, moves, index + 1, result)


def a_star_search(initial_state, goal_state):
    """
    Recursive A* Search Algorithm following functional paradigm principles.
    """

    
    goal_list = sum(goal_state, [])

    visited = set()


    def search(state, cost, path):
        """
        Inner recursive search function.
        """
       
        state_tuple = tuple(map(tuple, state))
        if state == goal_state:  # Base Case: Solution found
            return path + [state]
        
        if state_tuple in visited:  # Avoid revisiting states
            return None
        visited.add(state_tuple)

        # Generate new states and calculate f(n) = g(n) + h(n)
        new_states = generate_new_states(state)
        scored_states = map(lambda s: (manhattan_distance(s, goal_list) + cost + 1, s), new_states)
        scored_states = sorted(scored_states, key=lambda x: x[0])  # Sort by heuristic score

        # Recursive exploration of each state
        def explore_states(states, index=0):
            if index == len(states):  # Base Case: No solution found in this branch
                return None
            _, next_state = states[index]
            result = search(next_state, cost + 1, path + [state])
            return result if result else explore_states(states, index + 1)

        return explore_states(scored_states)

    return search(initial_state, 0, [])


# Initial and Goal States
initial_state = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Solve Puzzle
solution_path = a_star_search(initial_state, goal_state)

def print_solution(path, step=0):
    if step == len(path):  # Base Case
        return
    print(f"Step {step}:")
    print("\n".join(map(str, path[step])))  
    print()
    print_solution(path, step + 1)

if solution_path:
    print("Solution Found!")
    print_solution(solution_path)
else:
    print("No solution exists.")

