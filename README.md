# Python Foundations

Python practice for my AI Engineering roadmap (Phase 1: Python + Data).

## Why this repo

I already know Java/OOP, data structures and databases. This repo is where I practice Python and write small scripts myself, without copying tutorials.

## Plan

- Week 1: Python core (syntax, functions, modules, exceptions, file handling)
- Week 2: NumPy + OOP revision
- Week 3: Pandas + data cleaning
- Week 4: Small data-analysis project

## Structure

```text
Week-01/
  Day-01/   types demo, FizzBuzz, stats, experiments
  Day-02/   functions, exceptions, file handling, word counter
  Day-03/   comprehensions, modules, CSV and JSON

Week-02/
  Day-01/   NumPy arrays, reshaping, vectorization, performance and statistics
```

## Progress

### Week 1

#### Day 1

- `types_demo.py`: basic data types and `type()`
- `fizzbuzz.py`: FizzBuzz for 1 to 50
- `stats.py`: min, max and average with a loop and with built-ins, using `main()` and `if __name__ == "__main__"`
- `experiments.py`: Java vs Python checks (`/` vs `//`, reassigning a variable, big integers, lists changed inside functions, `id()`)

#### Day 2

- `functions.py`: default arguments and multiple return values
- `exceptions.py`: `try` / `except` / `finally`
- `files_basic.py`: write, append and read files, and handle a missing file
- `word_counter.py`: counts words in a text file and prints the top 5

#### Day 3

- `comprehensions.py`: list and dict comprehensions
- `math_utils.py` and `app.py`: my own module, imports, and `if __name__ == "__main__"`
- `csv_reader.py`: reads `students.csv`, skips invalid rows, prints statistics
- `json_demo.py`: writes and reads JSON, adds grades, handles broken or missing files

### Week 2

#### Day 1 — NumPy

- Created NumPy arrays and practiced array shapes.
- Practiced `reshape()`, `transpose()` and `ravel()`.
- Compared Python loops and list comprehensions with NumPy vectorized operations.
- Benchmarked square-and-sum operations to compare performance.
- Used NumPy to calculate the mean, minimum and maximum of marks, and compared the results with the Week 1 report.
- Updated `.gitignore` to exclude local `.vscode/` and `.venv/` folders.

## How to run

```bash
python Week-01/Day-02/word_counter.py
```

Replace the path with any script in the repo.
