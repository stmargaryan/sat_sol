import numpy as np

def check_solution(input_matrix, Solution, m, n):
    """
    Checks if the provided solution satisfies the SAT problem.

    Parameters:
    - input_matrix: The SAT problem matrix
    - Solution: The proposed solution
    - n: Number of variables
    - m: Number of clauses

    Returns:
    - sat_clauses: Array indicating if each clause is satisfied
    """
    # Adjust indices to match Python's 0-based indexing
    input_matrix = input_matrix[1:, 1:]
    Solution = Solution[1:]

    # Create a matrix where each element is True if the condition for SAT is met
    condition_matrix = (input_matrix == -1) & (Solution == 0)[:, np.newaxis] | (input_matrix == 1) & (Solution == 1)[:, np.newaxis]

    # Any clause is satisfied if it contains at least one True
    sat_clauses = np.any(condition_matrix, axis=0)

    # Convert boolean array to int and add a zero at the beginning to match the original format
    return np.concatenate(([0], sat_clauses.astype(np.int8)))

def check_if_sol_is_correct(checked_solution):
    """
    Determines if the solution is correct for the SAT problem.

    Parameters:
    - checked_solution: Array from check_solution function

    Returns:
    - Boolean indicating if the solution is correct
    """
    # Check if all clauses (except the first dummy element) are satisfied
    is_correct = np.all(checked_solution[1:])
    print("Is Solution Correct: ", is_correct)