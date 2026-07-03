# Two sum - to find the indices of 2 numbers in an array which when added gives the target number.

# BRUTE FORCE APPROACH : Check every possible pair of numbers. If their sum equals the target, return their indices.
# TIME COMPLEXITY : O(n²) Outer loop runs n times. Inner loop runs about n times.
# SPACE COMPLEXITY : O(1) No extra data structures are used.

nums = [11,2,7,15]
target = 9

def two_Sum(nums,target):
    for i in range(len(nums)): # (0,4) i=1
        for j in range(i + 1,len(nums)): # (1,4) j=2
            if nums[i] + nums[j] == target: # num[1]+num[2]=2+7=9
                return [i,j]
    
result = two_Sum(nums,target)
print(result)

# OPTIMISED APPROACH : Instead of checking every pair, Store each number in a dictionary.
                     # Compute the number needed to reach the target (target - current_number).
                     # If that number is already in the dictionary, you've found the answer.
# TIME COMPLEXITY : O(n) Only one loop. Dictionary lookups are approximately constant time.
# SPACE COMPLEXITY : O(n) The dictionary may store all numbers.

nums = [11,2,7,15]
target = 9

def twoSum(nums,target):
  seen = {}
  for i in range(len(nums)): # (0,4) i=2
      complement = target - nums[i] # 9-7=2 
      if complement in seen: 
          print([seen[complement],i])# 1,2

      seen[nums[i]] = i # seen={11:0,2:1,}

twoSum(nums,target)

