class CB_Prac:



    def sleep_in(self,weekday, vacation):
        if not weekday or vacation:
           return True
        else :
           return False

    def monkey_trouble(self,a_smile, b_smile):
        if a_smile and b_smile:
           return True
        else:
            return False

    def sum_double(a, b):
        if not a == b:
            return a + b
        else:
            return (a + b) * 2


    def diff21(n):
     if 21 < n:
        return 2 * abs(21 - n)
     else:
        return abs(n - 21)


     def makes10(self,a, b):
         if a == 10 or b == 10:
             return True
         else:
             sum = a + b
         return sum == 10


    def near_hundred(self,n):
        #if(100-abs(n)<=10) or (200-abs(n)<=10):
        return abs(100 - n) <= 10 or abs(200 - n) <= 10

    def not_string(str):
        if "not" in str:
            return str
        else:
            return "not " + str


    def missing_char(self,str,n):
        fst=str[:n]
        second=str[n+1:]
        return fst+second

    def front3(self,str):
        str=str[:3]
        if len(str)<=3:
           return str*3
        else:
            return str

    def not_string(str):
        if "not" in str:
            return str
        else:
            return "not " + str



    def front_back(self,str):
        print(len(str))
        if len(str)==1:
            return str
        else :
            fst=str[0]
            last=str[len(str)-1]
            mid=str[1:len(str)-1]
            return last+mid+fst

    def pos_neg(a, b, negative):
        if negative == True:
            return (a < 0) and (b < 0)
        return (a * b) < 0

cb=CB_Prac()


#print(cb.sleep_in(True,True))
#print(cb.monkey_trouble(False,False))

#print(cb.near_hundred(90))
#print(cb.missing_char('kitten', 1))
#print(cb.front3('Ja'))
print(cb.front_back('a'))

