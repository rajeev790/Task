def find_duplicate(nums):
    slow, fast = nums[0], nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

# Example usage:
nums = [1, 3, 4, 2, 2]
print(find_duplicate(nums))  # Output: 2
