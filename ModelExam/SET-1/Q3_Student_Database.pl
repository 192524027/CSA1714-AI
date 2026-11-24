/*
========================================================================================
CSA1714 - Artificial Intelligence | Model Exam: SET 1 - Question 3
Problem: Student Database Knowledge Base and Query Rules in Prolog
Student Name: Bhuvanesh H
Register No: 192524027
Course: CSA1714 - Artificial Intelligence
========================================================================================
*/

% --- Student Database Facts: student(Name, Department, Age) ---
student(arun, cse, 21).
student(bala, it, 22).
student(chitra, cse, 20).
student(divya, ece, 21).

% --- Rule 1: Find all students belonging to a particular department ---
students_in_department(Department, StudentName) :-
    student(StudentName, Department, _).

% --- Rule 2: Find all students above a given age threshold ---
students_above_age(AgeLimit, StudentName, Age) :-
    student(StudentName, _, Age),
    Age > AgeLimit.

% --- Interactive Helper: Display all students in a given department ---
display_dept(Dept) :-
    format('Students in ~w Department:~n', [Dept]),
    forall(students_in_department(Dept, Name),
           format('  - ~w~n', [Name])).

% --- Interactive Helper: Display all students above a given age ---
display_above_age(MinAge) :-
    format('Students with Age > ~w:~n', [MinAge]),
    forall(students_above_age(MinAge, Name, Age),
           format('  - ~w (Age: ~w)~n', [Name, Age])).

% --- Demonstration Query Runner ---
run_demo :-
    writeln('======================================================'),
    writeln('CSA1714 Model Exam SET 1: Student Database in Prolog'),
    writeln('Student: Bhuvanesh H (192524027)'),
    writeln('======================================================'),
    nl,
    display_dept(cse),
    nl,
    display_dept(it),
    nl,
    display_above_age(20),
    nl,
    display_above_age(21),
    writeln('======================================================').
