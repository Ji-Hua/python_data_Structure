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
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

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
        for j in range(i+1, len(nums)):
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
            nums.insert(i+1, val)

    return nums