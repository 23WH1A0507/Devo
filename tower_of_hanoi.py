def tower_of_hanoi_recursive(n, source, auxiliary, destination):
    """
    Recursive solution for Tower of Hanoi problem
    Parameters:
        n (int): Number of disks
        source (str): Source rod
        auxiliary (str): Auxiliary rod
        destination (str): Destination rod
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi_recursive(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi_recursive(n - 1, auxiliary, source, destination)

if __name__ == "__main__":
    try:
        num_disks = int(input("Enter the number of disks: "))
        print(f"\nSteps to solve Tower of Hanoi with {num_disks} disks:\n")
        tower_of_hanoi_recursive(num_disks, 'A', 'B', 'C')
    except ValueError:
        print("Please enter a valid integer.")
