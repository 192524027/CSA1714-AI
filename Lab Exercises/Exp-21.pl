/*
Experiment 21: Backward Chaining Reasoning System
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
*/

sunny.
warm.

go_outside :-
    sunny,
    warm.

play_cricket :-
    go_outside.

enjoy_day :-
    play_cricket.

backward :-
    enjoy_day.

