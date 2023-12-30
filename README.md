# Disk Scheduling Algorithms Implementation and Analysis

## Overview

This project implements and analyzes the performance of three disk scheduling algorithms: SCAN, C-SCAN, and C-LOOK. Disk scheduling is a critical aspect of operating systems that involves optimizing data access on disk drives. The goal is to compare the seek times of each algorithm for various sets of random requests on a disk drive with 200 cylinders.

## Project Structure

- `src/`: Contains the source code for the disk scheduling algorithms.
- `results/`: Will store the results of the algorithm executions.
- `report/`: Includes the final report and any additional documentation.
- `appendix/`: Contains the source code and any extra data/graphs for reference.

## How to Run

1. Clone this repository.
2. Navigate to the `src/` directory.
3. Execute the main program with the chosen programming language (e.g., `python main.py`).

## Requirements

- [Specify any dependencies or requirements here]

## Implementation Details

- `DiskScheduler` class in `main.py` encapsulates SCAN, C-SCAN, and C-LOOK algorithms.
- Random requests are generated using the `generate_requests` function.
- Average and worst-case seek times are calculated and printed.

## Results

Results of the algorithm executions, including average and worst-case seek times for different request sizes, will be stored in the `results/` directory.

## Report

The detailed analysis, strengths, weaknesses, and recommendations are presented in the `report/` directory. Please refer to [report/README.md] for more information.

## Contribution

This project is a group assignment for the Operating Systems course. Each group member contributed to the implementation, testing, and report writing.

## Deadline

The submission due date is 11th January 2024 (11.59 PM).

## Grading Rubric

- Correctness and completeness of the implementation of the algorithms.
- Accuracy and clarity of the results and analysis.
- Organization and presentation of the report.

## License

[Specify the license for your project, e.g., MIT License]

---

**Note:** Remember to update the sections with specific details such as dependencies, instructions, and any additional information relevant to your project.
