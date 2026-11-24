# CSA1714 - Artificial Intelligence | Model Practical Examination (SET 1)

**Student Name:** Bhuvanesh H  
**Register No:** 192524027  
**Course Code:** CSA1714  
**Course Name:** Artificial Intelligence  
**Examination:** Model Practical Examination (SET 1)  

---

## Question 1: Iterative Deepening Depth-First Search (IDDFS)

### AIM
To write and execute a Python program to implement Iterative Deepening Depth First Search (IDDFS) for a given state-space graph and display the path from the initial node to the goal node.

### ALGORITHM
1. **Graph Formulation:** Represent the state-space graph as an adjacency list with starting initial node `'A'` and target goal node `'J'`.
2. **Depth-Limited Exploration:** Implement a recursive Depth-Limited Search (DLS) function that traverses child nodes up to a specified depth bound while maintaining a path list for cycle prevention.
3. **Iterative Depth Increment:** Increment the depth limit $L$ sequentially from $0, 1, 2, \dots$ up to the maximum search depth, invoking DLS at each iteration.
4. **Goal Termination & Path Reconstruction:** Terminate execution immediately upon finding the goal node, output the depth limit at which the solution was found, and print the complete traversal path.

### RESULT
The Iterative Deepening Depth First Search (IDDFS) algorithm was successfully implemented in Python. The goal node `'J'` was discovered at depth limit 3, outputting the optimal solution path: `A -> B -> E -> J` (Path length: 3 steps).

- **Source Code:** [`Q1_IDDFS.py`](Q1_IDDFS.py)  
- **Execution Proof Screenshot:** [`Q1_IDDFS.png`](Q1_IDDFS.png)

---

## Question 2: 4-Queens Problem using Backtracking

### AIM
To write and execute a Python program to solve the 4-Queens problem using the Backtracking technique and display all possible valid chessboard placements.

### ALGORITHM
1. **Board Representation:** Initialize an empty $4 \times 4$ chessboard with dots (`'.'`) and begin placing queens row-by-row starting from row index 0.
2. **Conflict Checking:** Define a safety verification function that checks if placing a queen at `(row, col)` conflicts with existing queens in the same column, upper-left diagonal, or upper-right diagonal.
3. **Recursive Placement:** Place a queen at `(row, col)` when safe and recursively advance to place the remaining queens in the next row (`row + 1`).
4. **Solution Recording & Backtracking:** When all 4 queens are safely placed (`row == 4`), display the full chessboard configuration; otherwise, backtrack by clearing the cell (`'.'`) and testing the next column.

### RESULT
The 4-Queens problem was successfully solved using the Backtracking technique in Python. Exactly 2 distinct non-attacking solutions were identified and displayed with complete row-column coordinates:
- **Solution 1:** Queen positions at `[(0, 1), (1, 3), (2, 0), (3, 2)]`
- **Solution 2:** Queen positions at `[(0, 2), (1, 0), (2, 3), (3, 1)]`

- **Source Code:** [`Q2_4_Queens.py`](Q2_4_Queens.py)  
- **Execution Proof Screenshot:** [`Q2_4_Queens.png`](Q2_4_Queens.png)

---

## Question 3: Student Database Knowledge Base in Prolog

### AIM
To write and execute a Prolog program to represent a Student Database with facts and define inference rules to find students belonging to a particular department and students above a given age.

### ALGORITHM
1. **Knowledge Base Definition:** Represent student records as atomic Prolog facts using the schema `student(Name, Department, Age)` for Arun, Bala, Chitra, and Divya.
2. **Department Filter Rule:** Formulate the inference rule `students_in_department(Dept, Name) :- student(Name, Dept, _)` to retrieve students matching a specific department.
3. **Age Comparison Rule:** Formulate the age-filtering rule `students_above_age(MinAge, Name, Age) :- student(Name, _, Age), Age > MinAge` using numeric relational comparison.
4. **Query Execution & Inference:** Query the Prolog engine to infer and list all student names belonging to specific branches (`cse`, `it`) and those exceeding specified age thresholds ($>20$, $>21$).

### RESULT
The Prolog Student Database program was successfully executed and queried. The department queries correctly returned `arun` and `chitra` for CSE and `bala` for IT; the age threshold queries correctly identified all students aged above 20 (`arun` [21], `bala` [22], `divya` [21]) and above 21 (`bala` [22]).

- **Source Code:** [`Q3_Student_Database.pl`](Q3_Student_Database.pl)  
- **Execution Proof Screenshot:** [`Q3_Student_Database.png`](Q3_Student_Database.png)

---

## Question 4: Depth-First Backtracking for City Path Finding in Prolog

### AIM
To write and execute a Prolog program to implement Depth-First Backtracking for finding all feasible paths and cumulative travel distances between two cities using connected-city facts.

### ALGORITHM
1. **Network Definition:** Define road connections as facts `connected(CityA, CityB, Distance)` and establish symmetric bidirectional connectivity via the rule `route(X, Y, D)`.
2. **Base Case:** Establish the terminal condition `dfs(Goal, Goal, Visited, Visited, 0)` when the destination city is reached with 0 remaining distance.
3. **Recursive DFS with Cycle Avoidance:** Recursively select connected cities, verifying `\+ member(Next, Visited)` to avoid infinite cycles, and accumulate step distances along the branch.
4. **Exhaustive Backtracking Search:** Exploit Prolog's backtracking search to automatically enumerate and print all possible alternative paths between origin and destination cities with their total route distances.

### RESULT
Depth-First Backtracking for city pathfinding was successfully implemented in Prolog. All possible routes between specified pairs of cities (e.g., Chennai to Bangalore via Vellore [353 km] and via Kancheepuram-Vellore [360 km]) were accurately discovered and displayed along with their total travel distances.

- **Source Code:** [`Q4_City_Path_DFS.pl`](Q4_City_Path_DFS.pl)  
- **Execution Proof Screenshot:** [`Q4_City_Path_DFS.png`](Q4_City_Path_DFS.png)
