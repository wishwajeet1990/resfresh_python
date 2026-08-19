import time as t

def gen_val():
    for i in range(1000):
        yield i

my_val = gen_val()

s_t = t.time()
for i in my_val:
    print(i)
e_t =  t.time()

y_time  =  e_t - s_t

my_list  =  list(range(1000))

s_t = t.time()
for i in my_list:
    print(i)
e_t =  t.time()

l_time  =  e_t - s_t

print("Total Yeild time =  ",+y_time,"\tTotal loop time  =  ",+l_time)

