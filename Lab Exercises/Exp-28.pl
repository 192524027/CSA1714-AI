/*
Experiment 28: Best-First Search Algorithm
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
*/

% Best First Search

edge(a, b, 4).
edge(a, c, 2).
edge(b, d, 5).
edge(c, d, 1).
edge(c, e, 3).
edge(d, f, 2).
edge(e, f, 4).

h(a, 6).
h(b, 4).
h(c, 3).
h(d, 2).
h(e, 2).
h(f, 0).

bestfirst(Start, Goal) :-
    search([[Start]], Goal).

search([[Goal|Path]|_], Goal) :-
    reverse([Goal|Path], Result),
    write(Result).

search([[Current|Path]|Rest], Goal) :-
    findall([Next,Current|Path],
            (edge(Current, Next, _),
             \+ member(Next, [Current|Path])),
            NewPaths),
    append(Rest, NewPaths, Paths),
    sort_paths(Paths, Sorted),
    search(Sorted, Goal).

sort_paths(Paths, Sorted) :-
    predsort(compare_paths, Paths, Sorted).

compare_paths(Order, [A|_], [B|_]) :-
    h(A, HA),
    h(B, HB),
    compare(Order, HA, HB).
