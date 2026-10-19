"""
DAA Project:
Performance Evaluation and Comparative Analysis of
Insertion Sort and Quick Sort Algorithms.

Metrics:
1. Execution time
2. Number of element comparisons

Input types:
1. Sorted
2. Reverse-sorted
3. Random
"""

import random
import time
import csv
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. INSERTION SORT
# --------------------------------------------------
def insertion_sort(arr):
    comparisons = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Shift elements greater than the key
        while j >= 0:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break

        # Insert the key at its correct position
        arr[j + 1] = key

    return comparisons


# --------------------------------------------------
# 2. QUICK SORT
# --------------------------------------------------
def quick_sort(arr):
    comparisons = 0

    def partition(low, high):
        nonlocal comparisons

        # Select a random pivot to reduce
        # the likelihood of consistently poor partitions
        pivot_index = random.randint(low, high)

        arr[pivot_index], arr[high] = (
            arr[high], arr[pivot_index]
        )

        pivot = arr[high]
        i = low - 1

        # Place elements smaller than or equal to pivot
        # on its left side
        for j in range(low, high):
            comparisons += 1

            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        # Place pivot in its correct position
        arr[i + 1], arr[high] = (
            arr[high], arr[i + 1]
        )

        return i + 1

    def sort(low, high):
        if low < high:
            pivot = partition(low, high)

            # Process the smaller partition first
            # to limit recursion depth
            if pivot - low < high - pivot:
                sort(low, pivot - 1)
                sort(pivot + 1, high)
            else:
                sort(pivot + 1, high)
                sort(low, pivot - 1)

    sort(0, len(arr) - 1)

    return comparisons


# --------------------------------------------------
# 3. EXPERIMENT CONFIGURATION
# --------------------------------------------------
sizes = [100, 1000, 5000, 10000]

input_types = ["Sorted", "Reverse", "Random"]

algorithms = {
    "Insertion Sort": insertion_sort,
    "Quick Sort": quick_sort
}

results = []


# --------------------------------------------------
# 4. RUN EXPERIMENTS
# --------------------------------------------------
print("SORTING ALGORITHM PERFORMANCE ANALYSIS")
print("-" * 75)

for size in sizes:
    for input_type in input_types:

        # Generate the required input arrangement
        if input_type == "Sorted":
            original = list(range(size))

        elif input_type == "Reverse":
            original = list(range(size, 0, -1))

        else:
            original = random.sample(
                range(size * 10), size
            )

        # Run both sorting algorithms
        for name, algorithm in algorithms.items():

            arr = original.copy()

            start_time = time.perf_counter()
            comparisons = algorithm(arr)
            elapsed_time = time.perf_counter() - start_time

            # Verify that sorting was successful
            assert arr == sorted(original)

            time_ms = elapsed_time * 1000

            results.append({
                "Size": size,
                "Input Type": input_type,
                "Algorithm": name,
                "Comparisons": comparisons,
                "Time (ms)": round(time_ms, 4)
            })

            print(
                f"{name:15} | "
                f"Size: {size:5} | "
                f"Input: {input_type:7} | "
                f"Comparisons: {comparisons:9} | "
                f"Time: {time_ms:.4f} ms"
            )


# --------------------------------------------------
# 5. SAVE RESULTS TO CSV
# --------------------------------------------------
csv_filename = "sorting_results.csv"

with open(csv_filename, "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "Size",
            "Input Type",
            "Algorithm",
            "Comparisons",
            "Time (ms)"
        ]
    )

    writer.writeheader()
    writer.writerows(results)

print(f"\nResults saved to {csv_filename}")


# --------------------------------------------------
# 6. GENERATE EXECUTION-TIME GRAPHS
# --------------------------------------------------
for input_type in input_types:

    plt.figure(figsize=(9, 5))

    for algorithm_name in algorithms:

        selected = [
            row for row in results
            if row["Input Type"] == input_type
            and row["Algorithm"] == algorithm_name
        ]

        plt.plot(
            [row["Size"] for row in selected],
            [row["Time (ms)"] for row in selected],
            marker="o",
            label=algorithm_name
        )

    plt.title(f"Execution Time - {input_type} Input")
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (ms)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    filename = f"{input_type.lower()}_time.png"
    plt.savefig(filename, dpi=150)
    plt.close()

    print(f"Graph saved: {filename}")


# --------------------------------------------------
# 7. GENERATE COMPARISON-COUNT GRAPHS
# --------------------------------------------------
for input_type in input_types:

    plt.figure(figsize=(9, 5))

    for algorithm_name in algorithms:

        selected = [
            row for row in results
            if row["Input Type"] == input_type
            and row["Algorithm"] == algorithm_name
        ]

        plt.plot(
            [row["Size"] for row in selected],
            [row["Comparisons"] for row in selected],
            marker="o",
            label=algorithm_name
        )

    plt.title(
        f"Element Comparisons - {input_type} Input"
    )

    plt.xlabel("Input Size")
    plt.ylabel("Number of Comparisons")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    filename = f"{input_type.lower()}_comparisons.png"
    plt.savefig(filename, dpi=150)
    plt.close()

    print(f"Graph saved: {filename}")


# --------------------------------------------------
# 8. COMPLETION MESSAGE
# --------------------------------------------------
print("\n" + "=" * 55)
print("EXPERIMENT COMPLETED SUCCESSFULLY!")
print("CSV results and six graphs have been generated.")
print("=" * 55)
