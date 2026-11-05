/*
Experiment 18: Student, Teacher and Subject Code Database
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
*/

student(101, arun).
student(102, ravi).
student(103, kumar).

teacher(t1, ramesh).
teacher(t2, suresh).

subject(s1, c).
subject(s2, python).
subject(s3, java).

sub_code(c, cs101).
sub_code(python, cs102).
sub_code(java, cs103).

handles(ramesh, c).
handles(suresh, python).
handles(ramesh, java).

