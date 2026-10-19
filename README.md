**Performance Evaluation and Comparative Analysis of Insertion Sort and Quick Sort Algorithms**

Objective

To compare Insertion Sort and Quick Sort based on execution time and the number of element comparisons.

Technologies Used

- Python
- Google Colab
- Matplotlib
- Pandas

Experimental Setup

- Input sizes: 100, 1,000, 5,000, and 10,000 elements.
- Input types: Sorted, Reverse-Sorted, and Random.
- Performance metrics: Execution time and element comparisons.

Project Files

- "sorting_analysis.py" — Python implementation of both sorting algorithms.
- "sorting_results.csv" — Experimental results.
- "sorted_time.png" — Execution-time graph for sorted input.
- "reverse_time.png" — Execution-time graph for reverse-sorted input.
- "random_time.png" — Execution-time graph for random input.
- "sorted_comparisons.png" — Comparison graph for sorted input.
- "reverse_comparisons.png" — Comparison graph for reverse-sorted input.
- "random_comparisons.png" — Comparison graph for random input.

Time Complexity

Algorithm| Best Case| Average Case| Worst Case
Insertion Sort| O(n)| O(n²)| O(n²)
Quick Sort| O(n log n)| O(n log n)| O(n²)

Conclusion

The experiment compares the performance of both algorithms under different input conditions. Insertion Sort is effective for small or nearly sorted arrays, while Quick Sort generally performs better for larger arrays.
