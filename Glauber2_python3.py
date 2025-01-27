import numpy as np

# In NumPy 1.25+ it’s common to do threshold=None to show the entire array.
# or np.set_printoptions(threshold=np.inf)
np.set_printoptions(threshold=None)

n = 40               # DEPTH OF THE INTERLACING ARRAY
sim_steps = 50000     # Number of Glauber steps (times height of the system) per one simulation
biga = 5

la = np.zeros((n, n))
laprint = np.zeros((n, n))

# BOUNDARY CONDITIONS
AAA = n
addition = -AAA // 2 - 1
HOLE_SIZE = 8
OTHER_ADD = 8

# MAKE A PLAIN HEXAGON ; INITIAL CONDITION SPEEDS UP THE CONVERGENCE
for m in range(n):
    for j in range(m + 1):
        # integer division n//2 used for clarity
        if m >= n // 2:
            if 0 <= j <= m - n // 2:
                la[m, j] = AAA + 1 + addition
            if j >= n // 2:
                la[m, j] = 1 + addition

for a in range(biga):
    # Write out the current configuration to file
    with open('outputXX' + str(a) + '.txt', 'w') as f:
        f.write("{")
        for m in range(n):
            f.write("{")
            for k in range(n):
                if k == n - 1:
                    f.write(str(la[m, k]))
                else:
                    f.write(str(la[m, k]) + ", ")
            if m == n - 1:
                f.write("}")
            else:
                f.write("},")
        f.write("}")

    print(a)  # Python 3 style print

    # Perform Glauber updates
    for x in range(1, sim_steps * n):
        if x % 50000 == 0:
            print(x / (sim_steps * n))
        # random_integers(1, n-1) -> randint(1, n) is the direct replacement:
        m_rand = np.random.randint(1, n)
        j_rand = np.random.randint(1, m_rand + 1)  # inclusive of m_rand

        # The "HOLE" conditions:
        if (m_rand == n // 2 - 1
            and (m_rand / 2.0 - HOLE_SIZE) <= j_rand <= (m_rand / 2.0 + HOLE_SIZE)):
            la[m_rand, j_rand + OTHER_ADD] = OTHER_ADD
        if (m_rand < n // 2 - 1
            and ((n // 2 - 1) / 2.0 - HOLE_SIZE) <= j_rand
            and j_rand <= ((n // 2 - 1) / 2.0 + HOLE_SIZE) - (n // 2 - 1 - m_rand)):
            la[m_rand, j_rand + OTHER_ADD] = OTHER_ADD
        if (m_rand > n // 2 - 1
            and ((n // 2 - 1) / 2.0 - HOLE_SIZE - (n // 2 - 1 - m_rand)) <= j_rand
            and j_rand <= ((n // 2 - 1) / 2.0 + HOLE_SIZE)):
            la[m_rand, j_rand + OTHER_ADD] = OTHER_ADD

        coin = np.random.random()
        if coin < 0.5:
            # Attempt "increase" move
            if la[m_rand - 1, j_rand - 1] < la[m_rand, j_rand - 1]:
                if m_rand == 1 or j_rand == 1:
                    la[m_rand - 1, j_rand - 1] += 1
                else:
                    if la[m_rand - 1, j_rand - 1] < la[m_rand - 2, j_rand - 2]:
                        la[m_rand - 1, j_rand - 1] += 1
        else:
            # Attempt "decrease" move
            if la[m_rand - 1, j_rand - 1] > la[m_rand, j_rand]:
                if m_rand == 1 or j_rand == m_rand:
                    la[m_rand - 1, j_rand - 1] -= 1
                else:
                    if la[m_rand - 1, j_rand - 1] > la[m_rand - 2, j_rand - 1]:
                        la[m_rand - 1, j_rand - 1] -= 1

    # Enforce hole boundaries one last time after the simulation steps
    for m_chk in range(n):
        for j_chk in range(n):
            if (m_chk == n // 2 - 1
                and (m_chk / 2.0 - HOLE_SIZE) <= j_chk <= (m_chk / 2.0 + HOLE_SIZE)):
                la[m_chk, j_chk + OTHER_ADD] = OTHER_ADD
            if (m_chk < n // 2 - 1
                and ((n // 2 - 1) / 2.0 - HOLE_SIZE) <= j_chk
                and j_chk <= ((n // 2 - 1) / 2.0 + HOLE_SIZE) - (n // 2 - 1 - m_chk)):
                la[m_chk, j_chk + OTHER_ADD] = OTHER_ADD
            if (m_chk > n // 2 - 1
                and ((n // 2 - 1) / 2.0 - HOLE_SIZE - (n // 2 - 1 - m_chk)) <= j_chk
                and j_chk <= ((n // 2 - 1) / 2.0 + HOLE_SIZE)):
                la[m_chk, j_chk + OTHER_ADD] = OTHER_ADD
