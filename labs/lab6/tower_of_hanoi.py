def tower_of_hanoi(n, source, target, helper):
    if n == 1:
        print(f"Move disk {n} from {source} to {target}")
        return

    tower_of_hanoi(n - 1, source, helper, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, helper, target, source)


# Example usage
if __name__ == "__main__":
    n = 3  # Number of disks
    tower_of_hanoi(n, 'S', 'D', 'H')  # S is source, D is target, H is helper