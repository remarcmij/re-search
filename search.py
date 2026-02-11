import json

def generate_even_sorted_array(size):
    array = [0] * size
    for i in range(size):
        array[i] = i * 2
    return array


def linear_search(array, target):
    for i, value in enumerate(array):
        if value == target:
            return i
    return -1


def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


array_10m = generate_even_sorted_array(10_000_000)

arrays = {
    "1K": array_10m[:1_000],
    "10K": array_10m[:10_000],
    "100K": array_10m[:100_000],
    "1M": array_10m[:1_000_000],
    "10M": array_10m,
}

functions = [linear_search, binary_search]


def run_experiment(search_function, arrays_map, key, target):
    from time import perf_counter

    array = arrays_map[key]
    start_time = perf_counter()
    index = search_function(array, target)
    end_time = perf_counter()
    return {
        "func": search_function.__name__,
        "key": key,
        "time_ms": (end_time - start_time) * 1000,
        "size": len(array),
        "index": index,
    }


def run_experiments(offset, is_missing=False):
    results = []

    for func in functions:
        for key, array in arrays.items():
            target = array[offset] if offset > 0 else array[len(array) + offset]
            if is_missing:
                # Make the target missing by adding 1 (all elements are even)
                target += 1
            results.append(run_experiment(func, arrays, key, target))


    print(json.dumps(results, indent=2))


print("\nExperiments with target present near the end")
run_experiments(-13)

print("\nExperiments with target NOT present near the end")
run_experiments(-13, True)

print("\nExperiments with target present near the start")
run_experiments(13)

print("\nExperiments with target NOT present near the start")
run_experiments(13, True)
