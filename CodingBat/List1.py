class List1:
    def same_first_last(nums):
        if len(nums) >= 1 and nums[0] == nums[len(nums) - 1]:
            return True
        else:
            return False

############################

    def make_pi(self):
        return [3, 1, 4]

############################

    def common_end(a, b):
     if a[0]==b[0] or a[len(a)-1]==b[len(b)-1]:
      return True
     else:
       return False
############################

    def sum3(nums):
      temp = 0
      for i in range(len(nums)):
        temp = temp + nums[i]
        return temp


#########################

    def reverseArray(nums):
     temp = []

     length = len(nums) -1
     for i in range(len(nums)):
        t=nums[length]
        temp.append(t)
        length= length-1

     return temp



    def reverse3(nums):
     temp = []
     r=1
     length=len(nums)-1
     for i in range(len(nums)):
        t=nums[length]
        temp.append(t)
        length= length-1

     return temp

############################
    # Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

    def rotate_left_3(nums):

        temp = []
        temp.insert(0,nums[1])
        temp.insert(1,nums[2])
        temp.insert(2,nums[0])

        return temp

###############################################################
# Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all
# the other elements to be that value. Return the changed array.


    def max_end3(nums):
      temp=[]
      length=len(nums)
      k=len(nums)-1
      if nums[0]>nums[k]:
          for i in range(length):
             temp.insert(i,nums[0])
      else:
            for i in range(length):
                temp.insert(i,nums[k])
      return temp

##############################################################
    # Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2,
    # just sum up the elements that exist, returning 0 if the array is length 0.


    def sum2(nums):
       if len(nums)<=0:
         return 0
       elif len(nums) == 1:
         return nums[0]
       else:
         return nums[0]+nums[1]

#############################################
    # Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

    def middle_way(a, b):
      temp=[]
      a_mid=int(len(a)%2)
      b_mid =int(len(b)%2)
      temp.insert(0,a[a_mid])
      temp.insert(1,b[b_mid])
      return temp


#############################################
# Given an array of ints, return a new array length 2 containing the first and last elements from the original array.
# The original array will be length 1 or more.
    def make_ends(nums):
        temp=[]
        temp.insert(0,nums[0])
        temp.insert(1,nums[len(nums)-1])
        return temp


#############################################
#Given an int array length 2, return True if it contains a 2 or a 3.


    def has23(nums):
        flag=False
        for i in range(len(nums)):
            if nums[i]==3 or nums[i]==2:
                flag= True

        return flag


##################################################

l1=List1
#print(l1.reverse3([1, 2, 3]))
#print(l1.rotate_left_3([1, 2, 3]))

#print(l1.max_end3([11, 5, 9]))
#print(l1.sum2([11, 5, 9]))
#print(l1.middle_way([1, 2, 3], [4, 5, 6]))
print(l1.has23([1, 2, 3]))
