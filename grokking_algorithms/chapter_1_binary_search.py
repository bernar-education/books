# Big O Notation: O(log n)

import random

ages = list(range(1, 101))
target_age = random.randint(1, 100)

def binary_search(array: list[int], target: int) -> int | None:
    low, high = 0, len(array) - 1
    step_count = 0

    print("Searching for age:", target)

    while low <= high:
        step_count += 1
        mid = (low + high) // 2
        guess = array[mid]
        if guess == target:
            print("Steps taken:", step_count)
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    print("Steps taken:", step_count)
    return None

index = binary_search(ages, target_age)
print(ages[index])
