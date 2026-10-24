"""
Experiment 6: Vacuum Cleaner Agent
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

class VacuumCleanerAgent:
    def __init__(self, room_states=None, initial_position='A'):
        # 1 indicates dirty, 0 indicates clean
        self.environment = room_states if room_states else {'A': 1, 'B': 1}
        self.location = initial_position

    def clean(self):
        while True:
            print("Room", self.location)
            
            # Percept and Act
            if self.environment[self.location] == 1:
                print("Cleaning room", self.location)
                self.environment[self.location] = 0
            
            # Switch position between room A and B
            self.location = 'B' if self.location == 'A' else 'A'
            
            # Goal test: all rooms cleaned
            if self.environment['A'] == 0 and self.environment['B'] == 0:
                break
                
        print("All rooms are clean")

if __name__ == "__main__":
    agent = VacuumCleanerAgent()
    agent.clean()
