from abc import ABC, abstractmethod

# Room class
class Room:
    def __init__(self, location, status="dirty"):
        self.location = location
        self.status = status

# Abstract Agent class
class Agent(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def sense(self, environment):
        pass

    @abstractmethod
    def act(self):
        pass

# VacuumAgent class
class VacuumAgent(Agent):
    def __init__(self):
        pass

    def sense(self, env):
        self.environment = env

    def act(self):
        if self.environment.currentRoom.status == 'dirty':
            return 'clean'
        if self.environment.currentRoom.location == 'A':
            return 'right'
        return 'left'

# Abstract Environment class
class Environment(ABC):
    @abstractmethod
    def __init__(self, n):
        self.n = n

    @abstractmethod
    def executeStep(self, n=1):
        raise NotImplementedError("action must be defined!")

    @abstractmethod
    def executeAll(self):
        raise NotImplementedError("action must be defined!")

# TwoRoomVacuumCleanerEnvironment class
class TwoRoomVacuumCleanerEnvironment(Environment):
    def __init__(self, agent):
        self.r1 = Room('A', 'dirty')
        self.r2 = Room('B', 'dirty')
        self.agent = agent
        self.currentRoom = self.r1
        self.delay = 1000
        self.step = 1
        self.action = ""

    def executeStep(self, n=1):
        for _ in range(n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res

            if res == 'clean':
                self.currentRoom.status = 'clean'
            elif res == 'right':
                self.currentRoom = self.r2
            else:
                self.currentRoom = self.r1

            self.displayAction()
            self.step += 1

    def executeAll(self):
        pass  # Optional

    def displayPerception(self):
        print(f"Perception at step {self.step} is [{self.currentRoom.status}, {self.currentRoom.location}]")

    def displayAction(self):
        print(f"------- Action taken at step {self.step} is [{self.action}]")

# Main execution
if __name__ == '__main__':
    vcagent = VacuumAgent()
    env = TwoRoomVacuumCleanerEnvironment(vcagent)
    env.executeStep(10)