#Modify the code below so that the function sense, which 
#takes p and Z as inputs, will output the NON-normalized 
#probability distribution, q, after multiplying the entries 
#in p by pHit or pMiss according to the color in the 
#corresponding cell in world.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q = []
    for i in range(len(p)):
        factor = pHit if world[i] == Z else pMiss
        q.append(factor*p[i])
    total = sum(q)
    for i in range(len(q)):
        q[i] = q[i]*1.0/total
    return q

for i in range(len(measurements)):
    p = sense(p, measurements[i])
print p