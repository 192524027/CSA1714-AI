# CSA1714 - Artificial Intelligence Laboratory

**Student Name:** Bhuvanesh H  
**Register / Roll No:** 192524027  
**Course Code:** CSA1714  
**Course Name:** Artificial Intelligence  

---

## Repository Structure

```
CSA1714-AI/
├── CO-Assesments/
│   ├── Assignment-1/
│   │   ├── Assignment-1_Bhuvanesh_H.pdf  # Comprehensive Analytical & Experimental Report (PDF)
│   │   ├── hospital_robot_search.py     # Uninformed Search Algorithms & Benchmark Suite
│   │   ├── CO-1 AT-1.pdf                # Problem Statement & Task Specification
│   │   └── Guidelines for preparing Assignments.pdf
│   └── Assignment-2/
│       ├── Assignment-2_Bhuvanesh_H.pdf  # Comprehensive Analytical & Experimental Report (PDF)
│       ├── informed_csp_adversarial.py  # Informed Search, CSP, Alpha-Beta, TSP & Transposition Table
│       ├── Assignment-2.pdf             # Problem Statement & Task Specification
│       └── Guidelines for preparing Assignments.pdf
├── ModelExam/
│   └── SET-1/
│       ├── Q1_IDDFS.py                  # Iterative Deepening DFS (Python)
│       ├── Q2_4_Queens.py              # 4-Queens Backtracking Solver (Python)
│       ├── Q3_Student_Database.pl       # Student Database Knowledge Base (Prolog)
│       └── Q4_City_Path_DFS.pl          # Depth-First City Path Traversal (Prolog)
└── Lab Exercises/
    ├── Exp-1.py  & Exp-1.png   # 8-Puzzle Problem (BFS)
    ├── Exp-2.py  & Exp-2.png   # 8-Queens Problem (Backtracking)
    ├── Exp-3.py  & Exp-3.png   # Water Jug Problem (BFS)
    ├── Exp-4.py  & Exp-4.png   # Cryptarithmetic Problem (SEND + MORE = MONEY)
    ├── Exp-5.py  & Exp-5.png   # Missionaries and Cannibals Problem
    ├── Exp-6.py  & Exp-6.png   # Vacuum Cleaner Reflex Agent
    ├── Exp-7.py  & Exp-7.png   # Breadth-First Search (BFS) on Graph
    ├── Exp-8.py  & Exp-8.png   # Depth-First Search (DFS) on Graph
    ├── Exp-9.py  & Exp-9.png   # Traveling Salesperson Problem (TSP)
    ├── Exp-10.py & Exp-10.png  # A* Search Algorithm
    ├── Exp-11.py & Exp-11.png  # Map Coloring Problem (CSP)
    ├── Exp-12.py & Exp-12.png  # Tic-Tac-Toe Game
    ├── Exp-13.py & Exp-13.png  # Minimax Algorithm for Game Trees
    ├── Exp-14.py & Exp-14.png  # Alpha-Beta Pruning Algorithm
    ├── Exp-15.py & Exp-15.png  # Decision Tree Algorithm
    ├── Exp-16.pl & Exp-16.png  # Sum of Integers from 1 to N (Prolog)
    ├── Exp-17.pl & Exp-17.png  # Name and Date of Birth Database (Prolog)
    ├── Exp-18.pl & Exp-18.png  # Student, Teacher and Subject Code Database (Prolog)
    ├── Exp-19.pl & Exp-19.png  # Planetary Database and Classification (Prolog)
    ├── Exp-20.pl & Exp-20.png  # Forward Chaining Reasoning System (Prolog)
    ├── Exp-21.pl & Exp-21.png  # Backward Chaining Reasoning System (Prolog)
    ├── Exp-22.pl & Exp-22.png  # Towers of Hanoi Problem (Prolog)
    ├── Exp-23.pl & Exp-23.png  # Bird and Flying Ability Knowledge Base (Prolog)
    ├── Exp-24.pl & Exp-24.png  # Family Tree and Relationship Reasoning (Prolog)
    ├── Exp-25.pl & Exp-25.png  # Medical Diagnostic and Diet Suggestion System (Prolog)
    ├── Exp-26.pl & Exp-26.png  # Monkey Banana Problem (Prolog)
    ├── Exp-27.pl & Exp-27.png  # Fruit and Color Knowledge Base (Prolog)
    ├── Exp-28.pl & Exp-28.png  # Best-First Search Algorithm (Prolog)
    ├── Exp-29.pl & Exp-29.png  # Medical Diagnostic Expert System (Prolog)
    ├── Exp-30.py & Exp-30.png  # Linear Regression Algorithm (Python)
    ├── Exp-31.py & Exp-31.png  # K-Nearest Neighbors (KNN) Classification (Python)
    ├── Exp-32.py & Exp-32.png  # Decision Tree Classification (Python)
    ├── Exp-33.py & Exp-33.png  # Sentiment Analysis using TextBlob NLP (Python)
    ├── Exp-34.py & Exp-34.png  # Genetic Algorithm for Optimization (Python)
    ├── Exp-35.py & Exp-35.png  # Support Vector Machine (SVM) Classification (Python)
    ├── Exp-36.py & Exp-36.png  # Principal Component Analysis (PCA) Dimensionality Reduction (Python)
    ├── Exp-37.py & Exp-37.png  # Collaborative Filtering Recommendation System (Python)
    └── Exp-38.py & Exp-38.png  # K-Means Clustering Algorithm (Python)
```

## Course Outcome (CO) Assessments

| Assessment | Outcome | Title | Key Topics Covered | Report & Source |
| :---: | :---: | :--- | :--- | :--- |
| **Assignment 1** | **CO1** | Hospital Medicine-Delivery Robot Uninformed Search Strategy | PEAS formulation, Environment classification, BFS vs UCS vs IDDFS mathematical complexity derivations, Empirical scaling benchmarks, Memory exhaustion threshold, Sensor uncertainty & Belief State search | [Assignment-1 PDF](CO-Assesments/Assignment-1/Assignment-1_Bhuvanesh_H.pdf)<br>[`hospital_robot_search.py`](CO-Assesments/Assignment-1/hospital_robot_search.py) |
| **Assignment 2** | **CO2** | Informed Search, CSP, Adversarial Search & Optimization | UCS vs Greedy Best-First vs A* across map topologies, Online search agent & competitive ratio, Alpha-Beta move ordering, Minimax depth scaling, AC-3 constraint propagation for exam timetabling, TSP Exhaustive vs 2-Opt local search, Day-4 Transposition Table caching redesign | [Assignment-2 PDF](CO-Assesments/Assignment-2/Assignment-2_Bhuvanesh_H.pdf)<br>[`informed_csp_adversarial.py`](CO-Assesments/Assignment-2/informed_csp_adversarial.py) |

## Model Practical Examination

| Set | Question | Problem Description | Implementation | Source Code |
| :---: | :---: | :--- | :--- | :--- |
| **SET 1** | **Q1** | **Iterative Deepening Depth First Search (IDDFS)** for state-space graph | Python 3.11 | [`Q1_IDDFS.py`](ModelExam/SET-1/Q1_IDDFS.py) |
| **SET 1** | **Q2** | **4-Queens Problem** using Backtracking technique | Python 3.11 | [`Q2_4_Queens.py`](ModelExam/SET-1/Q2_4_Queens.py) |
| **SET 1** | **Q3** | **Student Database Knowledge Base** with Department & Age rules | SWI-Prolog 10.0.2 | [`Q3_Student_Database.pl`](ModelExam/SET-1/Q3_Student_Database.pl) |
| **SET 1** | **Q4** | **Depth-First Backtracking** for finding paths between connected cities | SWI-Prolog 10.0.2 | [`Q4_City_Path_DFS.pl`](ModelExam/SET-1/Q4_City_Path_DFS.pl) |

## Lab Exercises Overview

| Exp # | Experiment Title | Algorithm / Technique |
| :---: | :--- | :--- |
| **01** | 8-Puzzle Problem | Breadth-First Search (BFS) |
| **02** | 8-Queens Problem | Backtracking |
| **03** | Water Jug Problem | State Space Search (BFS) |
| **04** | Cryptarithmetic Problem | Constraint Satisfaction Search |
| **05** | Missionaries and Cannibals | State Space Search (BFS) |
| **06** | Vacuum Cleaner Agent | Reflex Agent Architecture |
| **07** | Graph Traversal (BFS) | Queue-based Breadth-First Search |
| **08** | Graph Traversal (DFS) | Recursion-based Depth-First Search |
| **09** | Traveling Salesperson Problem | Greedy Nearest Neighbor Heuristic |
| **10** | Pathfinding & Heuristic Search | A* Search Algorithm ($f = g + h$) |
| **11** | Map Coloring | CSP with Backtracking |
| **12** | Adversarial Game Playing | Tic-Tac-Toe Game Engine |
| **13** | Game Tree Decision Making | Minimax Algorithm |
| **14** | Adversarial Search & Pruning | Alpha-Beta Pruning Algorithm |
| **15** | Machine Learning Classification | Decision Tree Algorithm |
| **16** | Prolog Recursion & Arithmetic | Sum of Integers from 1 to N |
| **17** | Prolog Knowledge Base Querying | Date of Birth Database |
| **18** | Prolog Relational Database | Student, Teacher & Subject System |
| **19** | Planetary Facts & Rules | Planetary Distance & Orbit Classification |
| **20** | Expert Systems Reasoning | Forward Chaining Algorithm |
| **21** | Goal-Driven Inference | Backward Chaining Algorithm |
| **22** | Classical Recursion Problem | Towers of Hanoi ($2^n - 1$) |
| **23** | Knowledge Representation | Bird Flying Ability with Negation as Failure |
| **24** | Relational Reasoning | Family Tree & Ancestry Rules |
| **25** | Rule-Based Diagnostic System | Disease & Dietary Recommendation Engine |
| **26** | Monkey Banana Problem | State Space Planning (Prolog) |
| **27** | Fruit and Color Database | Knowledge Base Querying (Prolog) |
| **28** | Best-First Search | Heuristic Search on Graph (Prolog) |
| **29** | Medical Diagnostic System | Knowledge-Based Expert System (Prolog) |
| **30** | Linear Regression | Supervised Continuous Prediction (scikit-learn) |
| **31** | K-Nearest Neighbors (KNN) | Distance-Based Classification (scikit-learn) |
| **32** | Decision Tree Classifier | Information-Theoretic Classification (scikit-learn) |
| **33** | Sentiment Analysis | Natural Language Processing (TextBlob) |
| **34** | Genetic Algorithm | Evolutionary Optimization |
| **35** | Support Vector Machine (SVM) | Maximal Margin Classification (scikit-learn) |
| **36** | Principal Component Analysis | Unsupervised Dimensionality Reduction (PCA) |
| **37** | Collaborative Filtering | User-Based Cosine Similarity Recommender |
| **38** | K-Means Clustering | Unsupervised Centroid Clustering (scikit-learn) |

## Environment
- **Operating System:** Windows 11
- **Python Version:** Python 3.11.9
- **Prolog Environment:** SWI-Prolog 10.0.2
- **IDE / Environment:** Python IDLE (Python 3.11.9) & SWI-Prolog Console

