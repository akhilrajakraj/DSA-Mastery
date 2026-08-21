"""Big-O practice from Foundations.

These exercises are intentionally kept simple so the focus stays on
reasoning about time and extra space complexity.
"""


def exercise_1(numbers):
    """Return the first element.

    Expected complexity:
        Time: O(1)
        Extra space: O(1)
    """
    return numbers[0]


def exercise_2(numbers):
    """Print every element.

    Expected complexity:
        Time: O(n)
        Extra space: O(1)
    """
    for number in numbers:
        print(number)


def exercise_3(numbers):
    """Print every ordered pair.

    Expected complexity:
        Time: O(n^2)
        Extra space: O(1)
    """
    for first in numbers:
        for second in numbers:
            print(first, second)


def exercise_4(numbers):
    """Create a doubled copy.

    Expected complexity:
        Time: O(n)
        Extra space: O(n)
    """
    result = []
    for number in numbers:
        result.append(number * 2)
    return result


def exercise_5(numbers):
    """Print pairs using a triangular nested loop.

    Expected complexity:
        Time: O(n^2)
        Extra space: O(1)
    """
    for i in range(len(numbers)):
        for j in range(i):
            print(numbers[i], numbers[j])


def exercise_6(numbers):
    """O(log n) outer loop with O(n) inner work.

    Expected complexity:
        Time: O(n log n)
        Extra space: O(1)
    """
    i = 1
    while i < len(numbers):
        for j in range(len(numbers)):
            print(i, j)
        i *= 2


if __name__ == "__main__":
    sample = [1, 2, 3]
    print("Exercise 1:", exercise_1(sample))
    exercise_2(sample)
    exercise_3(sample)
    print("Exercise 4:", exercise_4(sample))
    exercise_5(sample)
    exercise_6(sample)
