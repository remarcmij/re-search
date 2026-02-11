function generateEvenSortedArray(size) {
  const array = new Array(size);
  for (let i = 0; i < size; i++) {
    array[i] = i * 2;
  }
  return array;
}

function linearSearch(array, target) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === target) {
      return i;
    }
  }
  return -1;
}

function binarySearch(array, target) {
  let left = 0;
  let right = array.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (array[mid] === target) {
      return mid;
    } else if (array[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return -1;
}

const array10M = generateEvenSortedArray(10_000_000);

const arrays = {
  '1K': array10M.slice(0, 1_000),
  '10K': array10M.slice(0, 10_000),
  '100K': array10M.slice(0, 100_000),
  '1M': array10M.slice(0, 1_000_000),
  '10M': array10M,
};

const functions = [linearSearch, binarySearch];

const runExperiment = (searchFunction, arrays, key, target) => {
  const array = arrays[key];
  const startTime = performance.now();
  const index = searchFunction(array, target);
  const endTime = performance.now();
  return {
    func: searchFunction.name,
    key,
    time_ms: endTime - startTime,
    size: array.length,
    index,
  };
};

function runExperiments(offset, isMissing = false) {
  const results = [];

  for (const func of functions) {
    for (const key in arrays) {
      const array = arrays[key];
      let target;
      if (offset > 0) {
        // If offset is positive, target is at the offset index from the start
        target = array[offset];
      } else {
        // If offset is negative, target is at the offset index from the end
        target = array[array.length + offset];
      }
      if (isMissing) {
        // Make the target missing by adding 1 (since all elements are even,
        // this will ensure it's not in the array)
        target++;
      }
      results.push(runExperiment(func, arrays, key, target));
    }
  }

  console.table(results);
}

console.log('\nExperiments with target present near the end');
runExperiments(-13);

console.log('\nExperiments with target NOT present near the end');
runExperiments(-13, true);

console.log('\nExperiments with target present near the start');
runExperiments(13);

console.log('\nExperiments with target NOT present near the start');
runExperiments(13, true);
