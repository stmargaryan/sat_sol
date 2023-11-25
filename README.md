
# SAT Problem Generator and Solver

This project includes three Python scripts that work together to generate and check solutions for SAT (Satisfiability) problems. The SAT problems are represented as matrices, and the solution-checking is based on the correctness of these matrix representations.

## Files Description

1. **generate.py**: Contains functions to generate matrices representing SAT problems. There are two types of generation methods:
   - `generate_sat_K_new_random`: Generates a SAT problem with a specific structure (K-SAT).
   - `generate_sat_full_random`: Generates a fully random SAT problem.

2. **check_solution.py**: Provides functions to check if a given solution satisfies a SAT problem and determine the correctness of the solution. It includes:
   - `check_solution`: Checks if a solution satisfies the SAT problem.
   - `check_if_sol_is_correct`: Determines if the checked solution is correct.

3. **main.py**: The main script that integrates the functionality of the other two. It offers an interface to either generate new SAT problems or check existing solutions.

## Usage

### Generating SAT Problems

To generate a new SAT problem, run `main.py` and choose the 'gen' option. You will be prompted to enter:
- Number of ones in the matrix (`num_1`).
- Total number of rows (`M`) (Number of clause).
- Number of columns (`N`) (Number of variables).

The script will generate a SAT problem and save it as a `.npy` file.

### Checking SAT Solutions

Please download input SAT problem matrix files and their corresponding soultion sequences from [HERE][https://drive.google.com/drive/folders/1lkNM7CpooTrn2tBXNHPV4beQVkR_38LZ?usp=share_link]

To check a solution, run `main.py` and choose the 'chk' option. 

**Example:**
When prompted for the input matrix path, you can provide a path like './solutions/input_matricies/fcnf_vars_10000_claus_15000_1.npy'. The script will automatically load the corresponding solution sequence from './solutions/solution_sequence/sol_vars_10000_claus_15000_1.npy' and check its correctness.

## Requirements

- Python 3.x
- NumPy library

## Installation

Ensure you have Python and NumPy installed. Clone this repository or download the files to your local machine.

## Running the Scripts

Navigate to the directory containing the scripts and run:

```bash
python main.py
```

Follow the prompts to either generate a new SAT problem or check an existing solution.
