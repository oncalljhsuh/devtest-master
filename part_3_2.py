import numpy as np

# A matrix defining how different locations (home, work, school) infect other people.
# Rows are infectors, columns are infectees.
infect_matrix = np.array([
    [0.9, 0.05, 0.05],
    [0.05, 0.9, 0.05],
    [0.05, 0.05, 0.9],
])

# Compartments of people (home, work, school).
infectors = np.array([10, 19, 35])  # people who can infect other people

infected = np.dot(infect_matrix, infectors)  # repalce for-loops with numpy.dot fuction

print("Number of people infected (home, work, school):", infected)
