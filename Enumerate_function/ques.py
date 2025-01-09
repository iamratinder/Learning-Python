D = dict()
for x in enumerate(range(2)):   
    D[x[0]] = x[1]              
    D[x[1]+7] = x[0]            
print(D)

# first loop :
'''
x = (0,0)
D[0] = 0
D[0+7] = 0    '''

# second loop :
'''
x = (1,1)
D[1] = 1
D[1+7] = 1    '''