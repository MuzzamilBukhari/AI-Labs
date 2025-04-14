class Room:
    def __init__(self, location, status="dirty"):
        self.location = location
        self.status = status

class Environment:
    def __init__(self, agent, n_rooms=3):
        self.rooms = [Room(chr(65 + i)) for i in range(n_rooms)]  # 'A', 'B', 'C', ...
        self.agent = agent
        self.current_index = 0
        self.step = 1
        self.score = 0

    def get_current_room(self):
        return self.rooms[self.current_index]

    def execute_step(self, n):
        for _ in range(n):
            self.display_perception()

            self.agent.sense(self)
            action = self.agent.act()

            # Perform action and update score
            if action == "clean":
                self.get_current_room().status = "clean"
                self.score += 25
            elif action == "right" and self.current_index < len(self.rooms) - 1:
                self.current_index += 1
                self.score -= 1
            elif action == "left" and self.current_index > 0:
                self.current_index -= 1
                self.score -= 1

            # Apply dirty room penalty (-10 per dirty room)
            dirty_penalty = sum(1 for room in self.rooms if room.status == "dirty") * 10
            self.score -= dirty_penalty

            self.display_action(action, dirty_penalty)
            self.step += 1

    def display_perception(self):
        room = self.get_current_room()
        print(f"Step {self.step} - Perception: [{room.status}, {room.location}]")

    def display_action(self, action, dirty_penalty):
        print(f"Action: [{action}]")
        print(f"Score after step {self.step}: {self.score} (Dirty penalty: -{dirty_penalty})")
        print("-" * 40)


class Agent:
    def __init__(self):
        self.environment = None

    def sense(self, env):
        self.environment = env

    def act(self):
        room = self.environment.get_current_room()
        if room.status == "dirty":
            return "clean"

        index = self.environment.current_index
        size = len(self.environment.rooms)

        if index < size - 1:
            return "right"
        else:
            return "left"


# Run the simulation
if __name__ == "__main__":
    agent = Agent()
    env = Environment(agent, n_rooms=7)  # Change number of rooms here
    env.execute_step(15)  # Simulate 15 steps