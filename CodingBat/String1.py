class String1:

#####################

    def hello_name(name):
        return "Hello " + name + "!"

##################
    def make_abba(a, b):
        return a + b + b + a

###################

    def make_out_word(out, word):
       return out[0:2]+word+out[2:4]


#####################

    def extra_end(str):
         length=len(str)
         if length>2:
             return str[length-2:length]*3
         else:
             return str*3

#########################

    def first_two(str):
        if len(str) >= 2:
           return str[0:2]
        else:
           return str

############################
    def first_half(str):
        mid = int (len(str) / 2)
        print(mid)
        print(str[:3])

############################
    def combo_string(a, b):
       if  len(a)< len(b):
           return a + b + a
       else:
           return b + a + b

###########################

    def non_start(a, b):
      alength=len(a)
      blength = len(b)
      if len(a)<1 and len(a)<len(b):
       return b[1:blength]
      elif len(b)<1 and len(b)<len(a):
        return a[1:length]
     # elif len(a)==len(b):
      else : return a[1:alength]+b[1:blength]


##############################
    def left2(str):
     return str[2:len(str)]+str[:2]


s1=String1

print(s1.make_out_word('<<>>', 'Yay'))
#print(s1.hello_name("bob"))
#print(s1.extra_end("Hello"))
s1.extra_end("Hello")
s1.first_half("WooHoo")
#print(s1.combo_string('xyz', 'ab'))

print(s1.non_start('x', 'ac') )