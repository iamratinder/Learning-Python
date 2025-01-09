# copy() : Returns copy of list. This can be done to perform operations on the list without modifying the original list.
colors = ["voilet", "2", "indigo", "blue", "green"]
newlist = colors.copy()   
print(newlist)

# another method using list() :
colors = ["voilet", "2", "indigo", "blue", "green"]
newlist = list(colors)   
print(newlist)

# NOTE if i do :-
l = [2, 3, 9]
m = l      
m[0] = 3       # note that here list 'l' also changes 
n = l.copy()
n[0] = 3       # but here as 'n' was the copy, so original 'l' list is not affected
print(m)
print(l)
