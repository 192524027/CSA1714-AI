/*
========================================================================================
CSA1714 - Artificial Intelligence | Model Exam: SET 1 - Question 4
Problem: Depth-First Backtracking for Finding Paths Between Cities
Student Name: Bhuvanesh H
Register No: 192524027
Course: CSA1714 - Artificial Intelligence
========================================================================================
*/

% --- Connected City Facts: connected(CityA, CityB, DistanceInKm) ---
connected(chennai, kancheepuram, 75).
connected(chennai, vellore, 138).
connected(kancheepuram, vellore, 70).
connected(kancheepuram, tiruvannamalai, 112).
connected(vellore, bangalore, 215).
connected(tiruvannamalai, salem, 140).
connected(salem, bangalore, 160).
connected(salem, coimbatore, 165).
connected(coimbatore, kochi, 190).

% --- Bidirectional Route Definition ---
route(City1, City2, Dist) :- connected(City1, City2, Dist).
route(City1, City2, Dist) :- connected(City2, City1, Dist).

% --- Depth-First Search with Backtracking & Loop Avoidance ---
% Top-level predicate
find_path(Start, Goal, Path, TotalDistance) :-
    dfs(Start, Goal, [Start], RevPath, TotalDistance),
    reverse(RevPath, Path).

% Base case: Destination reached
dfs(Goal, Goal, Visited, Visited, 0).

% Recursive Depth-First Backtracking step
dfs(Current, Goal, Visited, FinalPath, TotalDistance) :-
    route(Current, Next, Distance),
    \+ member(Next, Visited),                     % Cycle prevention check
    dfs(Next, Goal, [Next|Visited], FinalPath, SubDistance),
    TotalDistance is Distance + SubDistance.

% --- Interactive Helper: Display all possible paths with distances ---
show_all_paths(Origin, Destination) :-
    format('~nFinding all Depth-First paths between ~w and ~w:~n', [Origin, Destination]),
    writeln('------------------------------------------------------------'),
    forall(find_path(Origin, Destination, Path, Dist),
           (format('Path: ~w | Total Distance: ~w km~n', [Path, Dist]))),
    writeln('------------------------------------------------------------').

% --- Demonstration Query Runner ---
run_demo :-
    writeln('============================================================'),
    writeln('Depth-First Backtracking Path Finding Between Cities'),
    writeln('Student: Bhuvanesh H (192524027)'),
    writeln('============================================================'),
    show_all_paths(chennai, bangalore),
    show_all_paths(chennai, coimbatore),
    writeln('============================================================').
