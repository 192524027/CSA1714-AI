/*
Experiment 16: Sum of Integers from 1 to N
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
*/

% Sum of integers from 1 to N

sum(0, 0).

sum(N, S) :-
    N > 0,
    N1 is N - 1,
    sum(N1, S1),
    S is N + S1.

