# Model Practical Examination - SET 1

---

## Question 1: Iterative Deepening Depth First Search (IDDFS)

### AIM
To write a Python program to implement Iterative Deepening Depth First Search (IDDFS) for a given state-space graph and display the path from the initial node to the goal node.

### ALGORITHM
1. Define the state-space graph using an adjacency list with an initial node and a goal node.
2. Implement Depth-Limited Search (DLS) to explore nodes recursively up to a specified depth limit while tracking the visited path to prevent cycles.
3. Increment the depth limit iteratively from 0 up to a maximum depth, calling DLS at each level.
4. Stop when the goal node is found and print the complete path from the initial node to the goal node.

### RESULT
The Python program for Iterative Deepening Depth First Search (IDDFS) was executed successfully, and the path from initial node 'A' to goal node 'E' was obtained as `A -> B -> E`.

---

## Question 2: 4-Queens Problem using Backtracking

### AIM
To write a Python program to solve the 4-Queens problem using the Backtracking technique and display all possible solutions.

### ALGORITHM
1. Represent the $4 \times 4$ chessboard and start placing queens row by row from the first row.
2. Check safety for placing a queen at `(row, col)` by verifying that no other queen exists in the same column or along both diagonals.
3. If safe, place the queen in the current row and recursively attempt to place queens in subsequent rows.
4. If a valid configuration of 4 queens is achieved, print the board; otherwise, backtrack by removing the queen and try the next column.

### RESULT
The 4-Queens problem was successfully solved using backtracking in Python, and all 2 possible distinct configurations were obtained and displayed.

---

## Question 3: Student Database in Prolog

### AIM
To write a Prolog program to represent a Student Database with facts and define rules to find students belonging to a particular department and students above a given age.

### ALGORITHM
1. Define the facts representing the student database in the form `student(Name, Department, Age)`.
2. Define the rule `dept_student(Dept, Name)` to retrieve the names of students in a given department.
3. Define the rule `student_above_age(AgeLimit, Name)` using arithmetic comparison to find students with an age greater than the given threshold.
4. Query the Prolog interpreter with department names and age limits to retrieve the matching student records.

### RESULT
The Prolog program for the Student Database was executed successfully, and the queries correctly identified students belonging to a specific department and students above a given age.

---

## Question 4: Depth-First Backtracking for Finding Path Between Cities

### AIM
To write a Prolog program to implement Depth-First Backtracking for finding a path between two cities using suitable connected-city facts.

### ALGORITHM
1. Define the connected cities using facts of the form `connected(CityA, CityB)` and define an undirected relation `edge(X, Y)`.
2. Define the base condition of the depth-first search where the current city matches the destination city.
3. Recursively select an adjacent connected city, checking that it has not been visited already to avoid cycles, and add it to the path.
4. Utilize Prolog's built-in backtracking mechanism to search through paths until a complete route to the goal city is found.

### RESULT
The Prolog program for Depth-First Backtracking between connected cities was executed successfully, and all possible paths between the source and destination cities were displayed.
