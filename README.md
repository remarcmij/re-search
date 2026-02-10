# re-search

This repo is a small, educational playground for comparing search algorithms and talking about Big O. It includes JavaScript examples as the primary learning path, plus a readable Python version for cross-checking ideas.

## What is in here

- JavaScript search experiments: `search.js` builds sorted arrays of even numbers, runs linear search and binary search, and records timing results so you can compare behavior at different input sizes.
- Python search experiments: `search.py` mirrors the JavaScript logic in Python so you can read the same ideas in a second syntax.
- Notebook walkthrough: `search.ipynb` breaks the code into small sections with explanations and plots so you can see time and iteration counts.
- Plot helper: `plot_results.py` renders the timing results as horizontal bar charts and labels each bar with the search index and iteration count.

## Learning goals

- See the difference between linear search ( _O(n)_ ) and binary search ( _O(log n)_ ).
- Observe how input size affects runtime.
- Connect iteration counts to algorithmic complexity.
- Learn how to measure performance and visualize results.

## How to run (JavaScript)

1. Open `search.js`.
2. Run it with Node:

```bash
node search.js
```

## How to run (Python)

1. Open `search.py` or `search.ipynb`.
2. Run the script:

```bash
python search.py
```

1. Or open the notebook and run cells in order.

## Notes for trainees

- The arrays contain only even numbers. When we add 1 to a target, it becomes odd and is guaranteed to be missing. This is a simple way to test "not found" cases.
- Timing very small arrays can be noisy because overhead and scheduling can dominate the real work.
- The Python code is included for readability, not as a separate learning track.
