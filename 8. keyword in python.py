import keyword as kw

i = 0 

for k in kw.kwlist:
    i+=1
    print(k)

print(f"Total number of keywords in python is: {i}")