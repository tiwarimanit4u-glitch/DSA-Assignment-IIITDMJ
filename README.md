# DSA Assignments - IIITDM Jabalpur

Python coursework covering programming basics, algorithm analysis, recursion, and data structures.

**Name:** Manit Tiwari

**Roll No.:** 25BEC058

## Assignments

| File | Topics |
| --- | --- |
| [Assignment1.ipynb](Assignment1.ipynb) | Python basics, collections, strings, functions, file handling, exception handling, GPA calculator, and student records |
| [Assignment-2.py](Assignment-2.py) | Algorithm growth rates, execution-time benchmarks, and quadratic versus linear prefix averages |
| [Assignment-3.py](Assignment-3.py) | Recursive factorial, natural-number sum, power, sorted-order checking, stack, circular queue, and circular deque |

The assignment reference PDFs are included in the repository.

## Running the code

Use Python 3. Assignment 2 requires Matplotlib, and Assignment 1 requires Jupyter Notebook or an editor with notebook support.

Install the dependencies:

```sh
python -m pip install matplotlib notebook
```

Run the scripts from the repository folder:

```sh
python Assignment-2.py
python Assignment-3.py
```

To open Assignment 1:

```sh
python -m notebook Assignment1.ipynb
```

Run the notebook cells in order and enter input when prompted. Choose option `6` to exit the student-record menu.

## Benchmark plots

Assignment 2 prints timing results and saves these plots in the current working directory:

- [lab1_execution_times.png](lab1_execution_times.png): execution times for six algorithm growth classes.
- [lab1_normalized_times.png](lab1_normalized_times.png): timings divided by `n`, `n^2`, and `n log2(n)`.
- [lab2_prefix_averages.png](lab2_prefix_averages.png): comparison of the two prefix-average implementations.

Benchmarks use seven trials and report median execution times. Results vary with the machine and system load.
