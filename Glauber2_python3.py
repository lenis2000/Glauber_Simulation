import numpy as np

# Set numpy print options
np.set_printoptions(threshold=np.inf)  # np.nan is replaced with np.inf in newer versions

# Constants
n = 30                  # Depth of the interlacing array
sim_steps = 5000        # Number of Glauber steps (times height of the system) per simulation
biga = 50

# Initialize arrays
la = np.zeros((n, n))
laprint = np.zeros((n, n))

# Boundary conditions for hexagon
AAA = n
addition = -AAA/2-1
HOLE_SIZE = 8
OTHER_ADD = 8

# Make a plain hexagon; initial condition speeds up the convergence
for m in range(0, n):
    for j in range(0, m+1):
        if m >= n/2:
            if 0 <= j <= m - n/2:
                la[m][j] = AAA + 1 + addition
            if j >= n/2:
                la[m][j] = 1 + addition

# Main simulation loop
for a in range(0, biga):
    # Write current state to file
    with open(f'outputXX{a}.txt', 'w') as f:
        f.write("{")
        for m in range(0, n):
            f.write("{")
            for k in range(0, n):
                if k == n-1:
                    f.write(str(la[m][k]))
                else:
                    f.write(f"{la[m][k]}, ")
            if m == n-1:
                f.write("}")
            else:
                f.write("},")
        f.write("}")

    print(f"{a} ", end="")  # Updated print statement

    # Simulation steps
    for x in range(1, sim_steps*n):
        m = np.random.randint(1, n)  # Updated from random_integers to randint
        j = np.random.randint(1, m+1)

        # Apply hole conditions
        if m == n/2 - 1 and m/2 - HOLE_SIZE <= j <= m/2 + HOLE_SIZE:
            la[m][j + OTHER_ADD] = OTHER_ADD
        if m < n/2 - 1 and (n/2 - 1)/2 - HOLE_SIZE <= j <= (n/2 - 1)/2 + HOLE_SIZE - (n/2 - 1 - m):
            la[m][j + OTHER_ADD] = OTHER_ADD
        if m > n/2 - 1 and (n/2 - 1)/2 - HOLE_SIZE - (n/2 - 1 - m) <= j <= (n/2 - 1)/2 + HOLE_SIZE:
            la[m][j + OTHER_ADD] = OTHER_ADD

        # Random coin flip and state updates
        coin = np.random.random()
        if coin < 0.5:
            if la[m-1][j-1] < la[m][j-1]:
                if m == 1 or j == 1:
                    la[m-1][j-1] += 1
                else:
                    if la[m-1][j-1] < la[m-2][j-2]:
                        la[m-1][j-1] += 1
        else:
            if la[m-1][j-1] > la[m][j]:
                if m == 1 or j == m:
                    la[m-1][j-1] -= 1
                else:
                    if la[m-1][j-1] > la[m-2][j-1]:
                        la[m-1][j-1] -= 1

    # Final hole conditions update
    for m in range(0, n):
        for j in range(0, n):
            if m == n/2 - 1 and m/2 - HOLE_SIZE <= j <= m/2 + HOLE_SIZE:
                la[m][j + OTHER_ADD] = OTHER_ADD
            if m < n/2 - 1 and (n/2 - 1)/2 - HOLE_SIZE <= j <= (n/2 - 1)/2 + HOLE_SIZE - (n/2 - 1 - m):
                la[m][j + OTHER_ADD] = OTHER_ADD
            if m > n/2 - 1 and (n/2 - 1)/2 - HOLE_SIZE - (n/2 - 1 - m) <= j <= (n/2 - 1)/2 + HOLE_SIZE:
                la[m][j + OTHER_ADD] = OTHER_ADD
