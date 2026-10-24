"""
Experiment 13: Minimax Algorithm for Game Trees
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

def minimax(current_depth, is_maximizer, leaf_scores=None, target_depth=3):
    if leaf_scores is None:
        leaf_scores = [3, 5, 2]
        
    if current_depth == target_depth:
        return 0
        
    if is_maximizer:
        optimal_val = float('-inf')
        for val in leaf_scores:
            optimal_val = max(optimal_val, val)
        return optimal_val
    else:
        optimal_val = float('inf')
        for val in leaf_scores:
            optimal_val = min(optimal_val, val)
        return optimal_val

if __name__ == "__main__":
    best_value = minimax(0, True)
    print("Best score:", best_value)
