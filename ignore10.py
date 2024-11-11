```
Write a function that returns a list of numbers from an array, excluding any sections that start with a 1 and extend to the next 0. Also, compute the sum of the numbers in the resulting list. Ignore any numbers from a 1 that is followed by another 1 until a 0 is found.


Function Signature:
def ignore10(arr):
	pass
Parameters:
arr (List[int]): An array of integers from which sections will be ignored as described.
Returns:


Tuple[List[int], int]: A tuple containing the modified array and the sum of its elements.
Examples
Example 1:
Input: arr = [6, 1, 7, 0, 2, 5, 6, 1, 3]
Output: ([6, 2, 5, 6, 1, 3], 23)
Explanation:
The numbers between the first 1 and the next 0 (inclusive) are ignored, which are 1, 7, 0. The subsequent 1 is not followed by a 0, hence it and the numbers following it are included.
Example 2:
Input: arr = [4, 0, 6, 1, 4, 6, 1, 2]
Output: ([4, 0, 6, 1, 4, 6, 1, 2], 24)
Explanation:
There is no 1 followed by 0 that encloses numbers to ignore. All numbers are included.
Example 3:
Input: arr = [4, 0, 6, 1, 2, 4, 1, 1, 3, 0, 2]
Output: ([4, 0, 6, 2], 12)
Explanation:
The sequence starting with 1 at index 3 ends with 0 at index 9. All numbers between these indices are ignored.
Example 4:
Input: arr = [0, 6, 1, 1, 9, 1, 3, 0, 2]
Output: ([0, 6, 2], 8)
Explanation:
The numbers between the first 1 and the next 0 (inclusive) are ignored, which includes all numbers from the first 1 to the 0.
Constraints
1 <= arr.length <= 10^5
-10^9 <= arr[i] <= 10^9
Notes
If a sequence starting with 1 does not have a subsequent 0, then the 1 and the numbers following it up to the end of the array are included.
If a 1 follows another 1, continue ignoring until a 0 is found.
```
def ignore10(arr):
    res, totalsum, tempsum, is1, start = [], 0, 0, False, -1
    for i, v in enumerate(arr):
        if is1:
            if v == 0:
                tempsum, is1 = 0, False
            else:
                tempsum += v
        else:
            if v == 1:
                start, is1 = i, True
                tempsum += v
            else:
                totalsum += v
                res.append(v)
    if is1 and start > -1:
        for v in arr[start:]:
            res.append(v)
        totalsum += tempsum
    return (res, totalsum)
print(ignore10([6, 1, 7, 0, 2, 5, 6, 1, 3]))
print(ignore10([4, 0, 6, 1, 4, 6, 1, 2]))
print(ignore10([4, 0, 6, 1, 2, 4, 1, 1, 3, 0, 2]))
print(ignore10([0, 6, 1, 1, 9, 1, 3, 0, 2]))
print(ignore10([1]))
