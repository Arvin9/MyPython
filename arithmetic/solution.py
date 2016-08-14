# -*- encoding:utf-8 -*-

def TwoSum( nums, target):
    length = len(nums)
    target_list = []
    for i in range(length):
        for j in range(i+1,length):
            if (nums[i] + nums[j] == target):
                print nums[i] ,nums[j]
                target_list.append(i)
                target_list.append(j)
                return target_list



if __name__ == "__main__":
    nums = [5,9,11,7]
    print TwoSum(nums,18)
