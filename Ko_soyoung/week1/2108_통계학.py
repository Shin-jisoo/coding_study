import sys

numbers = []
N = int(sys.stdin.readline())
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()


def mean(nums):
    return round(sum(nums) / len(nums))


def median(nums):
    return nums[len(nums) // 2]


def mode(nums):
    numbers_dict = {}
    for num in nums:
        if num not in numbers_dict.keys():
            numbers_dict[num] = 1
        else:
            numbers_dict[num] += 1

    most_exist = max(numbers_dict.values())
    result = []
    for key, value in numbers_dict.items():
        if value == most_exist:
            result.append(key)
            if len(result) >= 2:
                return result[-1]
    return result[0]


def scope(nums):
    return nums[-1] - nums[0]


print(mean(numbers))
print(median(numbers))
print(mode(numbers))
print(scope(numbers))
