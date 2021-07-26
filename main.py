#  PROBLEM:
'''
Given an array of integers nums and an integer target,
 return indices of the two numbers such that they add up to target
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

from itertools import permutations


def two_sum(nums, target):
    per = list(permutations(nums, 2))
    sol = []
    for x in per:
        if (int(x[0]) + int(x[1])) == int(target):
            sol.append(nums.index(x[0]))
            sol.append(nums.index(x[1]))
            break

    print(sol)


if __name__ == '__main__':
    num = list(map(int, input("enter list of numbers").split(" ")))
    target = input("enter the target number")
    two_sum(num, target)
