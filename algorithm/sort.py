from typing import List


def bubble_sort(nums: List[int]) -> List:
    """ Use bubble sort algorithm to sort

        Input:
            nums: List of integers

        Return:
            List of integers
    """
    if not isinstance(nums, list):
        raise ValueError(f"Invalid input {nums}")

    if nums == []:
        return nums

    for i in range(len(nums)):
        # NOTE: it will carry the largest in the unsorted 
        # to the end of the list.
        j_range = len(nums) - 1 - i
        for j in range(j_range):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


def selection_sort(nums: List[int]) -> List:
    """ Use selection sort algorithm to sort

        Input:
            nums: List of integers

        Return:
            List of integers
    """
    if not isinstance(nums, list):
        raise ValueError(f"Invalid input {nums}")

    if nums == []:
        return nums

    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


def insertion_sort(nums: List[int]) -> List:
    """ Use insertion sort algorithm to sort

        Input:
            nums: List of integers

        Return:
            List of integers
    """
    if not isinstance(nums, list):
        raise ValueError(f"Invalid input {nums}")

    if nums == []:
        return nums

    for i in range(1, len(nums)):
        val = nums.pop(i)
        for j in range(0, i):
            if val < nums[j]:
                nums.insert(j, val)
                break
        else:
            nums.insert(i + 1, val)

    return nums


def shell_sort(nums: List[int]) -> List:
    """ Use shell sort algorithm to sort

        Input:
            nums: List of integers

        Return:
            List of integers
    """
    if not isinstance(nums, list):
        raise ValueError(f"Invalid input {nums}")

    if nums == []:
        return nums

    gap = len(nums)
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(nums)):
            val = nums[i]
            j = i
            while j > 0 and nums[j - gap] > val:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = val

    return nums


def merge_sort(nums: List[int]) -> List:
    """ Use merge sort algorithm to sort

        Input:
            nums: List of integers

        Return:
            List of integers
    """
    if not isinstance(nums, list):
        raise ValueError(f"Invalid input {nums}")

    if nums == []:
        return nums

    if len(nums) == 1:
        return nums

    def merge(left, right):
        results = []
        while left and right:
            if left[0] <= right[0]:
                results.append(left.pop(0))
            else:
                results.append(right.pop(0))
        if left:
            results.extend(left)
        else:
            results.extend(right)
        return results

    middle = len(nums) // 2
    left, right = nums[:middle], nums[middle:]

    return merge(merge_sort(left), merge_sort(right))


def merge_sort_iteration(nums: List[int]) -> List:
    """ Use merge sort by iteration algorithm to sort

        Input:
            nums: List of integers

        Return:
            List of integers
    """
    if not isinstance(nums, list):
        raise ValueError(f"Invalid input {nums}")

    if nums == []:
        return nums

    def merge(left, right):
        results = []
        while left and right:
            if left[0] <= right[0]:
                results.append(left.pop(0))
            else:
                results.append(right.pop(0))
        if left:
            results.extend(left)
        else:
            results.extend(right)
        return results

    batch_size = 1
    while batch_size < len(nums):
        start = 0
        while start < len(nums):
            middle = start + batch_size
            end = middle + batch_size
            left, right = nums[start:middle], nums[middle:end]
            nums[start:end] = merge(left, right)
            start = end
        batch_size *= 2

    return nums


# FIXME: this is still not perfect, it will fail
#  with [0] * 1000 test case
# RecursionError: maximum recursion depth exceeded in comparison
def quick_sort(nums: List[int]) -> List:
    """ Use quick sort algorithm to sort

        Input:
            nums: List of integers

        Return:
            List of integers
    """
    if not isinstance(nums, list):
        raise ValueError(f"Invalid input {nums}")

    if nums == []:
        return nums

    def _sort(nums, left, right):
        if left >= right:
            return nums
        
        pivot = left
        val = nums[pivot]
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= val:
                j -= 1
            while i < j and nums[i] <= val:
                i += 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[pivot] = nums[pivot], nums[i]
        nums = _sort(nums, left, i - 1)
        nums = _sort(nums, i + 1, right)
        return nums

    return _sort(nums, 0, len(nums) - 1)
