class warmUp2:

    def string_times(self,str, n):
        return str*n

    def front_times(str, n):
        if len(str) < 3:
            return str * 4
        else:
            return str[:3] * n


up2=warmUp2()

#print(up2.string_times("test",3))

print(up2.front_times("test",2))