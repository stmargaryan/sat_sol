import numpy as np

def generate_sat_K_new_random(num_1, M, N, K):
    """
    Generates a K-SAT problem with a specific structure.

    Parameters:
    - num_1: Number of rows with only 1s
    - M: Total number of rows (the number of clauses)
    - N: Number of columns (the number of variables)
    - K: Maximum number of 1s in a row (for K-SAT)

    Returns:
    - fcnf: A matrix representing the SAT problem
    """
    matrix = np.zeros((M, N))
    # Create rows with only num_1 ones
    for i in range(num_1):
        row = np.zeros(N)
        choice_of_K = np.random.randint(1, K + 1, size=1)
        ones = np.random.choice(N, choice_of_K, replace=False)
        row[ones] = 1
        matrix[i] = row
    # Create remaining rows with -1s, 1s and 0s
    for i in range(num_1, M):
        row = np.zeros(N)
        choice_of_K = np.random.randint(1, K + 1, size=1)
        nonzeros = np.random.choice(N, choice_of_K, replace=False)
        nonzero_vals = np.random.choice([-1, 1], choice_of_K)
        row[nonzeros] = nonzero_vals
        # Ensure that the row doesn't only contain 0s
        while np.all(row == 0):
            choice_of_K = np.random.randint(1, K + 1, size=1)
            nonzeros = np.random.choice(N, choice_of_K, replace=False)
            choice_of_K = np.random.randint(1, K + 1, size=1)
            nonzero_vals = np.random.choice([-1, 1], choice_of_K)
            row[nonzeros] = nonzero_vals
        matrix[i] = row

    np.random.shuffle(matrix)

    w, h = matrix.shape
    temp = np.zeros((w + 1, h + 1), dtype=np.int16)
    temp[1:, 1:] = matrix
    fcnf = temp
    return fcnf

def generate_sat_full_random(num_1, M, N):
    """
    Generates a fully random SAT problem.

    Parameters:
    - num_1: Number of rows with only 1s
    - M: Total number of rows (number of clauses)
    - N: Number of columns (number of variables)

    Returns:
    - fcnf: A matrix representing the SAT problem
    """
    K = np.random.randint(1, N+1)
    def generate_weighted_probabilities(N):
        weights = np.linspace(N, 1, N)  # Weights decreasing from N to 1
        total = np.sum(weights)
        probabilities = weights / total  # Normalizing to create a probability distribution
        return probabilities
        
    matrix = np.zeros((M, N))

    # Create rows with only num_1 ones
    for i in range(num_1):
        row = np.zeros(N)
        K = np.random.randint(1, N+1)
        probabilities = generate_weighted_probabilities(K)
        choice_of_K = np.random.choice(np.arange(1, K + 1), p=probabilities)  # Selecting K with weighted probability
        ones = np.random.choice(N, choice_of_K, replace=False)
        row[ones] = 1
        matrix[i] = row

    # Create remaining rows with -1s, 1s and 0s
    for i in range(num_1, M):
        row = np.zeros(N)
        K = np.random.randint(1, N+1)
        probabilities = generate_weighted_probabilities(K)
        choice_of_K = np.random.choice(np.arange(1, K + 1), p=probabilities)  # Selecting K with weighted probability
        nonzeros = np.random.choice(N, choice_of_K, replace=False)
        nonzero_vals = np.random.choice([-1, 1], choice_of_K)
        row[nonzeros] = nonzero_vals

        # Ensure that the row doesn't only contain 0s
        while np.all(row == 0):
            choice_of_K = np.random.choice(np.arange(1, K + 1), p=probabilities)  # Selecting K with weighted probability
            nonzeros = np.random.choice(N, choice_of_K, replace=False)
            nonzero_vals = np.random.choice([-1, 1], choice_of_K)
            row[nonzeros] = nonzero_vals

        matrix[i] = row

    np.random.shuffle(matrix)

    w, h = matrix.shape
    temp = np.zeros((w + 1, h + 1), dtype=np.int16)
    temp[1:, 1:] = matrix
    fcnf = temp
    return fcnf
