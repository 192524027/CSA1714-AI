# CSA1714 - Artificial Intelligence | Model Practical Examination

**Student Name:** Bhuvanesh H  
**Register No:** 192524027  
**Course Code:** CSA1714  
**Course Name:** Artificial Intelligence  
**Examination:** Model Practical Examination  

---

## SET 1 - Overview & Questions

| Q # | Problem Title | Paradigm / Language | Source Code | Proof Screenshot |
| :---: | :--- | :--- | :--- | :--- |
| **Q1** | **Iterative Deepening Depth-First Search (IDDFS)** | Python 3.11 (State-Space Search) | [`Q1_IDDFS.py`](SET-1/Q1_IDDFS.py) | [`Q1_IDDFS.png`](SET-1/Q1_IDDFS.png) |
| **Q2** | **4-Queens Problem using Backtracking** | Python 3.11 (Constraint Search) | [`Q2_4_Queens.py`](SET-1/Q2_4_Queens.py) | [`Q2_4_Queens.png`](SET-1/Q2_4_Queens.png) |
| **Q3** | **Student Database Knowledge Base** | SWI-Prolog 10.0.2 (Logic Database) | [`Q3_Student_Database.pl`](SET-1/Q3_Student_Database.pl) | [`Q3_Student_Database.png`](SET-1/Q3_Student_Database.png) |
| **Q4** | **Depth-First Backtracking for City Path Finding** | SWI-Prolog 10.0.2 (Graph Traversal) | [`Q4_City_Path_DFS.pl`](SET-1/Q4_City_Path_DFS.pl) | [`Q4_City_Path_DFS.png`](SET-1/Q4_City_Path_DFS.png) |

---

### Detailed Question Solutions

#### Question 1: Iterative Deepening Depth First Search (IDDFS)
- **Problem Statement:** Write a Python program to implement Iterative Deepening Depth First Search (IDDFS) for a given state-space graph. Display the path from the initial node to the goal node.
- **Approach:** Combines the space efficiency of Depth-First Search ($O(bd)$ linear memory) with the optimality and completeness of Breadth-First Search. It iteratively executes Depth-Limited Search (DLS) with depth limit $L = 0, 1, 2, 3, \dots$ until the target node is discovered.
- **Sample Execution:**
  - Start Node: `'A'` | Goal Node: `'J'`
  - Path Discovered at Depth Limit = 3: `A -> B -> E -> J` (Cost: 3 steps)

#### Question 2: 4-Queens Problem using Backtracking
- **Problem Statement:** Write a Python program to solve the 4-Queens problem using the Backtracking technique. Display all possible solutions.
- **Approach:** Recursive depth-first backtracking placing non-attacking queens row by row on a $4 \times 4$ chessboard. Checks for column attacks, upper-left diagonal attacks, and upper-right diagonal attacks before placement.
- **Results:** Exactly 2 unique valid configurations found:
  - Solution 1: `[(0, 1), (1, 3), (2, 0), (3, 2)]`
  - Solution 2: `[(0, 2), (1, 0), (2, 3), (3, 1)]`

#### Question 3: Student Database in Prolog
- **Problem Statement:** Write a Prolog program to represent a Student Database with facts: `student(arun, cse, 21)`, `student(bala, it, 22)`, `student(chitra, cse, 20)`, `student(divya, ece, 21)`. Define rules to find students belonging to a particular department and students above a given age.
- **Rules Defined:**
  - `students_in_department(Department, StudentName) :- student(StudentName, Department, _).`
  - `students_above_age(AgeLimit, StudentName, Age) :- student(StudentName, _, Age), Age > AgeLimit.`
- **Verification Queries:**
  - `students_in_department(cse, Name)` $\rightarrow$ `arun`, `chitra`
  - `students_above_age(20, Name, Age)` $\rightarrow$ `arun (21)`, `bala (22)`, `divya (21)`

#### Question 4: Depth-First Backtracking for City Path Finding
- **Problem Statement:** Write a Prolog program to implement Depth-First Backtracking for finding a path between two cities using suitable connected-city facts.
- **Approach:** Models a transportation road network using bidirectional `route/3` facts and implements recursive Depth-First Search with visited-node tracking to avoid infinite cycles. Backtracking enumerates all alternative routes with their respective cumulative route distances.
- **Sample Query:**
  - `find_path(chennai, bangalore, Path, Dist).`
    - Path 1: `[chennai, kancheepuram, vellore, bangalore]` (360 km)
    - Path 2: `[chennai, vellore, bangalore]` (353 km)
