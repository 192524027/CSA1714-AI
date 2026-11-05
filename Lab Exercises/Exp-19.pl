/*
Experiment 19: Planetary Database and Classification
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
*/

planet(mercury, 1).
planet(venus, 2).
planet(earth, 3).
planet(mars, 4).
planet(jupiter, 5).
planet(saturn, 6).
planet(uranus, 7).
planet(neptune, 8).

distance(mercury, 57900000).
distance(venus, 108200000).
distance(earth, 149600000).
distance(mars, 227900000).
distance(jupiter, 778600000).
distance(saturn, 1433500000).
distance(uranus, 2872500000).
distance(neptune, 4495100000).

inner_planet(X) :-
    planet(X, N),
    N =< 4.

outer_planet(X) :-
    planet(X, N),
    N > 4.

