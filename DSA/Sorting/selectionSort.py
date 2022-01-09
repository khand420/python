def selectionSort(nums):

    for i in range(5):
        minPostion = i
        for j in range(i,6):
            if nums[j] < nums[minPostion]:
                minPostion = j


        temp = nums[i]
        nums[i] = nums[minPostion]
        nums[minPostion] = temp        

        # print(nums)    

nums = [5,3,8,6,7,2] 
selectionSort(nums)
print(nums)       