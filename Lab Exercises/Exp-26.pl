/*
Experiment 26: Monkey Banana Problem
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
*/

% Monkey Banana Problem

move(state(middle, onbox, middle, hasnot),
     grasp,
     state(middle, onbox, middle, has)).

move(state(P, onfloor, P, H),
     climb,
     state(P, onbox, P, H)).

move(state(P1, onfloor, P1, H),
     push(P1, P2),
     state(P2, onfloor, P2, H)).

move(state(P, onfloor, B, H),
     walk(P, B),
     state(B, onfloor, B, H)).

solve(state(_, _, _, has), []).

solve(State1, [Action|Actions]) :-
     move(State1, Action, State2),
     solve(State2, Actions).

start :-
     solve(state(door, onfloor, middle, hasnot), Plan),
     write(Plan).
