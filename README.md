# AI_Puzzle_Solver
# 8-Puzzle Solver: Comparing Functional and Imperative Paradigms

This project demonstrates the implementation of an AI-based solution for solving the **8-Puzzle** problem using **two programming paradigms**:
1. **Imperative Programming**  
2. **Functional Programming**  

By solving the same problem in both paradigms, the project highlights their differences in terms of design, implementation, and performance.  

---

## Key Features

### Imperative Paradigm
- **Mutable State**: Puzzle states are directly modified during transitions.
- **Control Structures**: Uses `for` loops and `if-else` conditions to control flow.
- **Straightforward Logic**: Easier to implement and understand for step-by-step instructions.
- **Performance**: Computationally efficient but less modular.

### Functional Paradigm
- **Immutability**: Puzzle states remain unchanged; new states are generated.
- **Recursion**: Replaces loops with recursive calls for transitions and search.
- **First-Class and Higher-Order Functions**: Functions are passed as arguments and composed.
- **Complexity**: More abstract and challenging to implement, but aligns with modern functional programming principles.

---

## Paradigm Comparison

| Feature                 | Imperative                     | Functional                     |
|-------------------------|---------------------------------|--------------------------------|
| **State Management**    | Mutable                       | Immutable                     |
| **Control Structures**  | Loops, Conditions             | Recursion, Function Composition |
| **Ease of Use**         | Simple                        | Complex                       |
| **Performance**         | Efficient                     | Depends on recursion depth    |
| **Scalability**         | Moderate                      | High                          |

---

### Why Functional was Challenging?
The **functional approach** required a shift in mindset:
- Avoiding **loops** and **conditions** entirely.
- Implementing **recursion** for control flow.
- Designing code with **pure functions** and **immutability**.
  
Thanks to functional programming concepts, the code became modular, reusable, and aligned with modern software practices, but at the cost of increased complexity.
