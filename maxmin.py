def find_high_low(numbers):
    high = low = numbers[0]
    for num in numbers[1:]:
        if num > high:
            high = num
        if num < low:
            low = num
    return [low,high]

print(find_high_low([2,4,1,0,2,0,-1]))
print(find_high_low([20, 50, 12, 6, 14, 8]))
print(find_high_low([100, -100]))