from __future__ import annotations

def twoSum(nums: list[int], target: int)->list[int]:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            answer =nums[i]+nums[j]
            if(answer==int(target)):  
                return [i,j]
        
  
print("input : ")
nums = list(map(int,input() .split()))
print("target : ")
target = input()
output = twoSum(nums,target)

print(output)

        
    







