def longest_consecutive(numbers):
    nums, longest_streak, = set(numbers), 0

    for num in nums:
        if num - 1 not in nums:
            streak = 1
            while num + 1 in nums:
                streak += 1
                num = num + 1
            longest_streak = streak if streak > longest_streak else longest_streak
    return longest_streak

