name = "Ratinder"  # length : 8   indexes[0 to 7]

# Slicing :- 
print(name[0:4])   # includes 0th index but NOT 4 -> Rati
print(name[2:9])   # includes 2nd index but NOT 9 -> tinder
print(name[:5])    # by default consider start from 0th index -> Ratin
print(name[3:])    # by default consider last index as length of string -> inder

# Negative slicing : (both below are same)
print(name[-4:-1])                     # same as -> name[ length-4 : length-1 ] 
print(name[len(name)-4:len(name)-1])   # hence      name[ 8-4 : 8-1 ]             -> nde

a ="cherry"
print(a[-4:-2])  # will give output : er