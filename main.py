import numpy as np
import sys
import os
from generate import generate_sat_K_new_random, generate_sat_full_random
from check_solution import check_solution, check_if_sol_is_correct

def load_matrix(file_path):
    """
    Load a matrix from a .npy file.

    Parameters:
    - file_path: Path to the .npy file

    Returns:
    - matrix: Numpy array loaded from the file
    """
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return None
    return np.load(file_path)

def main():
    choice = input("Choose 'gen' to create new SAT problems or 'chk' to verify existing solutions: ")
    if choice == 'gen':
        num_1 = int(input("Enter number of ones, it can also be 0: "))
        M = int(input("Enter M value: "))
        N = int(input("Enter N value: "))
        # Optionally add input for K if using generate_sat_K_new_random function
        # Generate and save the SAT problem
        sat_problem = generate_sat_full_random(num_1, M, N)
        print(sat_problem)
        filename = f"fcnf_vars_{N}_claus_{M}.npy"
        np.save(filename, sat_problem)
        print(f"Generated SAT problem saved as {filename}")
    elif choice == 'chk':
        input_matrix_path = str(input("Enter input matrics path : "))
        input_matrix = np.load(input_matrix_path)
        print('Successfully loaded input matrix at path ',input_matrix_path)
        sol_matrix_path = input_matrix_path.replace('fcnf', 'sol')#str(input("Enter solution matrics path : "))
        sol_matrix_path = sol_matrix_path.replace('input_matricies', 'solution_sequence')
        print(sol_matrix_path)
        sol_matrix = np.load(sol_matrix_path)
        print('Successfully loaded solution matrix corresponding to the input matrix at path ',sol_matrix_path)
                
        checked_solution = check_solution(input_matrix, sol_matrix, input_matrix.shape[0] - 1, input_matrix.shape[1] - 1)
        check_if_sol_is_correct(checked_solution)
    else:
        print("Invalid choice. Please enter 'generate' or 'check'.")

if __name__ == "__main__":
    main()