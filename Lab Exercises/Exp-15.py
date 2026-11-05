"""
Experiment 15: Decision Tree Algorithm
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

def decision_tree(weather):
    if weather == "Sunny":
        return "No Play"
    elif weather == "Rainy":
        return "No Play"
    else:
        return "Play"

if __name__ == "__main__":
    print("Decision Tree Algorithm")
    weather = input("Enter weather (Sunny/Rainy/Cloudy): ")
    print("Decision:", decision_tree(weather))
