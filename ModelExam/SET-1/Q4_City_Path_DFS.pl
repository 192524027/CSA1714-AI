% Connected city facts
connected(chennai, kancheepuram).
connected(chennai, vellore).
connected(kancheepuram, vellore).
connected(vellore, bangalore).
connected(vellore, salem).
connected(salem, bangalore).
connected(salem, coimbatore).

% Undirected road connection
edge(X, Y) :- connected(X, Y).
edge(X, Y) :- connected(Y, X).

% Depth-First Search with backtracking
find_path(Start, Goal, Path) :-
    dfs(Start, Goal, [Start], RevPath),
    reverse(RevPath, Path).

dfs(Goal, Goal, Visited, Visited).
dfs(Current, Goal, Visited, Path) :-
    edge(Current, Next),
    \+ member(Next, Visited),
    dfs(Next, Goal, [Next|Visited], Path).
