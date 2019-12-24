class warmUp2:

    def string_times(self,str, n):
        return str*n

    def front_times(str, n):
        if len(str) < 3:
            return str * 4
        else:
            return str[:3] * n

    def string_bits(str):
        temp = ''
        for i in range(len(str)):
            if i % 2 == 0:
                temp = temp + str[i]
        return temp

    def string_splosion(self,str):
        result=''
        for i in range(len(str)):
            result=result+str[:i+1]
        print (result)
        return result

    def array_count9(self,nums):
        cnt = 0
        for i in range(len(nums)):
            if nums[i]==9:
                cnt = cnt + 1
        return cnt

    def array_front9(nums):
        for i in range(len(nums)):
            if i < 4 and nums[i] == 9:
                return True

        return False


up2=warmUp2()

#print(up2.string_times("test",3))

#print(up2.front_times("test",2))
print (up2.string_splosion("code"))


print (up2.array_count9([1,9,9]))