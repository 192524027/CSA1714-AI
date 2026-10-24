"""
Experiment 4: Cryptarithmetic Problem
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

from itertools import permutations

def solve_cryptarithmetic():
    unique_letters = tuple("SENDMORY")
    
    for digit_perm in permutations(range(10), len(unique_letters)):
        mapping = dict(zip(unique_letters, digit_perm))
        
        # Leading letters cannot be zero
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue
            
        send = (mapping['S'] * 1000 +
                mapping['E'] * 100 +
                mapping['N'] * 10 +
                mapping['D'])
                
        more = (mapping['M'] * 1000 +
                mapping['O'] * 100 +
                mapping['R'] * 10 +
                mapping['E'])
                
        money = (mapping['M'] * 10000 +
                 mapping['O'] * 1000 +
                 mapping['N'] * 100 +
                 mapping['E'] * 10 +
                 mapping['Y'])
                 
        if send + more == money:
            print("Solution:", mapping)
            print(f"{send} + {more} = {money}")
            break

if __name__ == "__main__":
    solve_cryptarithmetic()
