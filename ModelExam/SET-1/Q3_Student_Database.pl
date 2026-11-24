% Student Database

student(arun, cse, 21).
student(bala, it, 22).
student(chitra, cse, 20).
student(divya, ece, 21).

% Rule: Find students belonging to a particular department
dept_student(Dept, Name) :-
    student(Name, Dept, _).

% Rule: Find students above a given age
student_above_age(AgeLimit, Name) :-
    student(Name, _, Age),
    Age > AgeLimit.
