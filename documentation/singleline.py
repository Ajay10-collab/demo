vec=[0-4,-2,0,2,4]
print([x*2 for x in vec])
print(vec)
for x in range(len(vec)):
   vec[x]=vec[x]*2
    #print(vec)
print(vec)

print([x for x in vec if x>=0])

print([abs(x) for x in vec])

print(vec)


