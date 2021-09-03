def high_and_low(numbers):
    nums = [int(i) for i in numbers.split()]
    high = str(max(nums))
    low = str(min(nums))
    return (high  + " " +low)